import os
import unittest
from email.message import Message
from io import BytesIO
import urllib.error
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from NOVA.health import _state_defaults
from NOVA.router import (
    advance_scheduled_probe_rotation,
    call_openai_compatible,
    classify_http_error,
    diagnostic_http_headers,
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

    def test_order_providers_accepts_task_context_without_live_credentials(self):
        ordered = health_order_providers(
            self.providers[:2],
            self.state,
            max_observation_age_seconds=6 * 3600,
        )
        self.assertEqual(len(ordered), 2)

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


    def test_http_error_preserves_original_body_and_classifies_case_insensitively(self):
        headers = Message()
        error = urllib.error.HTTPError(
            "https://api.mistral.ai/v1/chat/completions",
            429,
            "Too Many Requests",
            headers,
            BytesIO(b'{"message":"Rate Limit Exceeded","type":"rate_limited","code":"1300"}'),
        )

        signal, body = classify_http_error(error)

        self.assertEqual(signal, "transient")
        self.assertIn("Rate Limit Exceeded", body)

    def test_diagnostic_http_headers_are_allowlisted_and_case_insensitive(self):
        headers = Message()
        headers["Retry-After"] = "12"
        headers["X-RateLimit-Remaining-Requests"] = "0"
        headers["X-Request-Id"] = "req-123"
        headers["Authorization"] = "Bearer DO_NOT_LOG"

        diagnostic = diagnostic_http_headers(headers)

        self.assertEqual(diagnostic["retry-after"], "12")
        self.assertEqual(diagnostic["x-ratelimit-remaining-requests"], "0")
        self.assertEqual(diagnostic["x-request-id"], "req-123")
        self.assertNotIn("authorization", diagnostic)
        self.assertNotIn("DO_NOT_LOG", repr(diagnostic))

    def test_mistral_429_probe_records_rate_limit_headers_without_secrets(self):
        headers = Message()
        headers["Retry-After"] = "12"
        headers["X-RateLimit-Limit-Requests"] = "1"
        headers["X-RateLimit-Remaining-Requests"] = "0"
        headers["X-Request-Id"] = "mistral-request-123"
        headers["Authorization"] = "Bearer DO_NOT_LOG"
        error = urllib.error.HTTPError(
            "https://api.mistral.ai/v1/chat/completions",
            429,
            "Too Many Requests",
            headers,
            BytesIO(b'{"message":"rate limit exceeded","type":"rate_limited","code":"1300"}'),
        )
        mistral = {
            "name": "mistral",
            "api_key_env": "TEST_MISTRAL_KEY",
            "base_url": "https://api.mistral.ai/v1/chat/completions",
            "models": ["mistral-small-latest"],
        }

        with patch.dict(os.environ, {"TEST_MISTRAL_KEY": "test-key"}):
            with patch("NOVA.router.urllib.request.urlopen", side_effect=error):
                _, _, probes = call_openai_compatible(mistral, "test prompt")

        probe = probes[0]
        self.assertEqual(probe["api_status"], 429)
        self.assertIn('"code":"1300"', probe["error_detail"])
        self.assertEqual(probe["response_headers"]["retry-after"], "12")
        self.assertEqual(
            probe["response_headers"]["x-ratelimit-remaining-requests"], "0"
        )
        self.assertNotIn("authorization", probe["response_headers"])
        self.assertNotIn("test-key", repr(probe))
        self.assertEqual(probe["capacity"]["metrics"]["requests"]["remaining"], 0)

if __name__ == "__main__":
    unittest.main()
