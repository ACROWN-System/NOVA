# ISO 704:2022 Preliminary Semantic Review — Batch 022 (Payment Intent, Pricing Policy and Regression Contracts)

**Review ID:** NOVA-ISO704-SEM-B022  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/CONTRACT REVIEW COMPLETE FOR SEVEN FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main; exact blob SHAs below  
**Boundary:** No payment was created, no quote was used to settle a transaction, and no tests were executed. This is not a financial/legal audit or ISO clause-conformity result.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B022-01 | NOVA/economic_policy.json | 0a42783f6d9da248feb1256ff349609b38553e60 | REVIEWED — payment-intent and payment-execution states are differentiated in policy, but implementation metadata is inconsistent |
| B022-02 | NOVA/economic_state.json | 5c22065c2f7d7b0d5901261d7c843b52b1bf260f | REVIEWED — empty/zero initial state with null update timestamp is valid scaffolding, not current verified economic balance |
| B022-03 | NOVA/pricing_policy.json | 9bf076aa343b5d5ae4bd3ee576556d3c77bc35a2 | REVIEWED — tariff/notice/approval constraints clear; services table empty and dynamic pricing disabled |
| B022-04 | NOVA/pricing.py | 801e577633175cd33eac4883b696068a24cf05b0 | REVIEWED — provider-independent quotes/recommendations explicit; input validation for negative/invalid amounts and exchange-rate provenance is not defined here |
| B022-05 | NOVA/payments.py | 64b20092c2f6230127cb0129360211ce6d89914f | REVIEWED — settlement refuses without a verified adapter; intent nevertheless records `irreversible: true` although creation is a local state append |
| B022-06 | NOVA/tests/test_payments_and_pricing.py | b216f0b47a1123198d7d271b32388cd9b531334b | REVIEWED — tests preserve public-price invariance and human-gated settlement; negative quote/intent inputs are not covered |
| B022-07 | NOVA/tests/test_provider_policy.py | e1cdbbf9b2925de9701c9425d3bb3e87fafd8ead | REVIEWED — deferred Cerebras exclusion is asserted against current roster/workflow text; tests were not executed here |

## 2. Findings

### B022-F01 — Payment-intent policy and recorded object disagree about the intent's lifecycle

The economic policy labels `payment_intent_creation` as AUTONOMOUSLY_ALLOWED while `payment_execution` and irreversible transfers are human-gated. In `payments.py`, creating an intent only appends a record to an in-memory state object; the returned record has status `HUMAN_GATE_REQUIRED` and `irreversible: true`. `settle_payment()` refuses execution without a verified adapter. These controls largely support a safe “prepare, then gate settlement” architecture, but the field `irreversible: true` is semantically inconsistent with a locally created draft intent unless it describes the contemplated eventual transfer rather than the creation operation.

**Required action:** define separate concepts/statuses for (a) a local draft payment instruction, (b) a validated but unapproved intent, (c) approved payment authorization, (d) submitted settlement, and (e) confirmed irreversible transfer. Make `irreversible` describe the actual state/operation it refers to, or rename it to a prospective effect field. Keep payment execution human-gated; do not infer from “intent creation autonomous” that any funds move or any provider/network fee is impossible without validating all downstream effects.

### B022-F02 — Price quote relies on a supplied exchange rate without recording its evidence provenance

`convert_price()` documents that it uses a verified external exchange rate but accepts a number without source, observed-at timestamp, validity or verification status. `create_quote()` copies that rate into the computed settlement amount and validity window. The quote stores its own creation/expiry but not the exchange-rate source/version or observation age. This is a clear contract/documentation gap: the caller may provide a verified rate, but the function cannot establish that fact from its arguments.

**Required action:** require the caller to supply a validated rate record or attach rate-source, observed-at, valid-until, asset pair and evidence ID to the quote. Check the rate is finite and positive, validate reference amount and settlement asset, and reject missing/invalid/expired rate evidence instead of representing the result as a verified quote. Preserve historical quotes and source metadata for auditability. This review did not test any live market rate.

### B022-F03 — Payment/price validation lacks explicit negative and malformed-input cases

`validate_payment_intent()` checks network, asset, destination and non-empty amount, but the amount remains a string and is not verified as a finite positive decimal; the same path does not validate a recipient identifier, invoice binding or decimal precision. Pricing conversion and recommendation functions also lack visible checks for negative reference/current prices, negative cost ratios or invalid exchange rates. Existing tests only use positive, well-formed examples and do not exercise these boundaries.

**Required action:** define the amount/asset/network rules appropriate to the intended payment adapter and add negative tests in a separate reviewed code change. Reject malformed, non-finite, zero/negative or excessive-precision values where those are invalid, and bind amount/asset/network/destination to the specific invoice before approval. Keep “PASS” limited to the exact validation actually performed; it is not external destination verification or payment approval.

### B022-F04 — Blank service pricing policy and zero-initialized economic state are not operational evidence

`pricing_policy.json` has an empty services table and disables dynamic pricing. `economic_state.json` has null `updated_at`, zero operating/reserve pools and empty transaction/obligation/payment-intent lists. This is a valid initial data shape, but it does not prove a service tariff has been approved, provider cost has been measured, no transactions exist outside this file, or the real operating pool is precisely zero. The public-price policy is currently a design rule, not a completed tariff ledger.

**Required action:** label these values as an uninitialized/default state until a controlled ledger import/reconciliation and source-backed service-price records exist. Distinguish “no record yet” from “verified balance is zero”; do not use `NO_PAID_COST_REQUIRED` with zero defaults as a current economic decision without a current input snapshot. Retain the public principle that free backend capacity does not reduce the user tariff, but do not infer a concrete service price where `services` is empty.

### B022-C01 — Positive control: settlement remains blocked without a verified adapter

The payment implementation's `settle_payment()` always returns `HUMAN_GATE_REQUIRED_NO_VERIFIED_ADAPTER`; the test asserts that it does not perform automatic settlement. Policy also blocks irreversible transfers and public-price changes without a human gate. Preserve this boundary until an explicitly verified and reviewed adapter, authorization workflow, and transaction-reconciliation evidence exist.

### B022-C02 — Positive control: provider switch must not silently reprice users

The pricing policy states that public pricing is service-based rather than provider-based, backend changes must not immediately change user price, and provider switching must not reprice a quote inside its validity period. The recommendation is marked as requiring approval and dynamic pricing is disabled. These are useful definitions/controls, but the currently empty service table means they do not establish an approved live tariff.

## 3. Evidence and limitations

- No payment intent was created during this review; only source files were inspected.
- Tests were read but not run.
- No wallet/network adapter, exchange-rate source, quote, invoice or ledger was externally verified.
- The empty pricing service map and zero/null initial economic state are treated as uninitialized, not as factual evidence of live pricing or balances.
- No ISO 704 clause result is assigned because the full controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed payment and pricing policy/state, payment/quote implementation, and relevant regression tests. Identified lifecycle, exchange-rate provenance and input-validation gaps while preserving human-gated settlement and provider-independent pricing.
