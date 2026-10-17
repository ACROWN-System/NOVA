# Semantic Review Batch 062 — AstroCrown Completed RSI Security Records

**Document ID:** NOVA-ISO704-SEM-B062  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Purpose:** Review terminology clarity, temporal/status consistency, evidence boundaries and the distinction between implementation evidence and independent readiness approval. This is not a formal ISO 704 clause assessment, independent security approval, or RSI authorization.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B062-01 | `development/audit/Completed/2026-10-11-Open-Source-Licensing.md` | `843b94ae69fdb26cefa4009a1e52df2407e0688e` | No unique finding |
| B062-02 | `development/audit/Completed/2026-10-11-RSI-Docker-Isolation.md` | `b0c1ac8bf0bc94ae2d119f93f38437f1b11d2718` | SWEEP-F-0034 |
| B062-03 | `development/audit/Completed/2026-10-11-RSI-Evidence-Retention-Verification.md` | `19693a0124ffec3c2eca1bca03d6d6fb86dfb247` | No unique finding |
| B062-04 | `development/audit/Completed/2026-10-11-RSI-GitHub-Action-SHA-Pinning.md` | `310d350066abb804856a69405eb85d75bf1d8b5a` | No unique finding |
| B062-05 | `development/audit/Completed/2026-10-11-RSI-Independent-Review-Package.md` | `03458d8f22cb29367835db6c3dff106f3dc120ba` | No unique finding |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. Source files were read only and remain untouched.

## 2. Semantic review results

### B062-01 — Open-source licensing

The completed plan distinguishes the MIT software license from AstroCrown/NOVA/HAAN brand identifiers and third-party/file-specific materials. It avoids implying that the software license grants trademark rights or relicenses third-party assets. The plan records the different verification boundaries for the two repositories: AstroCrown-Web PR #104 and NOVA PR #70 were recorded as merged, and the plan explicitly says no NOVA checks were triggered for the root-only license/README edits rather than claiming tests passed. Current GitHub metadata independently confirms both PRs merged.

**Disposition:** no unique finding. The source's dated historical verification does not establish legal rights to any third-party material beyond the stated license boundaries.

### B062-02 — Docker isolation candidate

The plan properly distinguishes OS-level container isolation from a sanitized environment/detached worktree, and it records explicit controls including immutable image identity, no network, read-only mounts, non-root execution, dropped capabilities, resource/time limits and bounded output. It also avoids treating Docker as perfect protection from kernel/runtime/supply-chain risk, retains the task-specific/unapproved benchmark limitation, and keeps protected RSI readiness `INCOMPLETE` with `promotion.allow_main = false`. AstroCrown-Web PR #58 is confirmed merged in live GitHub metadata.

However, the section headed **Current findings** still says that the evaluator executes compilation, unit tests and the configured benchmark as host subprocesses. Later in the same completed record, the execution outcome says the Docker adapter was merged and candidate-controlled commands use that fail-closed adapter. The record's top-level status and execution outcome make the chronology inferable, but the explicit word “Current” can be read as a claim about the current implementation. This review did not inspect or execute current RSI source, so it cannot establish any implementation regression.

**Disposition:** SWEEP-F-0034, preliminary temporal-label clarity issue only. Human maintainers should either label the section as the pre-change/baseline finding or add its observation revision/date. Do not infer a runtime defect, change readiness, or rerun CI as part of this content review.

### B062-03 — Evidence verification before retention

The document describes the original retention-boundary gap as finding RSI-SEC-008, then records that the verifier was implemented and merged in AstroCrown-Web PR #67. The execution outcome describes checks before patch application and again before staging, with a worktree recheck and protected readiness still `INCOMPLETE`. It records that the unified-diff parser defect was fixed and describes CI as passing 79 RSI unit tests and isolation checks. Importantly, the residual-risks section distinguishes a SHA-256 manifest from a producer-authenticating digital signature.

Live GitHub metadata confirms PR #67 merged. No tests were rerun for this sweep, and prior results are reported as historical evidence only.

**Disposition:** no unique finding. The initial `RSI-SEC-008` section is treated as the documented original problem statement; the later execution outcome records remediation rather than live status.

### B062-04 — Immutable GitHub Actions references

The record explains the risk of mutable major-version tags and lists full action commit SHAs with human-readable tags, dated official-ref verification, and the intended workflow scope. It records AstroCrown-Web PR #68 as merged, preserves the need to re-verify future action updates, and does not treat pinning as proof that upstream actions are vulnerability-free.

Live GitHub metadata confirms PR #68 merged. The finding section uses a present-tense statement about the pre-change moving-tag problem, but it is explicitly framed under historical finding ID RSI-SEC-009 and is followed by a specific execution outcome describing the pinning change. This is less ambiguous than the `Current findings` heading in B062-02 and is not separately raised.

**Disposition:** no unique finding.

### B062-05 — Independent RSI readiness review package

The document distinguishes completion of the review package from completion of the independent review itself. It marks the latter `BLOCKED`, records limits in the exact final-tree CI coverage, and retains `implementation_readiness.status = INCOMPLETE`, `promotion.allow_main = false`, and the disabled/unapproved benchmark. AstroCrown-Web PR #87 is confirmed merged in live GitHub metadata; merge of the package is not represented as independent approval.

**Disposition:** no unique finding. The reviewer dependency and protected readiness boundaries remain open; no RSI cycle, provider call, test or workflow was run here.

## 3. New finding

### SWEEP-F-0034 — Completed Docker isolation record labels pre-change behavior as current

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/audit/Completed/2026-10-11-RSI-Docker-Isolation.md`.
- **Observed issue:** The `Current findings` section states that the evaluator executes candidate-controlled commands as host subprocesses, while the same completed record later says the Docker isolation implementation was merged and that those commands use the fail-closed adapter. The record does not explicitly label that section's observations as the pre-change baseline.
- **Interpretation:** This is a potential temporal/status wording ambiguity. It is not evidence that the current source regressed or that the recorded implementation/CI results are false.
- **Required action:** A human maintainer should label the section as a pre-change finding or bind it to the relevant pre-change revision/date, preserving the original finding for audit traceability and the separate residual-risk/independent-review blocker.
- **Closure evidence:** Reviewed wording with an explicit baseline reference and confirmation that top-level status, execution outcome, residual risks, and current readiness limitations remain distinguishable.
- **Safety boundary:** No source, runtime, workflow, test, credential, provider configuration, billing, repository setting or backup/archive path was changed. No test/workflow was executed.

No other new finding ID was opened. Existing records correctly distinguish completed documentation/implementation tasks from still-blocked independent review and RSI readiness.

## 4. Counts, limits, and safety boundary

- Row-derived post-batch counts: **226 preliminary full-file reviews + 5 partial targeted screens + 87 not reviewed = 318 active paths**.
- Human validation remains pending for all 226 preliminary reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- All five target blob SHAs match the exact recorded baseline entries.
- Related PR status metadata was checked for AstroCrown-Web PRs #58, #67, #68, #87 and licensing PRs AstroCrown-Web #104 / NOVA #70. Existing CI references were not rerun and are treated as historical evidence.
- No AstroCrown-Web source file, backup/archive path, runtime file, credential, provider configuration, repository setting or billing setting was changed. No RSI cycle, live provider request, test, workflow or deployment was executed.
- Scope remains proposed and not human-approved.