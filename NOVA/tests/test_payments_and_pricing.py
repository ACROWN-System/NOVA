import unittest
from decimal import Decimal

from NOVA.payments import create_payment_intent, validate_payment_intent, settle_payment
from NOVA.pricing import convert_price, recommend_price


class PaymentsPricingTests(unittest.TestCase):
    def test_public_price_conversion_is_provider_independent(self):
        self.assertEqual(
            convert_price(Decimal("1"), rate_to_settlement=Decimal("200")),
            Decimal("200.00000000"),
        )

    def test_price_recommendation_is_governed_and_bounded(self):
        result = recommend_price(
            Decimal("10"),
            realized_cost_ratio=Decimal("0.95"),
            target_margin_ratio=Decimal("0.20"),
            max_change_ratio=Decimal("0.10"),
        )
        self.assertTrue(result["provider_independent"])
        self.assertTrue(result["requires_approval"])
        self.assertEqual(result["recommended_price"], "11.00000000")

    def test_payment_intent_is_not_automatic(self):
        state = {"payment_intents": []}
        intent = create_payment_intent(
            state,
            beneficiary_id="provider-a",
            destination="verified-destination",
            network="solana",
            asset="USDC",
            amount="5.00",
            invoice_reference="INV-1",
        )
        self.assertEqual(intent["status"], "HUMAN_GATE_REQUIRED")
        self.assertEqual(
            validate_payment_intent(
                intent,
                expected_network="solana",
                expected_asset="USDC",
                expected_destination="verified-destination",
            ),
            (True, "PASS"),
        )
        self.assertEqual(settle_payment(intent), (False, "HUMAN_GATE_REQUIRED_NO_VERIFIED_ADAPTER"))


if __name__ == "__main__":
    unittest.main()
