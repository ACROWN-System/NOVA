import unittest
from datetime import datetime, timezone

from NOVA.health import _state_defaults, fingerprint, record_probe, remember_observation, reusable_analysis


class HealthTests(unittest.TestCase):
    def test_fingerprint_ignores_transport_noise(self):
        left = {"value": 1, "observed_at": "2026-10-07T00:00:00Z", "latency_ms": 100}
        right = {"value": 1, "observed_at": "2026-10-07T01:00:00Z", "latency_ms": 900}
        self.assertEqual(fingerprint(left), fingerprint(right))

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

    def test_reusable_analysis_requires_same_fingerprint(self):
        state = _state_defaults()
        observation = {"headline": "A"}
        remember_observation(
            state, namespace="external-annotation", source="source",
            observation=observation, analysis={"decision": "monitor"}, valid_for_seconds=3600,
        )
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


if __name__ == "__main__":
    unittest.main()
