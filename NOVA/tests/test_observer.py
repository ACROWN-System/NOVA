import json
import unittest
import urllib.error
from io import BytesIO
from unittest.mock import MagicMock, patch

from NOVA.operational_observer import fetch_text, normalize_content, observe_source


class ObserverTests(unittest.TestCase):
    def test_normalize_content_removes_html_noise(self):
        content = "<html><script>bad()</script><body>Hello   NOVA</body></html>"
        self.assertEqual(normalize_content(content), "Hello NOVA")

    def test_http_error_body_is_not_returned_as_source_content(self):
        error = urllib.error.HTTPError(
            "https://example.invalid/annotation",
            429,
            "Too Many Requests",
            {},
            BytesIO(b'{"message":"do not retain this error body"}'),
        )
        with patch("NOVA.operational_observer.urllib.request.urlopen", side_effect=error):
            status, raw, detail = fetch_text("https://example.invalid/annotation", 1024, 5)

        self.assertEqual(status, 429)
        self.assertEqual(raw, "")
        self.assertEqual(detail, "HTTP 429")

    def test_oversized_successful_response_is_not_fingerprinted_as_complete(self):
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = 200
        response.read.return_value = b"12345678901"
        with patch("NOVA.operational_observer.urllib.request.urlopen", return_value=response):
            status, raw, detail = fetch_text("https://example.invalid/annotation", 10, 5)

        self.assertEqual(status, 200)
        self.assertEqual(raw, "")
        self.assertIn("max_bytes", detail)

    def test_failed_fetch_preserves_previous_successful_observation(self):
        state = {
            "observations": {
                "external-annotation:release-notes": {
                    "fingerprint": "previous-fingerprint",
                    "analysis": {"decision": "reviewed"},
                    "observation": {"content_excerpt": "previous successful content"},
                }
            },
            "events": {"previous-event": {"analysis_status": "ANALYZED"}},
        }
        before = json.dumps(state, sort_keys=True)
        source = {"name": "release-notes", "url": "https://example.invalid/annotation"}
        with patch(
            "NOVA.operational_observer.fetch_text",
            return_value=(429, '{"message":"sensitive error body"}', "HTTP 429"),
        ):
            result = observe_source(source, state, timeout=5, max_bytes=1024)

        self.assertEqual(result["status"], "ERROR")
        self.assertEqual(result["http_status"], 429)
        self.assertNotIn("sensitive error body", json.dumps(result))
        self.assertEqual(json.dumps(state, sort_keys=True), before)


if __name__ == "__main__":
    unittest.main()
