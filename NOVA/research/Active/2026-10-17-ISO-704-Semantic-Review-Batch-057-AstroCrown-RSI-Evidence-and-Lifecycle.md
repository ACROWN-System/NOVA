# Semantic Review Batch 057 — AstroCrown RSI Evidence and Lifecycle

**Document ID:** NOVA-ISO704-SEM-B057  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR's head.  
**Purpose:** Preliminary semantic, evidence-provenance and documentation-lifecycle review. This is not a formal ISO 704 clause assessment, a new RSI security audit, or permission to change RSI readiness.

## 1. Target manifest and source identity

| ID | Exact source path | Source commit | Verified blob SHA | Disposition |
|---|---|---|---|---|
| B057-01 | `development/audit/Active/2026-10-11-RSI-Evidence-Commit-Binding.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `90ed9f9be95c7e17697cf5cb1db07c3452faa179` | SWEEP-F-0031 |
| B057-02 | `development/audit/Active/2026-10-11-RSI-Evidence-Retention-Verification.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `e9ce657f87da60b3c1f262980ca9047ff4c021b6` | SWEEP-F-0012 |
| B057-03 | `development/audit/Active/2026-10-11-RSI-Executable-Mode-Consistency.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `16a77ef07ae7bb3304481878985ff3c5ff4a6fc6` | SWEEP-F-0012 |
| B057-04 | `development/audit/Active/2026-10-11-RSI-Finalizer-CLI-Smoke.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `074af08c48a2169662a387c84a965a2ac2f4f5fa` | SWEEP-F-0031 |
| B057-05 | `development/audit/Active/2026-10-11-RSI-GitHub-Action-SHA-Pinning.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `dc53b6dcb0302cda535b147b3cb8185c94253537` | SWEEP-F-0012 |

All five returned blob SHAs match their tracker rows exactly. No target source file was changed by this sweep.

## 2. Semantic review results

### B057-01 — RSI evidence commit-binding navigation plan

The plan defines a provenance contract: cycle and protected evaluator records must use supported integer schema versions, and the evaluator's exact full candidate commit SHA must match the cycle report. It explicitly distinguishes matching provenance fields from proof that benchmark results are valid. Its scope excludes changing readiness, promotion permissions, provider calls, credentials, billing or workflow permissions.

AstroCrown-Web [PR #81 — bind evaluator evidence to exact candidate commit](https://github.com/ACROWN-System/AstroCrown-Web/pull/81) merged on 2026-10-10 23:35:03 UTC. The PR's changed-file list includes this active navigation plan and the evaluator/verifier/test changes. The workflow run associated with the PR head, [run #38095491875](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38095491875), is recorded as completed successfully; its job-step listing reports success for immutable sandbox-image verification, Python compilation, RSI unit tests and Docker isolation-boundary exercise. These are retrieved historical CI records; this review did not rerun them.

The plan still says `ACTIVE — strict evidence schema and candidate-commit binding under verification`. This is a plausible documentation-task lifecycle mismatch after the plan's own PR and its recorded acceptance run completed. It is not evidence that RSI itself is ready: the reviewed plan explicitly keeps `implementation_readiness.status = INCOMPLETE`, `promotion.allow_main = false`, and the production benchmark/profile disabled or unapproved.

**Disposition:** extend SWEEP-F-0031, with a human to confirm the canonical completion destination and closure metadata. Do not change RSI readiness or promotion gates.

### B057-02 — RSI evidence-retention verification completed audit mirror

The record identifies itself as a completed audit, explicitly calls the Active-path copy an archival mirror, and links the canonical Completed record. It preserves the important distinction between validating a downloaded evidence artifact and independently rechecking the applied worktree before staging. It also records residual limits: a SHA-256 manifest is not a producer-authenticating digital signature, and retention remains unreachable while readiness is INCOMPLETE.

AstroCrown-Web [PR #67 — verify RSI evidence before candidate retention](https://github.com/ACROWN-System/AstroCrown-Web/pull/67) is merged. Its associated [CI run #38090681978](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38090681978) is recorded completed successfully. The source path remains under `Active/` while the record itself declares COMPLETED and links `../Completed/2026-10-11-RSI-Evidence-Retention-Verification.md`.

**Disposition:** cross-reference SWEEP-F-0012. The existing human scope decision remains necessary; this review does not move, rename or delete the mirror.

### B057-03 — RSI executable-mode consistency completed navigation-plan mirror

The record explicitly says COMPLETED, labels itself an archival mirror and links a canonical Completed record. Its control distinction is bounded: rejecting executable candidate files aligns evaluator checks with retention checks; it does not imply RSI promotion is enabled.

AstroCrown-Web [PR #72 — reject executable candidate files during evaluation](https://github.com/ACROWN-System/AstroCrown-Web/pull/72) is merged, and associated [CI run #38093982235](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38093982235) is recorded completed successfully. The changed-file list for [PR #73 — archive RSI security follow-up verification](https://github.com/ACROWN-System/AstroCrown-Web/pull/73) includes both the Active-path file and a Completed-path counterpart. The tracked baseline still contains the reviewed record beneath `Active/`.

**Disposition:** cross-reference SWEEP-F-0012. No source relocation or update is authorized by this finding.

### B057-04 — Workflow cleanup CLI smoke-test navigation plan

The plan differentiates invoking the exact standalone cleanup CLI from testing the underlying cleanup helper, and requires an independent Docker-label inventory check after the CLI succeeds. It also preserves the fail-safe cleanup attempt on errors and keeps readiness/provider/credential/permission settings out of scope.

AstroCrown-Web [PR #79 — exercise workflow cleanup CLI in a real Docker smoke test](https://github.com/ACROWN-System/AstroCrown-Web/pull/79) merged on 2026-10-10 23:28:55 UTC; its changed-file list includes this plan, the cleanup runtime and tests. The associated [CI run #38095122426](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38095122426) is recorded completed successfully; the job-step listing reports success for immutable image verification, compilation, the RSI unit-test step and Docker isolation-boundary exercise. The record nevertheless remains `ACTIVE — end-to-end cleanup CLI smoke coverage under verification`.

**Disposition:** extend SWEEP-F-0031 as an apparent navigation-plan lifecycle issue. Human review should confirm that the recorded PR/run satisfy the repository's intended closure convention before any lifecycle change. No tests or workflows were executed by this sweep.

### B057-05 — Immutable GitHub Actions references completed audit mirror

The record labels itself a completed audit and archival mirror, links a canonical Completed record, and records the specific immutable full commit SHAs used for third-party Actions. It also keeps the limitation clear: pinning makes consumed revisions explicit but does not prove the pinned upstream code is vulnerability-free.

AstroCrown-Web [PR #68 — pin GitHub Actions to verified commit SHAs](https://github.com/ACROWN-System/AstroCrown-Web/pull/68) is merged. Its associated [CI run #38090761808](https://github.com/ACROWN-System/AstroCrown-Web/actions/runs/38090761808) is recorded completed successfully. This reviewed path still resides under `Active/` despite its explicit completed-mirror status and canonical Completed link.

**Disposition:** cross-reference SWEEP-F-0012; no source move or edit pending the existing human decision.

## 3. Existing findings updated

### SWEEP-F-0031 — Navigation-plan lifecycle state remains Active after associated PRs merge

Batch 057 adds two further examples where the source plan remains explicitly Active after its own PR included the plan and the associated CI run is recorded successful: the evidence-commit-binding plan in PR #81, and the finalizer-CLI smoke plan in PR #79. The run records show the expected verification steps completed, but the scope/lifecycle decision still belongs to a human maintainer. These examples are distinguished from PR #84's canonical-candidate-path validation plan, which Batch 056 kept out of this finding because full acceptance was not independently established.

This finding concerns document lifecycle only. It does not authorize changing product architecture, readiness state, benchmark approval, promotion policy or workflow permissions.

### SWEEP-F-0012 — Completed archival mirrors under Active

Batch 057 adds three more explicit completed mirrors under `development/audit/Active/`: evidence-retention verification, executable-mode consistency, and GitHub Action SHA pinning. Each identifies a canonical Completed record; their associated PR/CI records are documented in this report. The Active-path copies remain untouched pending the existing human scope decision.

## 4. Counts, limits and safety boundary

- Row-derived post-batch counts: **201 preliminary full-file reviews + 5 partial targeted screens + 112 not reviewed = 318 active paths**.
- Human validation remains pending for all 201 preliminary full-file reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- The five source files were fetched at exact baseline paths and their returned blob SHAs matched the tracker.
- Historical PR/CI metadata was read for lifecycle/evidence context; no workflow, tests, provider calls, deployment, billing, credentials, secrets, runtime code, repository settings or source files were changed.
- No backup/archive directories were inspected or modified as part of this batch.
- Scope remains proposed and not human-approved.
