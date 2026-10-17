# ISO 704:2022 Preliminary Semantic Review — Batch 020 (Quality Gates, Reasoning Payload and Economic Status)

**Review ID:** NOVA-ISO704-SEM-B020  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/CONTRACT REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main; exact blob SHAs below  
**Boundary:** This review inspected definitions/state transitions and validation logic. Tests were read only if in these paths; no tests were executed and no provider/model call was made.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B020-01 | NOVA/quality_gate.py | aa5e44d493691b70c0c29f1b4fafb12feea624b5 | REVIEWED — exact-commit/timezone/field-complete closure gate; legacy capability path remains an explicit exception |
| B020-02 | NOVA/tests/test_quality_gate.py | c947e4e8e342b0e4000346c01ed0addee8109711 | REVIEWED — tests cover incomplete closure, exact candidate SHA, time zone, recurrence reopening and rejected extra fields |
| B020-03 | NOVA/reasoning.py | 07cf4514aad6804fe027cf2e94358d179fee7e89 | REVIEWED — action execution is bounded, but malformed JSON types and model-authored human-gate semantics need stronger enforcement |
| B020-04 | NOVA/economics.py | 098fb18e90ddbc488407554a5a7bc38a38135b60 | REVIEWED — public tariff/backend separation is explicit; missing or invalid price/cost can default to numeric zero |

## 2. Findings

### B020-F01 — Reasoning payload validator needs explicit top-level/type and cross-field policy checks

The reasoning response validator parses JSON and compares the returned keys, but it does not first require the payload to be a dictionary. Some valid JSON values such as a number, null, or an array of unhashable items may raise a TypeError in the schema comparison rather than cleanly return a documented invalid-payload state. The confidence check uses isinstance(value, (int, float)), which also accepts Python booleans as numeric values. Enum membership checks can likewise raise if a model returns an unhashable list/dictionary rather than a string.

More importantly, requires_human_gate and autonomy_level are provided by the model and are validated only as an allowed enum/boolean. The code separately derives permitted_action_classes from project policy by significance, but it does not enforce cross-field consistency between high/critical significance, autonomy level, mandatory human gate, and permitted action classes at the validation layer.

**Required action:** separately review/update the validator and tests so it (a) requires a JSON object before key comparison; (b) verifies every field has its intended type before set membership/comparison; (c) rejects booleans for numeric confidence; (d) converts malformed shapes to controlled BLOCKED/invalid-payload results rather than uncaught exceptions; and (e) derives or strictly constrains mandatory human-gate requirements from trusted project policy, not merely model-authored fields. Verify all downstream consumers treat model-authored assertions as analysis data, not as permission to act. Do not treat this preliminary finding as proof a production exception occurred.

### B020-F02 — Missing or malformed pricing data can be represented as zero cost

The money() helper returns Decimal("0") for invalid/unparseable input. provider_cost() uses empty defaults for missing pricing metadata (including a default per-request cost of zero for an unknown unit). A provider without an explicitly free price or a valid complete tariff could therefore yield a numeric cost of zero, which is semantically different from cost unknown. The transaction record always stores numeric revenue/cost/contribution values and has no explicit estimate-vs-verified or unknown-cost state.

**Required action:** ensure absent/invalid values required for a cost calculation remain UNKNOWN/BLOCKED or return a validation error rather than zero. Represent explicitly free/contractually zero-cost resource separately from missing price evidence; require a valid tariff/source/scope when claiming a measured cost. Add negative tests for missing unit/rate, malformed decimals, negative rates or quantities, and missing provider price records. This is a candidate implementation defect requiring a separately reviewed code/test change, not a conclusion about a specific historical charge.

### B020-C01 — Positive control: failure-case closure is evidence-gated

The quality gate requires all defined closure fields, a 40-character candidate SHA, the exact same SHA used for verification, a passing regression result and a timezone-aware ISO-8601 verification timestamp. It rejects fields outside the approved closure schema and reopens a previously closed case if the same signature recurs, preserving the verified closure record before clearing its closure fields.

These are strong auditable semantics. Preserve the rule that repeated success or a model's explanation cannot close a root-cause case without direct/systemic cause, missed control, prevention control, regression test and exact-commit verification.

### B020-C02 — Positive control: model capability states are explicit, with one declared legacy exception

When a provider has a model_contracts object, an absent model/capability entry is blocked and only the exact VERIFIED state permits the declared capability. The tests check that candidate, blocked and absent model entries do not pass. The code deliberately allows legacy providers that do not declare a contract record and labels them LEGACY_UNDECLARED.

**Disposition:** keep the exception explicit and auditable. Before claiming all model execution is fail-closed, maintain a current inventory of providers/models still on LEGACY_UNDECLARED, the reason and migration decision; the unbounded legacy compatibility route is not equivalent to a verified model contract.

### B020-C03 — Positive control: public tariff does not follow backend provider cost

The economics module states that a switch from free to paid backend should not silently change the user's public service tariff. It also separates resource usage and provider cost from the public price, and adds headroom/runway statuses for a potential provider-cost transition.

**Caution:** the schema still needs an explicit distinction between actual, forecast, estimated and unknown amounts. A stored numeric zero is not sufficient evidence to establish that the underlying provider resource was free or that no payment could occur.

## 3. Evidence and limitations

- No runtime code changed in this review.
- Tests were not run; the relevant test file was only inspected for declared contract coverage.
- No live provider call, billing check, economic ledger reconciliation or account eligibility verification was performed.
- No ISO 704 clause result is assigned because the full controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed quality-gate functions/tests, reasoning payload validation and provider-agnostic economic accounting; recorded schema/gate and unknown-cost semantics for controlled follow-up.
