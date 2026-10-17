# ISO 704:2022 Preliminary Semantic Review — Batch 011 (GPU Heartbeat and Weak RSI Workflow Terms)

**Review ID:** NOVA-ISO704-SEM-B011  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** This is a terminology/status review. It is not a live credential validation, workflow execution, security audit or ISO clause-conformity result.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B011-01 | `NOVA/tests/test_gpu_heartbeat.py` | `5eae5afb7716f63562d8b623ca948c115571f576` | REVIEWED — states distinguish token authentication from capacity; test results are mocked, not live |
| B011-02 | `.github/workflows/nova_GPU_heartbeat.yml` | `8bfd9292d823c9833a28911a191a4a793d163ca7` | REVIEWED — workflow naming and permissions shown; code-reading does not prove latest runtime configuration |
| B011-03 | `.github/workflows/nova-weak-rsi.yml` | `0d1ed3146c1851107c05bb2a22df3847cd191c78` | REVIEWED — manual human-in-loop control is clear; eligibility field is an operator attestation, not independent verification |
| B011-04 | `NOVA/tests/test_weak_rsi_workflow.py` | `9d991fc907d70bdd76f4240bd4c95f0d17cdcb25` | REVIEWED — tests assert manual-only/read-only intent; no live provider or external term review is performed |

## 2. Findings and distinctions

### B011-F01 — Data-use eligibility input is a human attestation, not independent proof of provider eligibility

The Weak RSI workflow is manually dispatched, limits the provider choice to Groq/Gemini, uses read-only workflow permissions, keeps each secret scoped to its own selected step, and defaults the data-use eligibility input to NOT_APPROVED. Its input description explicitly asks the operator to review the selected provider's current terms and choose PASS_AFTER_REVIEW only after that review.

This is a useful human gate, but the workflow input itself does not prove that the relevant terms were inspected, that the chosen data is eligible, or that the provider's terms objectively permit the exact use. The term “PASS_AFTER_REVIEW” could be misunderstood downstream as an independent policy-validation result rather than a human attestation.

**Required action:** keep the input as an explicit human decision gate, but label the resulting field/report as an operator declaration or attestation, preserving reviewer, date, source version/URL, intended data/use and decision scope. Where the workflow cannot store supporting evidence, record the declaration separately in a controlled evidence record. Do not represent the string value alone as provider approval or independent compliance verification.

### B011-F02 — Positive control: GPU candidate states do not imply usable capacity

The GPU heartbeat tests distinguish:
- missing credential: REQUIRED_NOT_CONFIGURED;
- configured/authenticated credential;
- candidate lifecycle: CANDIDATE_NOT_ACTIVATED;
- capacity evidence: UNVERIFIED;
- unverified/absent credit balance, even when a mocked read-only endpoint returns assigned/reserved/settled figures.

The workflow's read-only candidate credential probe and the GPU roster's active-provider list are conceptually separate. These distinctions are valuable: a successful token/authentication check is not evidence of no-card eligibility, free-tier entitlement, usable recurring allocation, GPU job completion or capacity.

**Disposition:** preserve the distinctions. Do not collapse candidate credential health into provider activation or GPU-minutes.

### B011-F03 — Unit-test success is not live-provider evidence

The test module uses mocked response classes and patched network openers. It confirms that certain code paths would return sanitized states for known synthetic responses, including not logging account identity or credential values. The tests do not authenticate an actual Hugging Face or Nosana credential, query a live quota, validate the current endpoint, or establish an actual free allocation.

The Weak RSI workflow tests also inspect YAML text for workflow triggers, permissions, secret placement and artifact settings; they do not dispatch the workflow or evaluate provider policy.

**Required action:** when these tests are referenced in the readiness package, classify them as deterministic/offline implementation evidence. Keep separate evidence types for static configuration review, mocked unit tests, workflow CI, manual runtime execution, actual provider response, account/terms qualification, and capacity measurement.

## 3. Terminology notes

- “GPU heartbeat” is a scheduled observation workflow; the name does not mean there is an active provider or usable GPU allocation.
- “Credential configured”, “authenticated”, “candidate”, “active”, “capacity verified” and “resource eligible” describe distinct lifecycle dimensions.
- “Weak RSI” is implemented as a manually triggered, bounded report-only workflow in the reviewed YAML. The word “RSI” in the workflow title must not be interpreted as the higher-autonomy Strong RSI readiness state.
- The test expectation that the aggregate GPU planning reference is 86,400 while explicitly asserting PROVISIONAL_UNVALIDATED / not a requirement / feasibility not established is internally well-bounded; it is not a capacity claim.

## 4. Evidence and limitations

- All four source files were reviewed at the exact baseline blob SHAs above.
- No workflow was triggered; no credential values were read or changed; no live API was called.
- Source/test inspection alone does not validate current default-branch settings, execution permissions, account eligibility or actual behavior.
- No clause-level ISO 704 assessment is performed because the full controlled standard baseline remains blocked.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Preliminary review of GPU heartbeat tests/workflow and Weak RSI manual workflow/tests.
