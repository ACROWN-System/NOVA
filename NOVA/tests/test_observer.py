import json
import tempfile
import unittest
import urllib.error
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

from NOVA.operational_observer import (
    fetch_text,
    normalize_content,
    observe_source,
    run,
    validate_watchlist,
)


class ObserverTests(unittest.TestCase):
    def test_watchlist_rejects_duplicate_normalized_source_names(self):
        watchlist = {
            "sources": [
                {"name": "release-notes", "url": "https://example.invalid/a"},
                {"name": " RELEASE-NOTES ", "url": "https://example.invalid/b"},
            ]
        }
        with self.assertRaisesRegex(RuntimeError, "duplicate source identities"):
            validate_watchlist(watchlist)

    def test_watchlist_rejects_duplicate_urls_even_when_names_differ(self):
        watchlist = {
            "sources": [
                {"name": "source-a", "url": "HTTPS://EXAMPLE.INVALID/updates"},
                {"name": "source-b", "url": "https://example.invalid/updates"},
            ]
        }
        with self.assertRaisesRegex(RuntimeError, "duplicate source URLs"):
            validate_watchlist(watchlist)

    def test_watchlist_rejects_malformed_source_structure(self):
        invalid_watchlists = (
            ({"sources": {}}, "must contain a sources array"),
            ({"sources": ["not-an-object"]}, "must be a JSON object"),
            ({"sources": [{"name": "release-notes", "url": "relative/path"}]}, "URL must be absolute"),
            ({"sources": [{"name": 12, "url": "https://example.invalid/updates"}]}, "name must be a string"),
        )
        for watchlist, expected_error in invalid_watchlists:
            with self.subTest(watchlist=watchlist):
                with self.assertRaisesRegex(RuntimeError, expected_error):
                    validate_watchlist(watchlist)

    def test_run_rejects_ambiguous_watchlist_before_state_load_or_fetch(self):
        with tempfile.TemporaryDirectory(prefix="nova-ambiguous-watchlist-") as temp_dir:
            repo_root = Path(temp_dir)
            nova_root = repo_root / "NOVA"
            nova_root.mkdir()
            (nova_root / "watchlist.json").write_text(
                json.dumps({
                    "sources": [
                        {"name": "release-notes", "url": "https://example.invalid/a"},
                        {"name": " RELEASE-NOTES ", "url": "https://example.invalid/b"},
                    ]
                }),
                encoding="utf-8",
            )

            with patch("NOVA.operational_observer.load_health_state") as load_state, patch(
                "NOVA.operational_observer.fetch_text"
            ) as fetch, patch("NOVA.operational_observer.atomic_write_json") as write_state:
                with self.assertRaisesRegex(RuntimeError, "duplicate source identities"):
                    run(repo_root)

            load_state.assert_not_called()
            fetch.assert_not_called()
            write_state.assert_not_called()

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

    def test_returning_to_previous_content_creates_new_event_and_supersedes_old_pending_events(self):
        state = {"observations": {}, "events": {}}
        source = {"name": "release-notes", "url": "https://example.invalid/annotation"}
        with patch(
            "NOVA.operational_observer.fetch_text",
            side_effect=[(200, "Content A", None), (200, "Content B", None), (200, "Content A", None)],
        ):
            results = [
                observe_source(source, state, timeout=5, max_bytes=1024)
                for _ in range(3)
            ]

        self.assertEqual([result["status"] for result in results], ["CHANGED", "CHANGED", "CHANGED"])
        events = list(state["events"].values())
        self.assertEqual(len(events), 3)
        self.assertEqual(events[0]["fingerprint"], events[2]["fingerprint"])
        self.assertNotEqual(events[0]["event_id"], events[2]["event_id"])
        self.assertEqual(
            [event["analysis_status"] for event in events],
            ["SUPERSEDED", "SUPERSEDED", "PENDING"],
        )
        self.assertEqual(
            [event["action_status"] for event in events],
            ["SUPERSEDED_BY_NEW_OBSERVATION", "SUPERSEDED_BY_NEW_OBSERVATION", "PENDING_POLICY_DECISION"],
        )

    def test_cached_analysis_without_matching_fingerprint_is_requeued_without_duplicate_event(self):
        state = {"observations": {}, "events": {}}
        source = {
            "name": "release-notes",
            "url": "https://example.invalid/annotation",
            "analysis_valid_for_seconds": 3600,
        }
        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            first = observe_source(source, state, timeout=5, max_bytes=1024)
        memory = state["observations"]["external-annotation:release-notes"]
        memory["analysis"] = {"decision": "legacy cached result"}
        memory.pop("analysis_fingerprint", None)
        memory.pop("analysis_observed_at", None)

        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            second = observe_source(source, state, timeout=5, max_bytes=1024)

        memory = state["observations"]["external-annotation:release-notes"]
        self.assertEqual(first["analysis_action"], "ANALYSIS_REQUIRED")
        self.assertEqual(second["status"], "UNCHANGED")
        self.assertEqual(second["analysis_action"], "ANALYSIS_REQUIRED")
        self.assertIsNone(memory["analysis"])
        self.assertTrue(memory["analysis_invalidated"])
        self.assertEqual(memory["analysis_history"][-1]["provenance_status"], "UNVERIFIED_ANALYSIS_FINGERPRINT")
        self.assertEqual(len(state["events"]), 1)
        self.assertEqual(next(iter(state["events"].values()))["analysis_status"], "PENDING")

    def test_cached_analysis_without_analysis_timestamp_is_requeued(self):
        state = {"observations": {}, "events": {}}
        source = {
            "name": "release-notes",
            "url": "https://example.invalid/annotation",
            "analysis_valid_for_seconds": 3600,
        }
        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            observe_source(source, state, timeout=5, max_bytes=1024)
        memory = state["observations"]["external-annotation:release-notes"]
        memory["analysis"] = {"decision": "untimed cached result"}
        memory["analysis_fingerprint"] = memory["fingerprint"]
        memory.pop("analysis_observed_at", None)

        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            result = observe_source(source, state, timeout=5, max_bytes=1024)

        memory = state["observations"]["external-annotation:release-notes"]
        self.assertEqual(result["analysis_action"], "ANALYSIS_REQUIRED")
        self.assertIsNone(memory["analysis"])
        self.assertTrue(memory["analysis_invalidated"])
        self.assertEqual(memory["analysis_history"][-1]["provenance_status"], "UNVERIFIED_ANALYSIS_TIMESTAMP")

    def test_pending_current_event_prevents_cache_reuse_without_duplicate_event(self):
        state = {"observations": {}, "events": {}}
        source = {
            "name": "release-notes",
            "url": "https://example.invalid/annotation",
            "analysis_valid_for_seconds": 3600,
        }
        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            first = observe_source(source, state, timeout=5, max_bytes=1024)
        memory = state["observations"]["external-annotation:release-notes"]
        memory["analysis"] = {"decision": "review"}
        memory["analysis_fingerprint"] = memory["fingerprint"]
        memory["analysis_observed_at"] = memory["observed_at"]
        self.assertEqual(first["analysis_action"], "ANALYSIS_REQUIRED")
        self.assertEqual(len(state["events"]), 1)

        with patch("NOVA.operational_observer.fetch_text", return_value=(200, "Content A", None)):
            second = observe_source(source, state, timeout=5, max_bytes=1024)

        self.assertEqual(second["analysis_action"], "ANALYSIS_REQUIRED")
        self.assertEqual(len(state["events"]), 1)
        pending = next(iter(state["events"].values()))
        self.assertEqual(pending["analysis_status"], "PENDING")

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
