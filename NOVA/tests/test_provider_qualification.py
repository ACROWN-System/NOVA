import json
import unittest
from email.message import Message
from unittest.mock import patch

from NOVA.provider_qualification import classify, safe_headers, build_report


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
        headers["retry-after"] = "2"
        headers["set-cookie"] = "not-for-report"
        headers["x-debug-info"] = "not-for-report"
        self.assertEqual(safe_headers(headers), {
            "x-ratelimit-remaining": "15",
            "retry-after": "2",
        })

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
