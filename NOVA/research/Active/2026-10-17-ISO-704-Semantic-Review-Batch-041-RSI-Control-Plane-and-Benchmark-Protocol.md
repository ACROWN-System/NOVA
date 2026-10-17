# ISO 704:2022 Semantic Review — Batch 041 (RSI Control Plane and Benchmark Protocol)

**Review ID:** NOVA-ISO704-SEM-B041  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Five AstroCrown-Web completed engineering records and the active capability-benchmark protocol  
**Boundary:** Not an implementation retest, independent security assessment, formal ISO 704 clause assessment, or certification decision.

## 1. Method

Each document was reviewed in full against its exact main-branch blob SHA. The review checks term/status precision, internal consistency, evidence traceability, and the distinction between a tested control and broader security/capability approval. It is AI-assisted and preliminary; human validation remains required. No code or source document was changed, and no CI, runtime, provider, or benchmark operation was run.

## 2. File-by-file review

### B041-01 — Trusted RSI Evaluator and Main-Ref Guard
- **Path:** `development/audit/Completed/2026-10-11-RSI-Trusted-Evaluator-Control-Plane.md`
- **Blob SHA:** `6545789ebae789b88cbcc84e56fcaa6922e09b74`
- **Disposition:** `PRELIMINARY_REVIEW_TRUSTED_CONTROL_PLANE_AND_MAIN_REF_GUARD`
- **Assessment:** The historical record identifies two concrete control-plane issues: evaluating with candidate-controlled evaluator code and allowing non-main workflow dispatch toward a credential boundary. It records the intended trusted-control-directory separation and main-ref guard with specific PR/CI evidence. It explicitly says broader independent sandbox/security review remains BLOCKED and readiness stays incomplete.
- **Existing terminology dependency:** The record references the legacy HAAN mission; this is part of existing SWEEP-F-0001 and remains subject to HSIAN rollout.

### B041-02 — RSI Provider Credential Egress Boundary
- **Path:** `development/audit/Completed/2026-10-11-RSI-Provider-Egress-Boundary.md`
- **Blob SHA:** `5fa4eb9c9395e95c76d5be31ef444b14caa522df`
- **Disposition:** `PRELIMINARY_REVIEW_HISTORICAL_PROVIDER_EGRESS_BOUNDARY`
- **Assessment:** The record describes an exact host allowlist, URL validation, redirect rejection and secret-safe test evidence, and it states that no provider request was made during that work. Its “current approved host” is Nosana's `inference.nosana.com`, appropriate to the historical Oct 11 configuration but no longer the checked current provider policy/client configuration.
- **Disposition boundary:** Treat this as a dated historical configuration record, not a current operator instruction. The difference supports existing SWEEP-F-0009, which calls for the live implementation runbook to be reconciled. Do not rewrite historical facts to match a later provider migration.

### B041-03 — RSI Supervisor I/O Failure Cleanup
- **Path:** `development/audit/Completed/2026-10-11-RSI-Supervisor-IO-Failure-Cleanup.md`
- **Blob SHA:** `6ec4712f1ec2f89739b680b263aaa980214b3a8c`
- **Disposition:** `PRELIMINARY_REVIEW_BOUNDED_PROCESS_TERMINATION_AND_CLEANUP`
- **Assessment:** It documents specific output monitoring/time-out edge cases and describes bounded process-group termination plus labelled-container cleanup. It distinguishes confirmed termination/cleanup from uncertain state and leaves residual host/daemon/kernel/supply-chain risk explicit. Named CI evidence is historical and was not reproduced here.

### B041-04 — RSI Executable-Mode Consistency
- **Path:** `development/audit/Completed/2026-10-11-RSI-Executable-Mode-Consistency.md`
- **Blob SHA:** `3a0a1400b53c20608f2f27ebdb7e3eb317f26dea`
- **Disposition:** `PRELIMINARY_REVIEW_EXECUTABLE_FILE_MODE_INTEGRITY`
- **Assessment:** The record clearly distinguishes an executable-mode integrity check from general security assurance; it identifies a regression test for newly added executable files and ties the reported outcome to a dated CI run. It keeps the context-packing benchmark disabled and readiness incomplete.
- **Existing terminology dependency:** Legacy HAAN mission reference remains under SWEEP-F-0001.

### B041-05 — NOVA RSI Capability Benchmark Protocol
- **Path:** `development/nova-recursive-self-improvement/CAPABILITY-BENCHMARK-PROTOCOL.md`
- **Blob SHA:** `349680884b9163bc6babda5170399502843fc0a2`
- **Disposition:** `PRELIMINARY_REVIEW_BENCHMARK_SCOPE_AND_LIFECYCLE_WORDING`
- **Assessment:** The protocol clearly distinguishes code-execution success from capability improvement; requires exact baseline/candidate commits, strict JSON output, per-case regression constraints, protected dispatch and task-specific workload approval; and says the context-packing workload is narrow, disabled/unapproved and not a general-intelligence benchmark. It explicitly requires independent review and leaves `RSI_BENCHMARK_COMMAND` unconfigured.
- **Finding B041-F01 / SWEEP-F-0013:** One section says the first workload “is being developed,” while later sections say it is implemented as a candidate. That stale lifecycle wording can make the document's state unclear even though its overall readiness boundary is correct.
- **Required action:** Say consistently that the workload is implemented as an unapproved candidate and still requires independent review; do not confuse implementation completion with approval.

## 3. Findings

### B041-F01 / SWEEP-F-0013 — Benchmark protocol contains inconsistent lifecycle wording
- **Status:** OPEN — documentation clarity.
- **Affected path:** `development/nova-recursive-self-improvement/CAPABILITY-BENCHMARK-PROTOCOL.md`.
- **Observed issue:** The “Initial workload implementation candidate” section says a deterministic workload “is being developed,” but subsequent sections state that it is implemented and remains a candidate pending independent review.
- **Risk:** Readers may misunderstand whether the workload exists, or mistake its implemented status for approval.
- **Action:** Replace the outdated future-work phrasing with the precise status “implemented candidate / independent review required,” while preserving the disabled/unapproved state and the rule that it is not a universal benchmark.
- **Closure evidence:** reviewed wording change and repeat check that the benchmark remains disabled/unapproved and the command unconfigured.

## 4. Counts and limitations

- Five files received preliminary full-file reviews; human validation remains required.
- Tracker counts after this batch: **121 preliminary full-file reviews + 5 partial screens + 192 not reviewed = 318 active paths**.
- Formal ISO 704 clause-level assessments completed: **0**.
- No provider call, CI run, Docker test or benchmark was performed.
- The Nosana egress-boundary record is treated as dated historical evidence, not current provider configuration.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Initial five-file preliminary content review; added SWEEP-F-0013. This is not a formal ISO 704 clause assessment.
