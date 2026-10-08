import os
import unittest
from unittest.mock import patch

from NOVA.health import _state_defaults
from NOVA.router import (
    advance_scheduled_probe_rotation,
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
        ]
        self.state = _state_defaults()

    def test_scheduled_provider_is_first_even_when_degraded(self):
        self.state["provider_rotation"]["ai-heart"]["next_index"] = 1
        self.state["targets"]["ai-heart:gemini:model"] = {"health_status": "UNACCEPTABLE"}
        self.state["targets"]["ai-heart:groq:model"] = {"health_status": "DEGRADED"}

        ordered = scheduled_probe_provider_order(self.providers, self.state)

        self.assertEqual(
            [item["name"] for item in ordered],
            ["gemini", "cerebras", "mistral", "groq"],
        )

    def test_rotation_advances_across_multiple_manual_runs(self):
        rotation = self.state["provider_rotation"]["ai-heart"]

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            expected = ["groq", "gemini", "cerebras", "mistral"]
            for name in expected[:-1]:
                ordered = scheduled_probe_provider_order(self.providers, self.state)
                self.assertEqual(ordered[0]["name"], name)
                advance_scheduled_probe_rotation(self.state, self.providers, ordered[0])

            ordered = scheduled_probe_provider_order(self.providers, self.state)
            self.assertEqual(ordered[0]["name"], "mistral")
            advance_scheduled_probe_rotation(self.state, self.providers, ordered[0])
            self.assertEqual(rotation["next_provider"], "groq")
            self.assertEqual(rotation["next_index"], 0)

    def test_rotation_skips_provider_removed_from_active_roster(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_provider"] = "groq"

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            scheduled = scheduled_probe_provider_order(self.providers, self.state)[0]
            self.assertEqual(scheduled["name"], "groq")

            self.providers[1]["status"] = "down"
            advance_scheduled_probe_rotation(self.state, self.providers, scheduled)

        self.assertEqual(rotation["next_provider"], "cerebras")
        self.assertEqual(rotation["next_index"], 1)

    def test_legacy_index_state_remains_supported(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_index"] = 2
        rotation["next_provider"] = None

        ordered = scheduled_probe_provider_order(self.providers, self.state)

        self.assertEqual(ordered[0]["name"], "cerebras")


if __name__ == "__main__":
    unittest.main()
