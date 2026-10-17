# ISO 704:2022 Preliminary Semantic Review — Batch 023 (Allocation Policy, Test Budgets and Dated Provider Observations)

**Review ID:** NOVA-ISO704-SEM-B023  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/CONTRACT REVIEW COMPLETE FOR SEVEN FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main; exact blob SHAs below  
**Boundary:** This is a semantics and evidence-state review. No code/tests were executed, no credentials were read, and no provider was contacted.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B023-01 | NOVA/allocation.py | e36445d126dad679be14b2da28cc8c12d300ecb6 | REVIEWED — possible hard-eligibility defect when required capacity is unknown/malformed |
| B023-02 | NOVA/tests/test_allocation.py | 24cc8d16e86d956d33b80689997e697cad4c4428 | REVIEWED — good resource/call separation and unknown-economics test, but missing tests for unknown required resource dimensions |
| B023-03 | NOVA/capacity_policy.json | 92398e94b5ff25d8773ca02df661fd7634097568 | REVIEWED — policy says missing measures are UNKNOWN and hard capacity dimensions must fit |
| B023-04 | NOVA/development_test_budget.json | 9fe5dbfbdb27dc54d95af83358fedfd901dd10bc | REVIEWED — protective limits stated; some values are historical/unset, and one-time/recurring scope should remain explicit |
| B023-05 | NOVA/capacity_observations/gemini_2026-10-08.json | f329073ab12a668a3f6de12687662e8751bf148b | REVIEWED — dated project-level observation; peak usage is not remaining quota and is too old for current-state claims |
| B023-06 | NOVA/provider_observations/mistral_2026-10-08.json | 2e1c98e661db03ac05a106039df7a28322afc858 | REVIEWED — dated workspace observation is account-specific and was superseded by later Mistral deferral policy; retain historically |
| B023-07 | NOVA/tests/test_credential_readiness.py | 94a0b65ce942c99413f645a89d33a576e15e074f | REVIEWED — tests explicitly keep configured credentials separate from verified provider/GPU activation |

## 2. Findings

### B023-F01 — Candidate can remain eligible when a required call/resource allowance is unknown

In `allocation.py`, when a task requires calls or tokens but the corresponding remaining allowance cannot be read, `_check_dimension_requirements()` appends `CALL_ALLOWANCE_UNKNOWN` / `TOKEN_ALLOWANCE_UNKNOWN` and continues returning `fits=True`. The same occurs when a required total resource amount is absent or unreadable: it appends `TOTAL_RESOURCE_UNKNOWN:<name>` but still returns `fits=True`. `evaluate_candidate()` then leaves `hard_eligible` true if other gates pass. Additionally, `_required_value()` converts absent, malformed or negative required-call/token amounts to a non-negative value (often zero), which can hide an invalid task specification.

This appears inconsistent with `capacity_policy.json`, whose allocation engine lists call-allowance fit and total-resource fit as hard dimensions, while its measurement policy says missing measurements are UNKNOWN, never unlimited. It may allow a selection even though feasibility has not been established. This is a source-level logic risk, not proof that a real allocation was incorrectly executed.

**Required action:** review and change the allocator in a separate reviewed implementation PR. When a task declares a positive required dimension and the corresponding remaining amount is unknown, the candidate should be BLOCKED/INELIGIBLE for that hard dimension (or return an explicit `FEASIBILITY_UNKNOWN` state that cannot be selected as eligible). Distinguish “not needed” from “required but unmeasured.” Reject negative or malformed task requirements instead of silently normalizing them to zero. Add tests for missing, null, malformed, negative, boolean and insufficient remaining request/token/total-resource values, then run the targeted suite and preserve the result.

### B023-F02 — Development budget mixes dated observations with policy caps

The test-budget file includes policy defaults (e.g. maximum fraction per day and reserve fraction), explicit UNSET states pending first observations, and Gemini per-model caps derived from an observation dated 2026-10-08. These are different kinds of values: policy choices, initial caps, and observed provider limits. The file correctly names its source record but must not let the dated caps appear to be current quota evidence indefinitely. Cloudflare and ZeroGPU caps are also planning limits, not proof of current allowance or of no-payment eligibility.

**Required action:** keep the quota observation's date, scope, source and validity/recheck rule linked to each derived budget cap. Mark caps as operator-imposed test limits vs observed account limits. Refresh them only from a new evidence-backed observation; a configured test ceiling must never increase assumed provider quota or eliminate a required reserve.

### B023-F03 — Historical observations are not current provider status

The Gemini observation dated 2026-10-08 explicitly labels itself project-scoped and says peak usage is not current remaining quota. At the assessment date it is nine days old. The Mistral observation dated 2026-10-08 records that the specific workspace showed “Upgrade required to activate API keys”; later repository policy deferred Mistral free health probes on 2026-10-10. This is not evidence that all Mistral plans are universally unavailable; it is a historical observation for a specific workspace followed by a project-specific deferral decision.

**Required action:** retain both files as historical evidence. Current dashboards and routing must use the current roster/lifecycle and fresh observation, while preserving the exact date/account scope and subsequent deferral decision. Do not describe the historical peak limits as remaining quota or the workspace observation as a universal provider rule.

### B023-C01 — Positive control: credential-readiness semantics are explicit

The test file asserts that absent slots are `REQUIRED_NOT_CONFIGURED`, non-empty slots become `CONFIGURED_NOT_VERIFIED`, GPU candidates remain `CANDIDATE_NOT_ACTIVATED`, and serialized reports do not contain secret values. Those are useful distinctions and should be preserved. The tests are source evidence only; they were not executed in this review.

## 3. Readiness effect and limitations

- The allocation-policy mismatch (B023-F01) is the principal follow-up: the policy calls capacity fit a hard dimension, but the implementation may still treat unknown required measures as eligible.
- Budget caps are not provider entitlements; historical rate limits and workspace states remain dated observations.
- No credential, provider API, workflow, economic transaction or allocation was executed.
- No ISO 704 clause-conformity result is assigned because the full controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed resource allocation code/tests, capacity policy, development test budget, dated Gemini/Mistral observations and credential-readiness tests; recorded unknown-required-resource eligibility as a code/test follow-up.
