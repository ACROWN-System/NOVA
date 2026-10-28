import json
import unittest

from NOVA.reasoning import build_alert_body, validate_reasoning_payload


class ReasoningTests(unittest.TestCase):
    def test_valid_reasoning_contract(self):
        payload = {
            "significance": "HIGH",
            "affected_areas": ["github-actions"],
            "evidence": ["A published retirement notice"],
            "conclusion": "Investigate workflow compatibility.",
            "recommended_actions": ["Inspect workflows"],
            "model_recommended_autonomy_level": "L1_ANALYZE",
            "model_recommended_requires_human_gate": False,
            "confidence": 0.9,
        }
        ok, reason = validate_reasoning_payload(json.dumps(payload))
        self.assertTrue(ok)
        self.assertEqual(reason, "PASS")

    def test_invalid_reasoning_contract_is_rejected(self):
        ok, reason = validate_reasoning_payload("{}")
        self.assertFalse(ok)
        self.assertEqual(reason, "SCHEMA_FIELDS_MISMATCH")

    def test_non_object_json_payloads_are_rejected_without_exception(self):
        for content in ("null", "123", "true", '"text"', "[]"):
            with self.subTest(content=content):
                ok, reason = validate_reasoning_payload(content)
                self.assertFalse(ok)
                self.assertEqual(reason, "INVALID_JSON_TYPE")

    def test_high_impact_model_recommendation_requires_a_human_gate(self):
        payload = {
            "significance": "HIGH",
            "affected_areas": [],
            "evidence": ["Observed state only"],
            "conclusion": "A human should review this recommendation.",
            "recommended_actions": ["Review"],
            "model_recommended_autonomy_level": "L5_IRREVERSIBLE",
            "model_recommended_requires_human_gate": False,
            "confidence": 0.99,
        }
        ok, reason = validate_reasoning_payload(json.dumps(payload))
        self.assertFalse(ok)
        self.assertEqual(reason, "HIGH_IMPACT_REQUIRES_HUMAN_GATE")

    def test_alert_labels_model_analysis_as_advisory_and_shows_policy_permissions(self):
        analysis = {
            "model_recommended_autonomy_level": "L5_IRREVERSIBLE",
            "model_recommended_requires_human_gate": True,
            "confidence": 0.99,
        }
        body = json.loads(build_alert_body(analysis, ["analyze", "human_gate_for_irreversible_action"]))
        self.assertEqual(body["model_analysis_authority"], "ADVISORY_ONLY")
        self.assertEqual(body["confidence_semantics"], "UNCALIBRATED_SELF_ASSESSMENT")
        self.assertEqual(body["model_analysis"], analysis)
        self.assertEqual(
            body["permitted_action_classes"],
            ["analyze", "human_gate_for_irreversible_action"],
        )
        self.assertEqual(body["permitted_action_classes_source"], "NOVA/action_policy.json")

    def test_boolean_confidence_is_rejected_as_not_numeric_confidence(self):
        payload = {
            "significance": "LOW",
            "affected_areas": [],
            "evidence": ["No observed change"],
            "conclusion": "No action indicated by this observation alone.",
            "recommended_actions": [],
            "model_recommended_autonomy_level": "L1_ANALYZE",
            "model_recommended_requires_human_gate": True,
            "confidence": True,
        }
        ok, reason = validate_reasoning_payload(json.dumps(payload))
        self.assertFalse(ok)
        self.assertEqual(reason, "INVALID_CONFIDENCE")

    def test_confidence_outside_unit_interval_is_rejected(self):
        payload = {
            "significance": "LOW",
            "affected_areas": [],
            "evidence": ["No observed change"],
            "conclusion": "No action indicated by this observation alone.",
            "recommended_actions": [],
            "model_recommended_autonomy_level": "L1_ANALYZE",
            "model_recommended_requires_human_gate": True,
            "confidence": 1.1,
        }
        ok, reason = validate_reasoning_payload(json.dumps(payload))
        self.assertFalse(ok)
        self.assertEqual(reason, "INVALID_CONFIDENCE")


if __name__ == "__main__":
    unittest.main()
