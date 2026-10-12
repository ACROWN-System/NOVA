import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class WorkflowCoverageTests(unittest.TestCase):
    def test_health_suite_runs_for_all_workflow_file_changes(self):
        workflow = (
            ROOT / ".github/workflows/nova_health_tests.yml"
        ).read_text(encoding="utf-8")
        push = workflow.split("push:", 1)[1].split("pull_request:", 1)[0]

        self.assertIn("'NOVA/**'", push)
        self.assertIn("'.github/workflows/**'", push)
        self.assertIn("pull_request:", workflow)

    def test_cloudflare_smoke_workflow_is_covered_by_the_health_suite(self):
        workflow = (
            ROOT / ".github/workflows/nova_health_tests.yml"
        ).read_text(encoding="utf-8")
        push = workflow.split("push:", 1)[1].split("pull_request:", 1)[0]
        filters = [
            line.strip().strip("'").strip('"')
            for line in push.splitlines()
            if line.strip().startswith("- ")
        ]

        smoke_workflow = ".github/workflows/nova_cloudflare_smoke_test.yml"
        self.assertTrue(
            any(
                smoke_workflow.startswith(pattern.removesuffix("**").rstrip("/"))
                or pattern == ".github/workflows/**"
                for pattern in filters
            ),
            f"Health tests do not cover {smoke_workflow}",
        )


if __name__ == "__main__":
    unittest.main()
