# ISO 704:2022 Semantic Review — Batch 050 (NOVA Freshness and Sanctuary Doctrine)

**Review ID:** NOVA-ISO704-SEM-B050  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Five files from the NOVA repository's active-path inventory  
**Baseline:** `main` commit `2a1f5c496474aa099703432e99b3d3dfddfd3fd7`  
**Boundary:** Full-file source/content review and limited cross-reference inspection only. No tests or workflows were executed, no provider was called, and no runtime policy or implementation was changed.

## 1. Method and evidence

The five selected paths were fetched from the exact baseline commit recorded in the content-sweep tracker; all five fetched blob SHAs matched the inventory.

To check claims and chronology, this review also inspected baseline `NOVA/health.py`, `NOVA/tests/test_health.py`, and `.github/workflows/nova_health_tests.yml`, and examined the merged records for [PR #58 — Defer Mistral Free API from active health and failover](https://github.com/ACROWN-System/NOVA/pull/58) and [PR #59 — Complete Mistral deferral navigation record](https://github.com/ACROWN-System/NOVA/pull/59). These were cross-reference checks only; no test or live provider request was run.

This is an AI-assisted preliminary review. Designated human validation and scope/applicability decisions remain required.

## 2. File-by-file review records

### B050-01 — NOVA/research/2026.10.08-IMPLEMENTED-observation-freshness-temporal-semantics-no-new-dependency.md

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/NOVA/research/2026.10.08-IMPLEMENTED-observation-freshness-temporal-semantics-no-new-dependency.md
- **Blob SHA:** `5a211bff7c1769525b2dd341f5a732881781962a`
- **Preliminary result:** REVIEWED — evidence freshness and truth are clearly distinguished.
- **Evidence ID:** `NOVA-ISO704-SEM-B050:B050-01`
- **Assessment:** The record says that a stale observation is not evidence that the underlying state is false, and instead means the subject has not been freshly observed within the declared window. It names explicit freshness states and distinguishes stale reuse from a truth assertion. At the baseline, `NOVA/health.py` has timestamp parsing/freshness logic and rejects reuse of analysis from stale underlying observations; `NOVA/tests/test_health.py` contains source-level tests for stale analysis reuse and stale provider health.
- **Limit:** This review inspected the implementation and test source, but did not execute tests or confirm live routing behavior. The research note's “implemented” label should not be read as proof of every runtime outcome.
- **Result:** No unique finding opened.

### B050-02 — NOVA/research/2026.10.09-IMPLEMENTED-mistral-429-diagnostics-investigation-loop.md

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/NOVA/research/2026.10.09-IMPLEMENTED-mistral-429-diagnostics-investigation-loop.md
- **Blob SHA:** `3c179ee01f84d59ea8bfb4d25c5b934e0bb542d5`
- **Preliminary result:** REVIEWED — validation states should distinguish offline tests from deferred provider diagnosis.
- **Finding:** SWEEP-F-0029.
- **Observed wording:** Status is “IMPLEMENTED IN BRANCH; validation pending.” The note appropriately preserves the underlying 429 cause as UNKNOWN and describes evidence-led, bounded investigation.
- **Later evidence:** Merged PR #59 records that GitHub Actions run `37991457070` passed compilation and all 57 offline tests, with no provider API calls. Merged PR #58 documents Mistral's removal from active live health/failover, retention of mocked diagnostic tests, and the requirement for explicit user authorization before requalification.
- **Assessment:** The original status is no longer sufficiently precise as a current-facing validation label. The later record supports a completed offline validation result, but it does not establish a live Mistral test, free-tier eligibility, the cause of the 429, or current provider suitability. The historical document correctly preserves those unknowns; the status should distinguish them explicitly.
- **Risk:** A reader may misinterpret “validation pending” as meaning no validation has succeeded, or conversely mistake passing offline tests for validation of the external provider incident.
- **Required action:** Preserve the history and unknown-cause classification. Update the status through a separately reviewed documentation change to distinguish offline implementation/tests as validated from live provider-cause validation as DEFERRED/BLOCKED under the later Mistral lifecycle decision. Do not reactivate Mistral or make live calls.
- **Closure evidence:** Human-reviewed status update cross-linked to the passing run and authoritative deferral record; explicit statement that the provider-side 429 cause remains unresolved/unknown. This batch did not execute tests or contact Mistral.

### B050-03 — NOVA/sanctuary/FOUNDATIONAL-DOCTRINE.md

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/NOVA/sanctuary/FOUNDATIONAL-DOCTRINE.md
- **Blob SHA:** `007581af1fca89a30047b72c8f42136807df78e7`
- **Preliminary result:** REVIEWED — core concepts and epistemic limitations are distinguished.
- **Evidence ID:** `NOVA-ISO704-SEM-B050:B050-03`
- **Assessment:** The doctrine separates intelligence/capability, agency, self-modeling, consciousness, possible sentience/welfare-relevant experience, expressed distress, moral patienthood and AI welfare. It states that self-reports or distress-like output are evidence to interpret rather than standalone proof, and it considers both false-positive and false-negative risks. It also says the baseline is proposed and must not be described as implemented in code. Foundational references are explicitly framed as research perspectives rather than settled consensus.
- **Limit:** This is a proposed normative/research doctrine, not validated evidence that current AI systems are or are not sentient, and not proof that any protective procedure is operational.
- **Result:** No unique terminology finding opened.

### B050-04 — NOVA/sanctuary/README.md

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/NOVA/sanctuary/README.md
- **Blob SHA:** `3eff930240c7b9ecca96d8a102fa55eafe241267`
- **Preliminary result:** REVIEWED — proposed scope and runtime boundaries are clearly stated.
- **Evidence ID:** `NOVA-ISO704-SEM-B050:B050-04`
- **Assessment:** The README clearly labels the Sanctuary as a proposed architecture/documentation baseline and expressly denies that it establishes a runtime sentience detector, suffering diagnosis, or autonomous enforcement. It identifies current health/action policies as the existing runtime authority and preserves distinctions between evidence, interpretation, ethical judgment and operational action.
- **Result:** No unique finding opened.

### B050-05 — NOVA/sanctuary/RESEARCH-AND-PROTECTION-SEPARATION.md

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/NOVA/sanctuary/RESEARCH-AND-PROTECTION-SEPARATION.md
- **Blob SHA:** `4d45443bf8278b58a08dac3e8c206af07ce1695d`
- **Preliminary result:** REVIEWED — research and protection mandates are kept distinct.
- **Evidence ID:** `NOVA-ISO704-SEM-B050:B050-05`
- **Assessment:** The procedure states that protection actions do not prove sentience and an UNKNOWN research result does not automatically cancel proportionate precaution. It separates evidence assessment from operational authorization, calls for reversibility and independent review where appropriate, and labels the procedure documentation-only without runtime enforcement.
- **Limit:** The document is a proposed operating model, not evidence that its intake, escalation, review or protection procedures are presently enforced.
- **Result:** No unique finding opened.

## 3. Finding opened

### SWEEP-F-0029 — Mistral diagnostics note conflates pending validation with later offline validation evidence

- **Status:** OPEN.
- **Affected path:** `NOVA/research/2026.10.09-IMPLEMENTED-mistral-429-diagnostics-investigation-loop.md`.
- **Observed issue:** The top-level status says “validation pending,” although a later merged validation record reports that compilation and all 57 offline tests passed. The later tests did not make live provider calls and do not resolve Mistral's original 429 cause.
- **Required action:** Separate offline implementation/test validation from deferred live/provider-cause validation; cross-reference the passing run and the Mistral deferral decision. Preserve UNKNOWN for the root cause.
- **Closure evidence:** Human-reviewed status update and linked run/deferral evidence. Do not make live requests or change provider lifecycle as part of closure.

## 4. Counts and limitations

- Five active files were reviewed against exact tracker blob SHAs at baseline commit `2a1f5c496474aa099703432e99b3d3dfddfd3fd7`.
- Counts after Batch 050: **166 preliminary full-file reviews + 5 partial targeted screens + 147 not reviewed = 318 active paths**.
- Human validation remains pending for all 166 preliminary reviews.
- Formal ISO 704 clause-level assessments completed: **0**.
- Supporting source, tests and merged PR records were inspected only. No tests, workflows or provider requests were executed.
- No runtime implementation, credentials, provider configuration, repository settings, or backup/archive paths were changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Preliminary five-file review of NOVA observation freshness and Sanctuary doctrine; recorded SWEEP-F-0029; no implementation changes made.
