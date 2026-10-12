import json
import unittest
from email.message import Message
from unittest.mock import patch

from NOVA.provider_qualification import classify, safe_headers, build_report, probe, openai_text


class ProviderQualificationTests(unittest.TestCase):
    def test_payment_and_quota_errors_are_distinct(self):
        expected = {
            302: "REDIRECT_BLOCKED",
            401: "AUTH_REJECTED",
            402: "PAYMENT_REQUIRED_OR_CREDITS_EXHAUSTED",
            403: "ACCESS_DENIED_OR_POLICY",
            404: "ENDPOINT_OR_MODEL_NOT_FOUND",
            429: "RATE_LIMITED_OR_QUOTA_EXHAUSTED",
            503: "PROVIDER_SERVER_ERROR",
        }
        for code, status in expected.items():
            with self.subTest(code=code):
                self.assertEqual(classify(code), status)

    def test_only_allowlisted_rate_limit_headers_are_reported(self):
        headers = Message()
        headers["x-ratelimit-remaining"] = "15"
        headers["x-ratelimit-remaining-req-minute"] = "0"
        headers["retry-after"] = "2"
        headers["set-cookie"] = "not-for-report"
        headers["x-debug-info"] = "not-for-report"
        self.assertEqual(safe_headers(headers), {
            "x-ratelimit-remaining": "15",
            "x-ratelimit-remaining-req-minute": "0",
            "retry-after": "2",
        })


    def test_successful_http_with_missing_marker_is_not_mislabelled_as_auth_failure(self):
        class FakeResponse:
            status = 200
            headers = {"x-ratelimit-remaining": "7"}

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def read(self, size):
                return json.dumps({
                    "choices": [{"message": {"content": "ordinary response"}}],
                    "usage": {"prompt_tokens": 3, "completion_tokens": 4, "total_tokens": 7},
                }).encode("utf-8")

        with patch("NOVA.provider_qualification.urllib.request.build_opener") as opener:
            opener.return_value.open.return_value = FakeResponse()
            result = probe(
                "fixture", "llm_inference", "FIXTURE_KEY", "configured-value",
                "https://provider.invalid/v1/chat/completions", "POST",
                {"Authorization": "Bearer configured-value"}, b"{}", openai_text,
            )
        self.assertEqual(result["http_status"], 200)
        self.assertEqual(result["status"], "RESPONSE_VALID_MARKER_MISSING")
        self.assertTrue(result["response_shape_valid"])
        self.assertFalse(result["probe_marker_present"])
        self.assertNotIn("ordinary response", json.dumps(result))
        self.assertEqual(result["usage"]["total_tokens"], 7)

    def test_empty_configuration_skips_all_endpoints(self):
        with patch("NOVA.provider_qualification.urllib.request.build_opener") as opener:
            report = build_report({})
        opener.assert_not_called()
        self.assertTrue(all(
            row["status"].startswith("SKIPPED")
            for row in report["results"]
        ))
        self.assertTrue(report["diagnostic_only"])
        self.assertFalse(report["production_roster_mutated"])
        self.assertFalse(report["secret_values_exposed"])

    def test_github_credential_is_not_labelled_as_inference_capacity(self):
        def fake_probe(name, kind, env_name, credential, *args):
            return {
                "provider": name,
                "provider_type": kind,
                "credential_env": env_name,
                "credential_configured": bool(credential),
                "status": "SKIPPED_MISSING_CREDENTIAL" if not credential else "PASS",
                "http_status": None,
                "latency_ms": None,
                "rate_limit_headers": {},
                "usage": {},
            }

        with patch("NOVA.provider_qualification.probe", side_effect=fake_probe):
            report = build_report({"GitHub_Token": "example-value"})
        github = next(row for row in report["results"] if row["provider"] == "github_api")
        self.assertEqual(github["provider_type"], "repository_management_not_inference")
        self.assertNotIn("example-value", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
