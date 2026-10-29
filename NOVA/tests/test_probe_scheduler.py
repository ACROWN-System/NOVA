import unittest
from datetime import datetime, timezone

from NOVA.health import _state_defaults
from NOVA.capacity import provider_capacity_opportunity
from NOVA.probe_scheduler import (
    reschedule_after_probes,
    select_probe_candidate,
)


def providers():
    return [
        {"name": "A", "status": "active"},
        {"name": "B", "status": "active"},
        {"name": "C", "status": "active"},
        {"name": "D", "status": "active"},
    ]


class RollingProbeSchedulerTests(unittest.TestCase):
    def test_expiring_provider_is_pulled_forward_and_checked_provider_moves_to_end(self):
        state = _state_defaults()
        roster = providers()

        # The normal ring has just completed D at 18:00, so the next cycle is
        # A 00:00, B 06:00, C 12:00, D 18:00.
        reschedule_after_probes(
            state,
            roster,
            ["D"],
            completed_at=datetime(2026, 10, 8, 18, 0, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )

        state["targets"]["ai-heart:C:model"] = {
            "health_status": "HEALTHY",
            "last_capacity": {
                "provider": "C",
                "observed_at": "2026-10-08T20:50:00+00:00",
                "expiration_at": "2026-10-08T21:00:00+00:00",
                "metrics": {},
                "resources": {
                    "credits": {
                        "remaining": 100,
                        "total": 100,
                        "unit": "credits",
                        "measurement_type": "TOTAL_RESOURCE",
                    }
                },
                "call_allowances": {},
            },
        }

        decision = select_probe_candidate(
            roster,
            state,
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
        )

        self.assertEqual(decision["provider"], "C")
        self.assertEqual(decision["reason"], "EXPIRY_REALLOCATION")
        self.assertTrue(decision["preempted"])

        # C is completed at 21:00. The rolling ring becomes C 21:00 -> A 03:00
        # -> B 09:00 -> D 15:00 -> C 21:00.
        reschedule_after_probes(
            state,
            roster,
            ["C"],
            completed_at=datetime(2026, 10, 8, 21, 0, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )

        schedule = state["provider_rotation"]["ai-heart"]["probe_schedule"]
        queue = state["provider_rotation"]["ai-heart"]["probe_queue"]
        self.assertEqual(queue, ["A", "B", "D", "C"])
        self.assertEqual(schedule["A"], "2026-10-09T03:00:00+00:00")
        self.assertEqual(schedule["B"], "2026-10-09T09:00:00+00:00")
        self.assertEqual(schedule["D"], "2026-10-09T15:00:00+00:00")
        self.assertEqual(schedule["C"], "2026-10-09T21:00:00+00:00")

    def test_expiry_does_not_preempt_when_normal_check_is_before_expiration(self):
        state = _state_defaults()
        roster = providers()
        reschedule_after_probes(
            state,
            roster,
            ["D"],
            completed_at=datetime(2026, 10, 8, 18, 0, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )
        state["targets"]["ai-heart:C:model"] = {
            "health_status": "HEALTHY",
            "last_capacity": {
                "provider": "C",
                "observed_at": "2026-10-08T20:50:00+00:00",
                "expiration_at": "2026-10-09T13:00:00+00:00",
                "metrics": {},
                "resources": {
                    "credits": {
                        "remaining": 100,
                        "total": 100,
                        "measurement_type": "TOTAL_RESOURCE",
                    }
                },
            },
        }

        decision = select_probe_candidate(
            roster,
            state,
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
        )

        self.assertEqual(decision["provider"], "A")
        self.assertEqual(decision["reason"], "SCHEDULED_PENDING")
        self.assertFalse(decision["preempted"])

    def test_duplicate_active_provider_identities_block_ambiguous_schedule(self):
        state = _state_defaults()
        roster = [
            {"name": "A", "status": "active"},
            {"name": "a", "status": "active"},
            {"name": "B", "status": "active"},
        ]

        decision = select_probe_candidate(
            roster,
            state,
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
        )
        rotation = state["provider_rotation"]["ai-heart"]

        self.assertIsNone(decision["provider"])
        self.assertEqual(decision["reason"], "BLOCKED_DUPLICATE_PROVIDER_IDENTITIES")
        self.assertEqual(rotation["schedule_status"], "BLOCKED_DUPLICATE_PROVIDER_IDENTITIES")
        self.assertEqual(rotation["probe_queue"], [])
        self.assertEqual(rotation["probe_schedule"], {})
        self.assertEqual(rotation["duplicate_provider_names"], ["A", "a"])

        # Rescheduling must not reconstruct a duplicated queue.
        after = reschedule_after_probes(
            state,
            roster,
            ["A"],
            completed_at=datetime(2026, 10, 8, 21, 0, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )
        self.assertEqual(after["probe_queue"], [])
        self.assertEqual(after["probe_schedule"], {})
        self.assertEqual(after["schedule_status"], "BLOCKED_DUPLICATE_PROVIDER_IDENTITIES")

    def test_empty_roster_is_reported_as_no_active_providers(self):
        state = _state_defaults()
        decision = select_probe_candidate(
            [],
            state,
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
        )
        self.assertIsNone(decision["provider"])
        self.assertEqual(decision["reason"], "NO_ACTIVE_PROVIDERS")

    def test_active_provider_without_name_blocks_probe_schedule(self):
        state = _state_defaults()
        roster = [
            {"status": "active"},
            {"name": "A", "status": "active"},
        ]
        decision = select_probe_candidate(
            roster,
            state,
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
        )
        rotation = state["provider_rotation"]["ai-heart"]
        self.assertIsNone(decision["provider"])
        self.assertEqual(decision["reason"], "BLOCKED_INVALID_PROVIDER_IDENTITIES")
        self.assertEqual(rotation["probe_queue"], [])
        self.assertEqual(rotation["invalid_active_provider_count"], 1)

    def test_skips_move_to_end_without_being_recorded_as_probes(self):
        state = _state_defaults()
        roster = providers()
        rotation = state["provider_rotation"]["ai-heart"]
        rotation["last_selection_decision"] = {
            "provider": "A",
            "reason": "SCHEDULED_DUE",
        }

        result = reschedule_after_probes(
            state,
            roster,
            ["B"],
            skipped_provider_names=["A"],
            completed_at=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )

        self.assertEqual(result["probe_queue"], ["C", "D", "A", "B"])
        self.assertEqual(result["last_probe_providers"], ["B"])
        self.assertEqual(result["last_skipped_providers"], ["A"])
        self.assertEqual(result["last_selection_reason"], "SCHEDULED_DUE")
        self.assertEqual(result["last_schedule_reason"], "ROLLING_INTERVAL")

    def test_expiry_reallocation_reason_requires_selected_provider_to_be_attempted(self):
        state = _state_defaults()
        roster = providers()
        rotation = state["provider_rotation"]["ai-heart"]
        rotation["last_selection_decision"] = {
            "provider": "C",
            "reason": "EXPIRY_REALLOCATION",
        }

        result = reschedule_after_probes(
            state,
            roster,
            ["B"],
            skipped_provider_names=["C"],
            completed_at=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )
        self.assertEqual(result["last_schedule_reason"], "EXPIRY_PREEMPTION_SKIPPED")
        self.assertEqual(result["last_probe_providers"], ["B"])
        self.assertEqual(result["last_skipped_providers"], ["C"])

    def test_no_network_attempt_is_not_reported_as_a_completed_probe(self):
        state = _state_defaults()
        roster = providers()
        result = reschedule_after_probes(
            state,
            roster,
            [],
            skipped_provider_names=["A", "B", "C", "D"],
            completed_at=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
            interval_seconds=6 * 3600,
        )
        self.assertEqual(result["last_probe_providers"], [])
        self.assertEqual(result["last_skipped_providers"], ["A", "B", "C", "D"])
        self.assertEqual(result["last_schedule_reason"], "SKIPPED_NO_NETWORK_ATTEMPT")

    def test_required_health_work_can_reuse_expiring_total_resource_without_inventing_cash_value(self):
        targets = {
            "ai-heart:C:model": {
                "last_capacity": {
                    "provider": "C",
                    "observed_at": "2026-10-08T20:50:00+00:00",
                    "expiration_at": "2026-10-08T21:00:00+00:00",
                    "metrics": {},
                    "resources": {
                        "credits": {
                            "remaining": 100,
                            "total": 100,
                            "measurement_type": "TOTAL_RESOURCE",
                        }
                    },
                }
            }
        }
        opportunity = provider_capacity_opportunity(
            targets,
            provider="C",
            namespace="ai-heart",
            now=datetime(2026, 10, 8, 20, 55, tzinfo=timezone.utc),
            allow_required_work_reuse=True,
        )

        self.assertEqual(opportunity["state"], "EXPIRING_SOON")
        self.assertEqual(
            opportunity["economic_signal"]["state"],
            "REQUIRED_WORK_EXPIRY_REUSE",
        )
        self.assertGreater(opportunity["priority"], 1.0)
        self.assertEqual(opportunity["dimension"], "TOTAL_RESOURCE")


if __name__ == "__main__":
    unittest.main()
