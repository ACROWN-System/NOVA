# ISO 704:2022 Semantic Review — Batch 042 (Context-Packing Evidence)

**Review ID:** NOVA-ISO704-SEM-B042  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Context-packing plan, implementation, synthetic corpus, benchmark runner and tests  
**Boundary:** This review does not execute code or tests, validate the workload independently, or assess any ISO clause.

## 1. Method

Each source was reviewed in full against its exact main-branch blob SHA. The review checks concept/status terms, provenance/temporal labels, test coverage and whether the benchmark's stated acceptance condition is enforced by its comparator. It is AI-assisted and preliminary; human validation remains mandatory.

## 2. File-by-file review

### B042-01 — Active-path context-packing workload record
- **Path:** `development/audit/Active/2026-10-11-Context-Packing-Benchmark-Workload.md`
- **Blob SHA:** `1c9a246caf54ea122028a483790aef55307c8a17`
- **Disposition:** `PRELIMINARY_REVIEW_COMPLETED_WORKLOAD_PLAN_MISCLASSIFIED_AS_ACTIVE`
- **Assessment:** The record explicitly labels itself COMPLETED and an archival mirror, but remains in `development/audit/Active/`. It also preserves a historical statement that NOVA's context/memory subsystem has no executable context-packing implementation, although a context-packer source file now exists. This is consistent with a dated archival mirror, not a trustworthy current-state statement.
- **Action:** Track the lifecycle/path/source-of-truth decision under SWEEP-F-0012. The file was not moved or edited; no archive/backup path was changed.

### B042-02 — Context-packer implementation candidate
- **Path:** `development/nova-context-memory-optimization/context_packer.py`
- **Blob SHA:** `1b117031cf024b68281583775a92ddf2a826c243`
- **Disposition:** `PRELIMINARY_REVIEW_CONTEXT_PACKING_RECORD_AND_PROVENANCE_TERMS`
- **Assessment:** Its module docstring explicitly says “development-stage implementation candidate.” The API preserves whole content and supplies IDs, sources, observation timestamps and status labels. It rejects duplicate IDs, invalid metadata and malformed budgets. These are appropriate data-integrity/terminology boundaries, but they do not prove deployment, independent benchmark approval or overall RSI readiness.

### B042-03 — Context-packing synthetic cases
- **Path:** `development/nova-recursive-self-improvement/benchmarks/context-packing-cases.json`
- **Blob SHA:** `31a724ddb9c14f5f9b79fc6f175dfe7c4ceca369`
- **Disposition:** `PRELIMINARY_REVIEW_SYNTHETIC_CORPUS_SCOPE_AND_LABELS`
- **Assessment:** The corpus labels itself fixed, synthetic and non-sensitive; it covers provider rotation/cursor persistence, timestamped supersession and RSI readiness/isolation caveats. Each case defines required IDs and a hard character budget. The file is a three-case illustration; adequacy, representativeness and independent validation remain separate questions.

### B042-04 — Context-packing benchmark runner
- **Path:** `development/nova-recursive-self-improvement/benchmarks/run_context_packing_benchmark.py`
- **Blob SHA:** `fc0f3266d5c02410bccf24f728cf9d23f1444a50`
- **Disposition:** `PRELIMINARY_REVIEW_BENCHMARK_REQUIRED_ITEM_REGRESSION_GAP`
- **Assessment:** The runner requires 40-character lowercase commit SHAs, loads baseline/candidate sources only from the expected `/benchmark-input` snapshot paths, validates exact full-record rendering, provenance, selected/dropped IDs and hard budget, and compares per-case results.
- **Finding B042-F01 / SWEEP-F-0014:** The comparator labels `no_per_case_required_evidence_regression` based on comparing only the **count** of required hits per case. It does not compare the identity of each required item against the baseline, nor does it explicitly require all `required_item_ids` to be selected by the candidate. A candidate could lose a specific required record but retain the same number of required hits, and the equality-of-count test could treat that as no regression. This fails to fully enforce the stated no-required-evidence-loss rule.
- **Required action:** Make the decision set-aware: for each case, record missing required IDs and fail/return not-better if any mandatory item is absent; also compare baseline/candidate required-ID sets so a substitution cannot hide a loss. Add negative tests for same hit count but different required item identity, and for a candidate that misses a required ID while improving other metrics. No code was modified in this content-review batch.

### B042-05 — Context-packing benchmark tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_context_packing_benchmark.py`
- **Blob SHA:** `5df270cf6b71b42378fa1d68167820487fc0cd81`
- **Disposition:** `PRELIMINARY_REVIEW_BENCHMARK_REGRESSION_TEST_COVERAGE_GAP`
- **Assessment:** Tests cover current packer output, expected required-record coverage, determinism, provenance/full-content preservation, zero budget, duplicate IDs, metadata line breaks and invalid budgets. The comparator test uses the real first-fit/current packer pair and does not exercise an intentionally defective candidate that keeps the same hit count while dropping a specific required item.
- **Finding:** The tests do not currently demonstrate that the benchmark comparator rejects the set-substitution scenario identified in B042-F01.

## 3. Findings

### SWEEP-F-0014 — Benchmark comparator can measure required-hit counts without enforcing required-item identity
- **Status:** OPEN — benchmark validity/control gap.
- **Affected paths:** `development/nova-recursive-self-improvement/benchmarks/run_context_packing_benchmark.py`; `development/nova-recursive-self-improvement/tests/test_context_packing_benchmark.py`.
- **Expected condition:** A candidate cannot be accepted if it drops a specific required evidence record, even when an aggregate/per-case hit count is unchanged or another metric improves.
- **Observed condition:** The comparator compares required-hit counts and unrequired-item counts; it does not currently assert that the selected candidate IDs contain every required ID or that the candidate preserves the baseline's required-ID set.
- **Risk:** A candidate can receive a favourable aggregate result despite substituting a different required record for a mandatory one; acceptance would not fully match the protocol's no-required-evidence-loss claim.
- **Remediation:** Update comparator result schema and decision rule to identify missing required IDs, require complete required-ID coverage where corpus semantics define each item as mandatory, preserve baseline required IDs, and return candidate_better=false (or BLOCKED/FAIL according to the protected contract) on a loss. Add synthetic negative cases and regression tests.
- **Closure evidence:** a reviewed code-change PR, passing targeted/full tests, retained negative-case output demonstrating rejection, and re-check that benchmark stays disabled/unapproved until independent review.

## 4. Counts and limitations

- Five files received preliminary full-file content reviews; human validation required.
- Tracker counts after this batch: **126 preliminary full-file reviews + 5 partial screens + 187 not reviewed = 318 active paths**.
- Formal ISO 704 clause-level assessments completed: **0**.
- No code or tests were run; no benchmark was executed.
- The active-path workload plan remains untouched pending the human lifecycle decision under SWEEP-F-0012.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Initial five-file preliminary review; recorded SWEEP-F-0014. This is not an ISO 704 clause assessment.
