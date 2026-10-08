import os
import unittest
from unittest.mock import patch

from NOVA.health import _state_defaults
from NOVA.router import (
    advance_scheduled_probe_rotation,
    scheduled_probe_provider_order,
)


def provider(name: str) -> dict:
    return {"name": name}


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

    def test_manual_run_advances_provider_rotation(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_index"] = 2

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            advance_scheduled_probe_rotation(self.state, self.providers, self.providers[2])

        self.assertEqual(rotation["next_index"], 3)
        self.assertEqual(rotation["last_scheduled_provider"], "cerebras")
        self.assertIsNotNone(rotation["last_scheduled_at"])

    def test_scheduled_run_advances_after_probe(self):
        rotation = self.state["provider_rotation"]["ai-heart"]
        rotation["next_index"] = 2

        with patch.dict(os.environ, {"NOVA_ADVANCE_PROVIDER_ROTATION": "true"}):
            advance_scheduled_probe_rotation(self.state, self.providers, self.providers[2])

        self.assertEqual(rotation["next_index"], 3)
        self.assertEqual(rotation["last_scheduled_provider"], "cerebras")
        self.assertIsNotNone(rotation["last_scheduled_at"])


if __name__ == "__main__":
    unittest.main()
