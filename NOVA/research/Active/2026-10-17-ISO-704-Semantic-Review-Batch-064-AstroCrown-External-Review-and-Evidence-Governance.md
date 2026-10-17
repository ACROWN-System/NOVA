# Semantic Review Batch 064 — AstroCrown External Review and Evidence Governance

**Document ID:** NOVA-ISO704-SEM-B064  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Purpose:** Review terminology, evidence/provenance boundaries, status claims, and the external-review measurement pipeline. This is not a formal ISO 704 clause assessment, execution test, legal approval, or independent security review.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B064-01 | `development/audit/external-review/ledger.json` | `4080a310df6b3c4f51db732e85be4baaf90b076e` | No unique finding |
| B064-02 | `development/audit/external-review/pipeline.py` | `f954990f5f64f803cff8a874f3928eafb04c4036` | SWEEP-F-0036 |
| B064-03 | `development/audit/external-review/README.md` | `ac4c4405172facee10736537cd9d6a24f56970d6` | No unique finding |
| B064-04 | `development/audit/external-review/tests/test_pipeline.py` | `fbfeb6e8aae7221756f4a361d8989814d6f73ce8` | Corroborates SWEEP-F-0036 test gap |
| B064-05 | `development/audit/FACT-OBSERVATION-AND-EVIDENCE-GOVERNANCE.md` | `4726c0a0ed4c626ba7f522550cda1a58953b1d55` | No unique finding |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. The source files were read only and remain unchanged.

## 2. Semantic review results

### B064-01 — External-review outreach ledger

The ledger records the one sent outreach with reply, acceptance, completion and qualification fields left unknown; its note makes clear that inbox state is not accessible through this tool connection. Its `planning_scenarios` entry is explicitly marked `UNVALIDATED_PLANNING_SCENARIO`, source-attributed as a user-supplied estimate, and limited to sensitivity analysis. This separates observed events from a planning assumption and avoids treating an unobserved reply as failure.

**Disposition:** no unique finding. The ledger was reviewed as data; no personal contact details or inbox contents were accessed.

### B064-02 — External-review pipeline

The pipeline generally separates reviewer fit from conversion probability, keeps unknown factor values unknown, requires evidence references for numeric factor ratings, validates outreach event ordering, uses conditional denominators, and marks low-sample rates as descriptive rather than calibrated. The use of a Wilson interval and explicit forecast-validation status is presented as a measurement aid, not as proof of independence or review quality.

A schema validation weakness exists in `analyze_ledger`: `if ledger.get("schema_version") != 1` checks equality, not exact type. In Python, `True == 1` evaluates true, and `1.0 == 1` also evaluates true. A JSON ledger whose `schema_version` is boolean `true` or number `1.0` therefore passes this guard even though the field is a version identifier expected to be an integer. This weakens the documented malformed-input boundary. The function does validate that `outreach_records` is a list and that its records are objects, but the version-field check does not enforce an exact integer type.

**Disposition:** SWEEP-F-0036 — input-schema type-validation gap. A narrow fix would require an integer value that is not a boolean and equals the supported version, with negative tests for `true`, `1.0`, `null`, strings and unsupported integers. This batch did not execute those examples or change source/tests.

### B064-03 — External-review pipeline README

The README makes clear that the process gathers evidence rather than proving an external review occurred. It treats automated analysis as supplemental, preserves separate hard gates (competence, independence/conflicts, scope agreement, zero-cost feasibility), and says candidate fit scores are not probabilities. It also clearly labels the low conversion scenario as an unvalidated user-supplied sensitivity case and does not use it as a training observation.

The OSS Scanner and Snyk/Alpha–Omega discussions are explicitly dated 2026-10-11 and distinguish eligibility candidates from acceptance or award. The `Current status` section is a status snapshot whose freshness was not independently revalidated by this batch. No external program eligibility, pricing, or enrollment terms were refreshed as part of the file review.

**Disposition:** no unique finding. Preserve the snapshot date and do not promote the dated program descriptions into present-day eligibility claims without a separate current-source review.

### B064-04 — External-review pipeline tests

The tests cover evidence coverage, refusing numeric scores without evidence, open outreach not being counted as failure, conditional event-stage denominators, unknown user scenario separation, Wilson interval uncertainty, event ordering, duplicate outreach IDs, and closed no-reply end-to-end outcomes. They do not include a test that `schema_version` must have an exact integer type, so the `true`/`1.0` acceptance path identified in B064-02 is not guarded by the recorded unit-test cases.

**Disposition:** corroborates SWEEP-F-0036. Test code was inspected, not run.

### B064-05 — Fact observation, independent derivation and evidence governance

The proposed governance document distinguishes factual observation, source claim, hypothesis/inference, general method, expressive material, licensed component, restricted/confidential information, and unknown/blocked states. It cautions that observing behavior does not confer permission to copy restricted material, that multiple sources may be correlated, and that hashes or labels do not establish truth, authorship, ownership, or legal permission. It separates shareable technical summaries from restricted evidence packages and calls for appropriate jurisdiction-specific counsel for material legal questions.

The document includes India and U.S. legal references as examples and explicitly says they must not be generalized across jurisdictions. This review did not independently revalidate the current legal status or applicability of cited authorities.

**Disposition:** no unique finding. Treat this as a proposed engineering-governance convention, not a legal opinion or proof of compliance.

## 3. New finding

### SWEEP-F-0036 — External-review ledger accepts malformed schema-version types

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/audit/external-review/pipeline.py`, function `analyze_ledger`; related coverage path `development/audit/external-review/tests/test_pipeline.py`.
- **Observed issue:** The guard `ledger.get("schema_version") != 1` relies on Python equality and does not reject `True` or `1.0`, both of which compare equal to integer `1`. Such JSON inputs can pass the version check despite the version field not being an integer.
- **Interpretation:** The guard does not fully enforce the intended schema-type contract. This is a narrow malformed-input validation defect inferred from source semantics; the pipeline was not executed to observe it at runtime.
- **Required action:** Validate that the value is an integer but not a boolean, and equals the supported version. Add negative unit cases for `true`, `1.0`, `null`, string values and unsupported integers, plus a positive integer-version case.
- **Closure evidence:** Reviewed code change, focused negative/positive unit-test output, and confirmation that the supported version and error status remain explicit.
- **Safety boundary:** No source/runtime file, test, outreach ledger, email/inbox, external-review submission, credential, provider call, repository setting, billing setting or backup/archive path was changed. No test or workflow was run.

No other new finding ID was opened. The existing proposed governance controls are distinguished from evidence that the process is operational or that an independent review has completed.

## 4. Counts, limits, and safety boundary

- Row-derived post-batch counts: **236 preliminary full-file reviews + 5 partial targeted screens + 77 not reviewed = 318 active paths**.
- Human validation remains pending for all 236 preliminary reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- All five target blob SHAs match the exact recorded baseline entries.
- The `schema_version` concern is a static source-level inference; code and tests were not executed.
- No AstroCrown-Web source/runtime file, backup/archive path, secret, credential, workflow, test, inbox, outreach submission, provider, billing, or repository setting was modified or used.
- Scope remains proposed and not human-approved.