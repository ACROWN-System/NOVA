import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

from NOVA.health import (
    _state_defaults,
    fingerprint,
    load_health_state,
    observation_freshness,
    provider_health_status,
    record_probe,
    remember_observation,
    reusable_analysis,
)


class HealthTests(unittest.TestCase):
    def test_health_state_loader_missing_file_uses_defaults(self):
        with tempfile.TemporaryDirectory(prefix="nova-missing-health-state-") as temp_dir:
            path = Path(temp_dir) / "health_state.json"

            state = load_health_state(path)

            self.assertEqual(state["targets"], {})
            self.assertEqual(state["observations"], {})
            self.assertEqual(state["events"], {})
            self.assertEqual(state["provider_rotation"], {"ai-heart": {
                "next_index": 0,
                "next_provider": None,
                "last_probe_providers": [],
                "last_scheduled_provider": None,
                "last_scheduled_at": None,
            }})
            self.assertFalse(path.exists())

    def test_health_state_loader_rejects_malformed_json_without_modifying_file(self):
        invalid_json = '{"events": '
        with tempfile.TemporaryDirectory(prefix="nova-corrupt-health-state-") as temp_dir:
            path = Path(temp_dir) / "health_state.json"
            path.write_text(invalid_json, encoding="utf-8")

            with self.assertRaisesRegex(RuntimeError, "not valid JSON"):
                load_health_state(path)

            self.assertEqual(path.read_text(encoding="utf-8"), invalid_json)

    def test_health_state_loader_rejects_undecodable_bytes_without_modifying_file(self):
        invalid_bytes = bytes((0xFF, 0xFE, 0x80))
        with tempfile.TemporaryDirectory(prefix="nova-undecodable-health-state-") as temp_dir:
            path = Path(temp_dir) / "health_state.json"
            path.write_bytes(invalid_bytes)

            with self.assertRaisesRegex(RuntimeError, "could not be read"):
                load_health_state(path)

            self.assertEqual(path.read_bytes(), invalid_bytes)

    def test_health_state_loader_rejects_read_error_without_modifying_file(self):
        original = '{"events": {}}'
        with tempfile.TemporaryDirectory(prefix="nova-unreadable-health-state-") as temp_dir:
            path = Path(temp_dir) / "health_state.json"
            path.write_text(original, encoding="utf-8")

            with patch.object(Path, "read_text", side_effect=PermissionError("permission denied")):
                with self.assertRaisesRegex(RuntimeError, "could not be read"):
                    load_health_state(path)

            self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_health_state_loader_rejects_duplicate_json_keys_without_modifying_file(self):
        invalid_documents = (
            '{"events": {}, "events": {}}',
            '{"events": {"event-id": 1, "event-id": 2}}',
        )
        for invalid_json in invalid_documents:
            with self.subTest(invalid_json=invalid_json):
                with tempfile.TemporaryDirectory(prefix="nova-duplicate-health-key-") as temp_dir:
                    path = Path(temp_dir) / "health_state.json"
                    path.write_text(invalid_json, encoding="utf-8")

                    with self.assertRaisesRegex(RuntimeError, "duplicate JSON object keys"):
                        load_health_state(path)

                    self.assertEqual(path.read_text(encoding="utf-8"), invalid_json)

    def test_health_state_loader_rejects_non_object_root_without_modifying_file(self):
        for invalid_root in ("[]", "null", '"state"', "17", "true"):
            with self.subTest(invalid_root=invalid_root):
                with tempfile.TemporaryDirectory(prefix="nova-nonobject-health-state-") as temp_dir:
                    path = Path(temp_dir) / "health_state.json"
                    path.write_text(invalid_root, encoding="utf-8")

                    with self.assertRaisesRegex(RuntimeError, "must be a JSON object"):
                        load_health_state(path)

                    self.assertEqual(path.read_text(encoding="utf-8"), invalid_root)

    def test_health_state_loader_rejects_malformed_core_maps_without_modifying_file(self):
        for field in ("targets", "observations", "events", "provider_rotation"):
            for invalid_value in (None, [], "invalid", 7, True):
                with self.subTest(field=field, invalid_value=invalid_value):
                    with tempfile.TemporaryDirectory(prefix="nova-invalid-health-map-") as temp_dir:
                        path = Path(temp_dir) / "health_state.json"
                        state = _state_defaults()
                        state[field] = invalid_value
                        serialized = json.dumps(state)
                        path.write_text(serialized, encoding="utf-8")

                        with self.assertRaisesRegex(RuntimeError, f"field '{field}'"):
                            load_health_state(path)

                        self.assertEqual(path.read_text(encoding="utf-8"), serialized)

    def test_fingerprint_ignores_transport_noise(self):
        left = {"value": 1, "observed_at": "2026-10-07T00:00:00Z", "latency_ms": 100}
        right = {"value": 1, "observed_at": "2026-10-07T01:00:00Z", "latency_ms": 900}
        self.assertEqual(fingerprint(left), fingerprint(right))

    def test_fingerprint_preserves_order_of_json_lists(self):
        first = {"steps": [{"name": "authenticate"}, {"name": "authorize"}]}
        reordered = {"steps": [{"name": "authorize"}, {"name": "authenticate"}]}
        self.assertNotEqual(fingerprint(first), fingerprint(reordered))

    def test_fingerprint_preserves_numeric_precision_in_observations(self):
        first = {"measurement": 1.0000000001}
        slightly_different = {"measurement": 1.0000000002}
        self.assertNotEqual(fingerprint(first), fingerprint(slightly_different))

    def test_unconfigured_probe_does_not_count_as_failure(self):
        state = _state_defaults()
        observation = record_probe(
            state, namespace="gpu-heart", provider="test",
            credential_env="TEST_GPU_API_KEY_01", requested_model=None, actual_model=None,
            api_status=None, authentication="BLOCKED", response_valid=False,
            quality_status="NOT_APPLICABLE", latency_ms=None,
            error_class="credential_not_configured", error_detail="Credential is not configured.",
            max_samples=24, latency_degraded_multiplier=2.0,
            latency_min_samples=4, unacceptable_failure_streak=3,
        )
        self.assertEqual(observation["health_status"], "UNCONFIGURED")
        self.assertEqual(state["targets"]["gpu-heart:test:-"]["failure_streak"], 0)

    def test_latency_degradation_is_detected_after_baseline(self):
        state = _state_defaults()
        kwargs = dict(
            namespace="ai-heart", provider="test", credential_env="TEST_AI_API_KEY_01",
            requested_model="model-a", actual_model="model-a", api_status=200,
            authentication="PASS", response_valid=True, quality_status="PASS",
            error_class=None, error_detail=None, max_samples=24,
            latency_degraded_multiplier=2.0, latency_min_samples=4,
            unacceptable_failure_streak=3,
        )
        for latency in (100, 110, 105, 108):
            record_probe(state, latency_ms=latency, **kwargs)
        observation = record_probe(state, latency_ms=250, **kwargs)
        self.assertEqual(observation["health_status"], "DEGRADED")
        self.assertTrue(observation["latency_degraded"])


    def test_observation_freshness_is_explicit_and_temporal(self):
        now = datetime(2026, 10, 8, 12, 0, tzinfo=timezone.utc)
        observed = (now - timedelta(minutes=30)).isoformat()
        self.assertEqual(
            observation_freshness(observed, fresh_for_seconds=3600, now=now),
            "FRESH",
        )
        self.assertEqual(
            observation_freshness(observed, fresh_for_seconds=1200, now=now),
            "STALE",
        )
        self.assertEqual(
            observation_freshness(observed, fresh_for_seconds=None, now=now),
            "UNSPECIFIED",
        )

    def test_nonfinite_and_boolean_freshness_windows_are_invalid(self):
        now = datetime(2026, 10, 8, 12, 0, tzinfo=timezone.utc)
        observed = "2026-10-08T11:59:00+00:00"
        for ttl in (True, False, float("inf"), float("-inf"), float("nan"), "inf", "nan"):
            with self.subTest(ttl=ttl):
                self.assertEqual(
                    observation_freshness(observed, fresh_for_seconds=ttl, now=now),
                    "INVALID_FRESHNESS_POLICY",
                )

    def test_stale_observation_does_not_reuse_analysis(self):
        state = _state_defaults()
        observed_at = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
        remember_observation(
            state,
            namespace="external-annotation",
            source="source",
            observation={"headline": "A"},
            analysis={"decision": "monitor"},
            fresh_for_seconds=3600,
        )
        state["observations"]["external-annotation:source"]["observed_at"] = observed_at
        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="source",
                current_observation={"headline": "A"},
                now=datetime.now(timezone.utc),
            )
        )

    def test_stale_provider_health_is_not_reported_as_current(self):
        state = _state_defaults()
        old = (datetime.now(timezone.utc) - timedelta(hours=8)).isoformat()
        record_probe(
            state,
            namespace="ai-heart",
            provider="test",
            credential_env="TEST_AI_API_KEY_01",
            requested_model="model-a",
            actual_model="model-a",
            api_status=200,
            authentication="PASS",
            response_valid=True,
            quality_status="PASS",
            latency_ms=100,
            error_class=None,
            error_detail=None,
        )
        target = state["targets"]["ai-heart:test:model-a"]
        target["last_observation"]["observed_at"] = old
        self.assertEqual(
            provider_health_status(
                state,
                provider="test",
                namespace="ai-heart",
                max_observation_age_seconds=6 * 3600,
            ),
            "STALE",
        )

    def test_changed_observation_preserves_prior_analysis(self):
        state = _state_defaults()
        remember_observation(
            state, namespace="external-annotation", source="source",
            observation={"headline": "A"}, analysis={"decision": "monitor"},
        )
        second = remember_observation(
            state, namespace="external-annotation", source="source", observation={"headline": "A"},
        )
        self.assertTrue(second["unchanged_from_previous"])
        self.assertEqual(second["analysis"], {"decision": "monitor"})
        third = remember_observation(
            state, namespace="external-annotation", source="source", observation={"headline": "B"},
        )
        self.assertEqual(third["analysis_history"][-1]["analysis"], {"decision": "monitor"})
        self.assertIsNone(third["analysis"])
        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="source",
                current_observation={"headline": "B"},
            )
        )

    def test_reordered_observation_list_invalidates_reusable_analysis(self):
        state = _state_defaults()
        first = {"steps": ["authenticate", "authorize"]}
        second = {"steps": ["authorize", "authenticate"]}
        remember_observation(
            state,
            namespace="external-annotation",
            source="ordered-source",
            observation=first,
            analysis={"decision": "first order"},
        )
        changed = remember_observation(
            state,
            namespace="external-annotation",
            source="ordered-source",
            observation=second,
        )
        self.assertFalse(changed["unchanged_from_previous"])
        self.assertEqual(changed["observation"]["steps"], second["steps"])
        self.assertIsNone(changed["analysis"])
        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="ordered-source",
                current_observation=second,
            )
        )

    def test_reusable_analysis_requires_same_fingerprint(self):
        state = _state_defaults()
        observation = {"headline": "A"}
        remember_observation(
            state, namespace="external-annotation", source="source",
            observation=observation, analysis={"decision": "monitor"}, valid_for_seconds=3600,
        )
        analysis_timestamp = state["observations"]["external-annotation:source"]["analysis_observed_at"]
        second = remember_observation(
            state, namespace="external-annotation", source="source",
            observation=observation, valid_for_seconds=3600,
        )
        self.assertEqual(second["analysis_fingerprint"], second["fingerprint"])
        self.assertEqual(second["analysis_observed_at"], analysis_timestamp)
        reused = reusable_analysis(
            state, namespace="external-annotation", source="source",
            current_observation=observation, now=datetime.now(timezone.utc),
        )
        self.assertEqual(reused, {"decision": "monitor"})
        self.assertIsNone(
            reusable_analysis(
                state, namespace="external-annotation", source="source",
                current_observation={"headline": "B"},
            )
        )



    def test_reusable_analysis_rejects_missing_or_mismatched_analysis_fingerprint(self):
        state = _state_defaults()
        observation = {"headline": "A"}
        remember_observation(
            state,
            namespace="external-annotation",
            source="source",
            observation=observation,
            analysis={"decision": "review"},
        )
        record = state["observations"]["external-annotation:source"]

        record["analysis_fingerprint"] = "other-fingerprint"
        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="source",
                current_observation=observation,
            )
        )
        record.pop("analysis_fingerprint")
        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="source",
                current_observation=observation,
            )
        )

    def test_analysis_ttl_uses_analysis_timestamp_not_last_seen_timestamp(self):
        state = _state_defaults()
        observation = {"headline": "A"}
        record = remember_observation(
            state,
            namespace="external-annotation",
            source="source",
            observation=observation,
            analysis={"decision": "review"},
            valid_for_seconds=60,
        )
        now = datetime(2026, 10, 29, 12, 0, tzinfo=timezone.utc)
        record["observed_at"] = now.isoformat()
        record["analysis_observed_at"] = (now - timedelta(seconds=120)).isoformat()

        self.assertIsNone(
            reusable_analysis(
                state,
                namespace="external-annotation",
                source="source",
                current_observation=observation,
                now=now,
            )
        )

    def test_reusable_analysis_rejects_untrusted_timestamp_without_freshness_ttl(self):
        now = datetime.now(timezone.utc)
        invalid_timestamps = (
            "not-a-timestamp",
            (now + timedelta(minutes=5)).isoformat(),
        )
        for observed_at in invalid_timestamps:
            with self.subTest(observed_at=observed_at):
                state = _state_defaults()
                observation = {"headline": "A"}
                remember_observation(
                    state,
                    namespace="external-annotation",
                    source="timestamp-check",
                    observation=observation,
                    analysis={"decision": "monitor"},
                )
                state["observations"]["external-annotation:timestamp-check"]["observed_at"] = observed_at
                self.assertIsNone(
                    reusable_analysis(
                        state,
                        namespace="external-annotation",
                        source="timestamp-check",
                        current_observation=observation,
                        now=now,
                    )
                )

    def test_health_persistence_drops_non_allowlisted_response_headers(self):
        state = _state_defaults()
        record_probe(
            state,
            namespace="ai-heart",
            provider="test",
            credential_env="TEST_API_KEY",
            requested_model="model-a",
            actual_model="model-a",
            api_status=200,
            authentication="PASS",
            response_valid=True,
            quality_status="PASS",
            latency_ms=100,
            error_class=None,
            error_detail=None,
            response_headers={
                "Authorization": "Bearer secret-value",
                "Set-Cookie": "session=secret-value",
                "X-RateLimit-Remaining-Req-Minute": "0",
                "Content-Type": "application/json",
            },
        )
        observation = state["targets"]["ai-heart:test:model-a"]["last_observation"]
        self.assertEqual(
            observation["response_headers"],
            {"x-ratelimit-remaining-req-minute": "0"},
        )
        self.assertNotIn("Authorization", json.dumps(state))
        self.assertNotIn("Set-Cookie", json.dumps(state))
        self.assertNotIn("secret-value", json.dumps(state))

    def test_allowlisted_response_headers_are_persisted_in_health_history(self):
        state = _state_defaults()
        response_headers = {
            "mistral-correlation-id": "corr-test-123",
            "x-ratelimit-limit-req-minute": "4",
            "x-ratelimit-remaining-req-minute": "0",
        }
        observation = record_probe(
            state,
            namespace="ai-heart",
            provider="mistral",
            credential_env="TEST_MISTRAL_KEY",
            requested_model="mistral-small-latest",
            actual_model=None,
            api_status=429,
            authentication="UNKNOWN",
            response_valid=False,
            quality_status="NOT_APPLICABLE",
            latency_ms=100,
            error_class="transient",
            error_detail='{"code":"1300","type":"rate_limited"}',
            response_headers=response_headers,
        )
        target = state["targets"]["ai-heart:mistral:mistral-small-latest"]
        self.assertEqual(observation["response_headers"], response_headers)
        self.assertEqual(target["last_observation"]["response_headers"], response_headers)
        self.assertEqual(target["history"][-1]["response_headers"], response_headers)

if __name__ == "__main__":
    unittest.main()
