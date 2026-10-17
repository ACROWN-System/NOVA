import json
import os
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

from NOVA.alerts import send_github_issue


def mock_response(payload):
    response = MagicMock()
    response.__enter__.return_value = response
    response.read.return_value = json.dumps(payload).encode("utf-8")
    return response


class GitHubAlertDeduplicationTests(unittest.TestCase):
    def test_existing_open_issue_receives_comment_instead_of_duplicate(self):
        issue_title = "NOVA AI heart: groq model model-a health is unacceptable"
        existing = {
            "number": 42,
            "title": issue_title,
            "html_url": "https://github.com/example/repo/issues/42",
        }
        with patch.dict(os.environ, {
            "GITHUB_TOKEN": "test-token",
            "GITHUB_REPOSITORY": "example/repo",
        }):
            with patch(
                "NOVA.alerts.urllib.request.urlopen",
                side_effect=[mock_response([existing]), mock_response({"id": 1})],
            ) as urlopen:
                result = send_github_issue(issue_title, '{"health_status":"UNACCEPTABLE"}')

        self.assertTrue(result)
        self.assertEqual(urlopen.call_count, 2)
        list_req = urlopen.call_args_list[0].args[0]
        comment_req = urlopen.call_args_list[1].args[0]
        self.assertEqual(list_req.method, "GET")
        self.assertIn("/issues?state=open&per_page=100", list_req.full_url)
        self.assertEqual(comment_req.method, "POST")
        self.assertTrue(comment_req.full_url.endswith("/issues/42/comments"))
        self.assertNotIn("/issues", comment_req.full_url.split("/comments")[0].rsplit("/", 1)[-1])

    def test_new_open_issue_created_when_exact_title_is_absent(self):
        issue_title = "NOVA AI heart: gemini model model-b health is unacceptable"
        with patch.dict(os.environ, {
            "GITHUB_TOKEN": "test-token",
            "GITHUB_REPOSITORY": "example/repo",
        }):
            with patch(
                "NOVA.alerts.urllib.request.urlopen",
                side_effect=[mock_response([]), mock_response({
                    "number": 43,
                    "html_url": "https://github.com/example/repo/issues/43",
                })],
            ) as urlopen:
                result = send_github_issue(issue_title, '{"health_status":"UNACCEPTABLE"}')

        self.assertTrue(result)
        self.assertEqual(urlopen.call_count, 2)
        create_req = urlopen.call_args_list[1].args[0]
        self.assertEqual(create_req.method, "POST")
        self.assertTrue(create_req.full_url.endswith("/issues"))
        self.assertNotIn("/comments", create_req.full_url)

    def test_issue_listing_failure_does_not_fall_back_to_duplicate_creation(self):
        issue_title = "NOVA AI heart: groq model model-c health is unacceptable"
        with patch.dict(os.environ, {
            "GITHUB_TOKEN": "test-token",
            "GITHUB_REPOSITORY": "example/repo",
        }):
            with patch(
                "NOVA.alerts.urllib.request.urlopen",
                side_effect=urllib.error.URLError("listing unavailable"),
            ) as urlopen:
                result = send_github_issue(issue_title, '{"health_status":"UNACCEPTABLE"}')

        self.assertFalse(result)
        self.assertEqual(urlopen.call_count, 1)


if __name__ == "__main__":
    unittest.main()
