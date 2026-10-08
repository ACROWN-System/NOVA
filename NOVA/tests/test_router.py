import os
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from NOVA.health import _state_defaults
from NOVA.router import (
    advance_scheduled_probe_rotation,
    health_order_providers,
    scheduled_probe_provider_order,
)


def provider(name: str, status: str = "active") -> dict:
    return {"name": name, "status": status}


class RouterRotationTests(unittest.TestCase):
    def setUp(self):
        self.providers = [
            provider("groq"),
            provider("gemini"),
            provider("cerebras"),
            provider("mistral"),
            provider("cloudflare"),
        ]
        self.state = _state_defaults()

    def test_stale_provider_is_deprioritized_when_age_boundary_is_enabled(self):
        old = (datetime.now(timezone.utc) - timedelta(hours=8)).isoformat()
        self.state["targets"]["ai-heart:groq:model"] = {
            "health_status": "HEALTHY",
            "last_observation": {"observed_at": old},
        }

        ordered = health_order_providers(
            self.providers[:2],
            self.state,
            max_observation_age_seconds=6 * 3600,
        )

        self.assertEqual([item["name"] for item in ordered], ["gemini", "groq"])

    def test_scheduled_provider_is_first_even_when_degraded(self):
        self.state["provider_rotation"]["ai-heart"]["next_index"] = 1
        self.state["targets"]["ai-heart:gemini:model"] = {"health_status": "UNACCEPTABLE"}
        self.state["targets"]["ai-heart:groq:model"] = {"health_status": "DEGRADED"}

        ordered = scheduled_probe_provider_order(self.providers, self.state)

        self.assertEqual(
            [item["name"] for item in ordered],
            ["gemini", "cerebras", "mistral", "cloudflare", "groq"],
        )

    def test_rotation_advances_to_next_unprobed_provider(self):
        rotation = self.state["provider_rotation"]["ai-heart"]

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            scheduled = scheduled_probe_provider_order(self.providers, self.state)[0]
            self.assertEqual(scheduled["name"], "groq")

            probed = ["groq", "cerebras", "cloudflare", "gemini"]
            advance_scheduled_probe_rotation(
                self.state, self.providers, scheduled, probed
            )

        self.assertEqual(rotation["next_provider"], "mistral")
        self.assertEqual(rotation["next_index"], 3)
        self.assertEqual(rotation["last_probe_providers"], probed)

    def test_rotation_continues_without_retesting_previous_heartbeat_probes(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_provider"] = "mistral"
        rotation["last_probe_providers"] = ["groq", "cerebras", "cloudflare", "gemini"]

        ordered = scheduled_probe_provider_order(self.providers, self.state)
        self.assertEqual(ordered[0]["name"], "mistral")

    def test_rotation_falls_back_to_next_active_after_scheduled_provider_is_down(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_provider"] = "mistral"
        self.providers[4]["status"] = "down"

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            scheduled = scheduled_probe_provider_order(self.providers, self.state)[0]
            self.assertEqual(scheduled["name"], "mistral")

            self.providers[0]["status"] = "down"
            advance_scheduled_probe_rotation(
                self.state, self.providers, scheduled, ["mistral"]
            )

        self.assertEqual(rotation["next_provider"], "gemini")
        self.assertEqual(rotation["next_index"], 0)

    def test_legacy_index_state_remains_supported(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_index"] = 2
        rotation["next_provider"] = None

        ordered = scheduled_probe_provider_order(self.providers, self.state)

        self.assertEqual(ordered[0]["name"], "cerebras")


if __name__ == "__main__":
    unittest.main()
