import unittest
from NOVA.operational_state import merge_dynamic_roster


class OperationalStateRosterMergeTests(unittest.TestCase):
    def test_current_repository_configuration_wins_except_persisted_down_marker(self):
        repository = {
            "providers": [
                {"name": "groq", "status": "active", "models": ["new-model"],
                 "base_url": "https://new.example/api", "api_key_env": "GROQ_API_KEY_02"},
                {"name": "gemini", "status": "active", "models": ["gemini-current"]},
            ],
            "deferred_providers": [{"name": "mistral", "status": "DEFERRED"}],
        }
        persisted = {
            "providers": [
                {"name": "groq", "status": "down", "marked_down_at": "2026-10-10T10:00:00+00:00",
                 "models": ["obsolete-model"], "base_url": "https://old.example/api"},
                {"name": "gemini", "status": "active", "models": ["obsolete-gemini"]},
                {"name": "removed", "status": "down"},
            ],
            "deferred_providers": [{"name": "old-deferred"}],
        }
        result = merge_dynamic_roster(repository, persisted)
        self.assertEqual(result["providers"][0]["status"], "down")
        self.assertEqual(result["providers"][0]["marked_down_at"], "2026-10-10T10:00:00+00:00")
        self.assertEqual(result["providers"][0]["models"], ["new-model"])
        self.assertEqual(result["providers"][0]["base_url"], "https://new.example/api")
        self.assertEqual(result["providers"][0]["api_key_env"], "GROQ_API_KEY_02")
        self.assertEqual(result["providers"][1]["models"], ["gemini-current"])
        self.assertEqual(result["deferred_providers"], [{"name": "mistral", "status": "DEFERRED"}])
        self.assertEqual([p["name"] for p in result["providers"]], ["groq", "gemini"])

    def test_repository_policy_can_keep_provider_non_active(self):
        repository = {"providers": [{"name": "groq", "status": "deferred", "models": ["model"]}]}
        persisted = {"providers": [{"name": "groq", "status": "down",
                                    "marked_down_at": "2026-10-10T10:00:00+00:00"}]}
        result = merge_dynamic_roster(repository, persisted)
        self.assertEqual(result["providers"][0]["status"], "deferred")
        self.assertNotIn("marked_down_at", result["providers"][0])

    def test_removed_or_new_providers_follow_current_repository_roster(self):
        repository = {"providers": [{"name": "new-provider", "status": "active"}]}
        persisted = {"providers": [{"name": "removed-provider", "status": "down"}]}
        result = merge_dynamic_roster(repository, persisted)
        self.assertEqual(result["providers"], repository["providers"])

    def test_no_persisted_down_marker_leaves_current_status_unchanged(self):
        repository = {"providers": [{"name": "groq", "status": "active"}]}
        persisted = {"providers": [{"name": "groq", "status": "active"}]}
        self.assertEqual(merge_dynamic_roster(repository, persisted), repository)


if __name__ == "__main__":
    unittest.main()
