# Semantic Review Batch 058 — AstroCrown RSI Egress, Baseline and Cleanup

**Document ID:** NOVA-ISO704-SEM-B058  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR's head.  
**Purpose:** Preliminary terminology, evidence-boundary and documentation-lifecycle review. This is not a formal ISO 704 clause assessment, fresh security approval, or authorization to change RSI readiness.

## 1. Target manifest and source identity

| ID | Exact source path | Source commit | Verified blob SHA | Disposition |
|---|---|---|---|---|
| B058-01 | `development/audit/Active/2026-10-11-RSI-Provider-Egress-Boundary.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `79109d2ad13d15451ad933dfdb5fd8af7f688307` | SWEEP-F-0012 |
| B058-02 | `development/audit/Active/2026-10-11-RSI-Retention-Baseline-Binding.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `fe84a74b2ae33202c7e1af7c323576dab2a69c5c` | SWEEP-F-0031 |
| B058-03 | `development/audit/Active/2026-10-11-RSI-Sandbox-Cleanup-Verification.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `969ba74fd4e73e56e58a2725dc17923ce36f8306` | SWEEP-F-0012 |
| B058-04 | `development/audit/Active/2026-10-11-RSI-Strict-Schema-Type-Validation.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `832f54229666a9cf544a4f64b84de6bb23c06703` | SWEEP-F-0031 |
| B058-05 | `development/audit/Active/2026-10-11-RSI-Supervisor-IO-Failure-Cleanup.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `00089275037435f2664339f23d577cb80ea43ea5` | SWEEP-F-0012 |

All five fetched source blobs match their tracker rows exactly. Source contents under review were not modified.

## 2. Semantic review results

### B058-01 — Provider credential egress boundary completed audit mirror

This record explicitly identifies itself as a completed audit and an archival mirror under `development/audit/Active/`, and links the canonical Completed record. Its core terminology distinguishes an exact protected provider-host allowlist from an unrestricted endpoint URL, and rejects implicit redirect-following for requests carrying bearer credentials. Its own residual-risk section correctly limits the control: a host allowlist does not establish overall provider safety, and additional providers require explicit policy and credential review.

AstroCrown-Web [PR #65 — constrain RSI provider credential egress](https://github.com/ACROWN-System/AstroCrown-Web/pull/65) merged on 2026-10-10 22:04:54 UTC. The associated [CI run #38090029867](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38090029867) is recorded completed successfully. Its job-step listing reports success for immutable-image verification, compilation, RSI unit tests and Docker isolation-boundary checks.

**Disposition:** cross-reference SWEEP-F-0012. Do not move, rename or edit this Active-path mirror pending the existing human scope decision. No provider call or credential use was performed here.

### B058-02 — Retention baseline-binding navigation plan

This plan says the retention verifier must bind cycle/evaluator baseline evidence to the exact trusted workflow `GITHUB_SHA`, and demands an explicit expected full, lowercase 40-character commit SHA on both pre-apply and post-apply verifier calls. Its acceptance criteria keep RSI readiness INCOMPLETE and main promotion disabled.

AstroCrown-Web [PR #70 — bind retention evidence to exact workflow baseline](https://github.com/ACROWN-System/AstroCrown-Web/pull/70) merged on 2026-10-10 22:22:31 UTC. Its changed-file list includes this plan, the retention workflow, evidence verifier, engine and related tests. Associated [CI run #38091173406](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38091173406) is recorded as completed successfully; its step summary reports successful immutable-image verification, compilation, RSI unit tests and Docker isolation-boundary exercise.

The plan nevertheless remains `ACTIVE — require exact baseline commit before privileged patch application`. As its own plan was included in the merged implementation PR and the associated CI run is recorded successful, this is a candidate documentation-task closeout mismatch. It does not, by itself, mean that every security assumption was independently audited or that readiness may change.

**Disposition:** extend SWEEP-F-0031; a human should confirm the canonical Completed destination and closure metadata. Do not change readiness or promotion gates.

### B058-03 — Sandbox cleanup verification completed navigation-plan mirror

This record explicitly says COMPLETED, calls itself an archival mirror, links a canonical Completed record, and separately says independent sandbox approval remains BLOCKED. It distinguishes cleanup attempts from the observable postcondition that Docker reports no containers remain for a unique evaluation label. It also explicitly avoids claiming that a Docker container eliminates kernel/daemon escape risk.

AstroCrown-Web [PR #71 — verify sandbox cleanup before leaving failure paths](https://github.com/ACROWN-System/AstroCrown-Web/pull/71) merged on 2026-10-10 23:06:40 UTC. Associated [CI run #38093812456](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38093812456) is recorded completed successfully. [PR #73 — archive RSI security follow-up verification](https://github.com/ACROWN-System/AstroCrown-Web/pull/73) includes the Active-path file and the corresponding Completed-path record.

**Disposition:** cross-reference SWEEP-F-0012. Leave both the mirror and independent-sandbox-approval gate unchanged.

### B058-04 — Strict schema-type validation navigation plan

The plan identifies a Python/JSON semantic trap: booleans and floating-point numbers can compare equal to integer schema values unless actual integer types are required. It proposes strict checks for dispatcher registry versions and evidence-manifest versions, with regression coverage, while explicitly keeping production readiness and promotion gates closed.

AstroCrown-Web [PR #74 — reject malformed RSI schema version types](https://github.com/ACROWN-System/AstroCrown-Web/pull/74) merged on 2026-10-10 23:16:47 UTC. Its changed-file list includes this plan, the benchmark dispatcher, the evidence verifier and associated tests. The associated [CI run #38094165089](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38094165089) is recorded completed successfully; its step listing reports success for immutable-image verification, compilation, RSI unit tests and Docker isolation-boundary checks.

The record still says `ACTIVE — strict malformed-configuration handling under verification`. This is a candidate navigation-plan lifecycle mismatch after the plan's own PR and recorded CI run completed. The review does not infer Strong RSI is active or production-approved.

**Disposition:** extend SWEEP-F-0031. Request a human lifecycle/closure decision; preserve all readiness and benchmark gates.

### B058-05 — Supervisor I/O failure cleanup completed navigation-plan mirror

This record says COMPLETED and identifies itself as an archival mirror under Active, linked to a canonical Completed record. It distinguishes a confirmed process termination/container cleanup outcome (FAIL when cleanup is confirmed) from uncertainty (BLOCKED), and scopes the remediation to output-pipe/monitoring errors. It explicitly preserves the readiness and benchmark gates.

AstroCrown-Web [PR #76 — clean up sandbox after supervisor I/O failures](https://github.com/ACROWN-System/AstroCrown-Web/pull/76) merged on 2026-10-10 23:21:03 UTC; [CI run #38094680673](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38094680673) is recorded completed successfully. [PR #77 — archive RSI supervisor cleanup reviews](https://github.com/ACROWN-System/AstroCrown-Web/pull/77) includes both the Active and Completed counterparts for this record, corroborating its archival-mirror classification.

**Disposition:** cross-reference SWEEP-F-0012. No source move or edit is authorized by this content sweep.

## 3. Existing findings updated

### SWEEP-F-0031 — Active navigation plans after their own PRs merge

Batch 058 adds two further candidates: the retention baseline-binding plan (PR #70; CI run #38091173406 recorded successful) and strict schema-type-validation plan (PR #74; CI run #38094165089 recorded successful). Both plans were included in their corresponding merged implementation PRs while retaining ACTIVE/under-verification status. This is a documentation-task lifecycle observation requiring human confirmation, not proof that all downstream policy gates are satisfied.

### SWEEP-F-0012 — Completed archival mirrors under Active

Batch 058 adds three explicit completed mirror paths: provider credential egress boundary, sandbox cleanup verification, and supervisor I/O failure cleanup. Each identifies itself as a completed archival mirror and references a canonical Completed record. For the latter two, PR #73 and PR #77 respectively have changed-file evidence of an Active/Completed pair. Do not relocate or modify these paths until the existing human scope decision authorizes a disposition.

## 4. Counts, limits and safety boundary

- Row-derived post-batch counts: **206 preliminary full-file reviews + 5 partial targeted screens + 107 not reviewed = 318 active paths**.
- Human validation remains pending for all 206 preliminary reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- Each source blob SHA was matched against the tracker row at the recorded baseline commit.
- Historical PR lists and CI job-step summaries were inspected only as existing evidence; no workflow, tests, provider calls, deployment, billing, credential/secret, runtime-code, or repository-setting change was made.
- No backup/archive path was accessed or modified as part of this batch.
- Scope remains proposed and not human-approved.
