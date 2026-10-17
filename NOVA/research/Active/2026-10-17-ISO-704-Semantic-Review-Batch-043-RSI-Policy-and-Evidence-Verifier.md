# ISO 704:2022 Semantic Review — Batch 043 (RSI Policy and Evidence Verifier)

**Review ID:** NOVA-ISO704-SEM-B043  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Protected RSI policy, evaluator, benchmark dispatcher, benchmark profile registry and evidence verifier  
**Boundary:** Not a runtime/security test, independent reviewer assessment, formal ISO 704 clause assessment, or certification decision.

## 1. Method

The complete source of each file was reviewed against the exact AstroCrown-Web main-branch blob SHA listed below. This assessment examines documented control/status boundaries, the relationship between policy and evidence checks, and whether language distinguishes provenance from capability/independent approval. It is AI-assisted and preliminary. No source code, secret, workflow setting, registry status or policy gate was changed, and no test/runtime operation was executed in this batch.

## 2. File-by-file review

### B043-01 — Protected RSI policy
- **Path:** `development/nova-recursive-self-improvement/rsi_policy.json`
- **Blob SHA:** `4ac2ce509d6ab7cca41fe1cdaa04a04a0ac81e32`
- **Disposition:** `PRELIMINARY_REVIEW_PROTECTED_STATUS_AND_AUTHORITY_BOUNDARIES`
- **Evidence:** The policy keeps `implementation_readiness.status = INCOMPLETE`, requires explicit READY, blocks promotion until readiness, disables direct-main promotion/automatic merge, separates manual report-only Weak RSI from Strong RSI, and states Strong RSI is SUSPENDED with zero provider calls allowed during suspension and a requirement for explicit human release.
- **Conclusion:** These are clear stated authorization/status boundaries. This review did not assess repository settings or execute the policy.

### B043-02 — Protected evaluator
- **Path:** `development/nova-recursive-self-improvement/evaluator.py`
- **Blob SHA:** `4e0c6f26a6359a30c65ac6aa80930750cca735a6`
- **Disposition:** `PRELIMINARY_REVIEW_EVALUATION_GATE_AND_STATUS_SEMANTICS`
- **Evidence:** The evaluator checks protected readiness before candidate evaluation; records baseline/candidate commit and tree identity; checks candidate scope, deletion, unsafe modes and configured secret patterns; runs candidate-controlled compile/tests through the sandbox; and requires a benchmark result. Benchmark output must be an object with boolean `candidate_better` and exact baseline/candidate commit identifiers.
- **Dependency:** A structurally valid result with the right SHAs still depends on the benchmark runner's semantics. The previously documented SWEEP-F-0014 gap—comparing required-hit counts without guaranteeing mandatory required-item identity—therefore remains material until code and negative tests are fixed.
- **Limitations:** No tests or runtime were run.

### B043-03 — Task-specific benchmark dispatcher
- **Path:** `development/nova-recursive-self-improvement/benchmark_dispatcher.py`
- **Blob SHA:** `5ac09ddeec0528e11120895841c85a7a015f3895`
- **Disposition:** `PRELIMINARY_REVIEW_FAIL_CLOSED_TASK_SCOPE_DISPATCH`
- **Evidence:** The dispatcher checks registry schema and registry-level approval, safely validates paths, requires a unique exact changed-file-set match, then checks explicit profile-level independent-review status, enabled state and exact command equality. Unknown, mixed, malformed, unapproved and disabled profiles produce BLOCKED.
- **Limitations:** The function's content and reported tests were reviewed; no tests were executed.

### B043-04 — Benchmark profile registry
- **Path:** `development/nova-recursive-self-improvement/benchmark_profiles.json`
- **Blob SHA:** `ee91f84a7afe2e6f1bfe733838bc7a84b6ed6a5e`
- **Disposition:** `PRELIMINARY_REVIEW_BENCHMARK_PROFILE_REMAINS_CANDIDATE`
- **Evidence:** The registry is explicitly `CANDIDATE_REGISTRY_NOT_INDEPENDENTLY_APPROVED`; its only profile is context-packing-only, disabled, and marked `BLOCKED_PENDING_INDEPENDENT_BENCHMARK_AND_EXECUTION_REVIEW`. The profile expressly disclaims general-intelligence scope.
- **Dependency:** Keep it disabled and unapproved until SWEEP-F-0014 is remediated, the workload/corpus is independently assessed, and execution isolation is independently reviewed. No registry state was changed.

### B043-05 — Evidence verifier
- **Path:** `development/nova-recursive-self-improvement/evidence_verifier.py`
- **Blob SHA:** `e6e184b78e062615a464fe4f75644757686f9b2d`
- **Disposition:** `PRELIMINARY_REVIEW_MANIFEST_COMMIT_TREE_AND_BUDGET_GATES`
- **Evidence:** It verifies the exact allowed evidence manifest/file inventory and SHA-256 hashes; rejects symlink/non-regular evidence; requires the trusted policy to be READY; binds cycle/evaluator baseline, candidate commit and candidate tree identities; validates candidate payload, patch, protected path/content and changed-file set; requires the exact expected set of evaluator checks all to PASS; and validates proposer telemetry and cycle budgets. The applied-worktree check compares paths/modes and the staged tree to the expected candidate tree.
- **Boundary:** These checks support artifact/provenance integrity. They do not alone establish that the benchmark is scientifically/operationally valid or that a qualified reviewer independently approved it. The verifier itself documents an external approval requirement through the other controls. No executable tests were run.

## 3. Findings

No new unique finding was added by this batch. The reviewed sources consistently express the intended fail-closed states and explicit separation between implemented verification mechanics and independent approval. The major cross-file dependency SWEEP-F-0014 remains open: evaluator/verifier integrity cannot compensate for a benchmark that does not enforce its stated mandatory evidence-item semantics.

## 4. Counts and limitations

- Five files received preliminary full-file reviews; human validation remains required.
- Tracker counts after this batch: **131 preliminary full-file reviews + 5 partial targeted screens + 182 not reviewed = 318 active paths**.
- Formal ISO 704 clause-level assessments completed: **0**.
- No code/tests, provider call, workflow, credential, registry setting or readiness flag was changed or executed in this review.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Initial five-file preliminary content review; no new unique finding. This is not a formal ISO 704 clause assessment.
