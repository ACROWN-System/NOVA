import unittest
from datetime import datetime, timedelta, timezone

from NOVA.capacity import capacity_opportunity, extract_rate_limit_snapshot
from NOVA.health import _state_defaults, record_probe


class CapacityMemoryTests(unittest.TestCase):
    def test_groq_headers_are_extracted_with_remaining_and_reset(self):
        snapshot = extract_rate_limit_snapshot(
            "groq",
            {
                "x-ratelimit-limit-requests": "1000",
                "x-ratelimit-remaining-requests": "997",
                "x-ratelimit-reset-requests": "2m",
                "x-ratelimit-limit-tokens": "8000",
                "x-ratelimit-remaining-tokens": "7936",
                "x-ratelimit-reset-tokens": "7.5s",
            },
            observed_at="2026-10-08T00:00:00+00:00",
        )
        self.assertEqual(snapshot["measurement_state"], "OBSERVED")
        self.assertEqual(snapshot["metrics"]["requests"]["remaining"], 997)
        self.assertEqual(snapshot["metrics"]["tokens"]["remaining"], 7936)
        self.assertEqual(
            snapshot["estimated_next_reset_at"]["requests"],
            "2026-10-08T00:02:00+00:00",
        )


    def test_expiring_capacity_is_marked_as_actionable(self):
        now = datetime(2026, 10, 8, 12, 0, tzinfo=timezone.utc)
        snapshot = {
            "provider": "groq",
            "observed_at": now.isoformat(),
            "estimated_next_reset_at": {
                "requests": (now + timedelta(minutes=5)).isoformat()
            },
            "metrics": {
                "requests": {"limit": 100, "remaining": 80}
            },
        }
        opportunity = capacity_opportunity(
            snapshot,
            now=now,
            urgency_window_seconds=300,
            minimum_remaining_reserve_fraction=0.2,
            max_observation_age_seconds=900,
        )
        self.assertEqual(opportunity["state"], "EXPIRING_SOON")
        self.assertGreater(opportunity["priority"], 1.0)

    def test_expiring_capacity_below_protected_reserve_is_not_burned(self):
        now = datetime(2026, 10, 8, 12, 0, tzinfo=timezone.utc)
        snapshot = {
            "provider": "groq",
            "observed_at": now.isoformat(),
            "estimated_next_reset_at": {
                "requests": (now + timedelta(minutes=2)).isoformat()
            },
            "metrics": {
                "requests": {"limit": 100, "remaining": 10}
            },
        }
        opportunity = capacity_opportunity(
            snapshot,
            now=now,
            urgency_window_seconds=300,
            minimum_remaining_reserve_fraction=0.2,
        )
        self.assertEqual(opportunity["state"], "PROTECTED_RESERVE")
        self.assertEqual(opportunity["priority"], 0.0)

    def test_missing_capacity_is_not_invented(self):
        snapshot = extract_rate_limit_snapshot("mistral", {})
        self.assertEqual(snapshot["measurement_state"], "NOT_EXPOSED")
        self.assertEqual(snapshot["metrics"], {})

    def test_capacity_is_persisted_in_target_and_history(self):
        state = _state_defaults()
        capacity = {
            "provider": "groq",
            "measurement_state": "OBSERVED",
            "metrics": {
                "requests": {"remaining": 997, "limit": 1000}
            },
        }
        observation = record_probe(
            state,
            namespace="ai-heart",
            provider="groq",
            credential_env="GROQ_API_KEY_01",
            requested_model="openai/gpt-oss-20b",
            actual_model="openai/gpt-oss-20b",
            api_status=200,
            authentication="PASS",
            response_valid=True,
            quality_status="PASS",
            latency_ms=100,
            error_class=None,
            error_detail=None,
            capacity=capacity,
        )
        self.assertEqual(observation["capacity"], capacity)
        target = state["targets"]["ai-heart:groq:openai/gpt-oss-20b"]
        self.assertEqual(target["last_capacity"], capacity)
        self.assertEqual(target["history"][-1]["capacity"], capacity)


if __name__ == "__main__":
    unittest.main()
