# ISO 704 Semantic Review Batch 073 — Strong RSI Readiness and Test-Outcome Terminology

**Document ID:** NOVA-ISO704-SEM-B073  
**Review date:** 2026-10-18  
**Baseline repository:** `ACROWN-System/AstroCrown-Web`  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Scope:** Strong RSI status, benchmark dispatcher tests, cycle detector tests, evaluator tests, and Weak RSI report tests, all retrieved at the pinned baseline and matched against tracker SHAs.  
**Review status:** Preliminary full-file semantic review; human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report makes no ISO 704 conformity or nonconformity claim.

## Review method and limits

The five complete documents/source files were read statically at their recorded blob SHAs. The review focused on distinctions among lifecycle status, implementation readiness, gate decision, benchmark result, test result, workflow-run outcome, credential presence, provider eligibility, report-only operation, and actual capability improvement. The tests were reviewed as specifications of intended behavior; they were not executed. No source/runtime files, test runs, workflows, credentials, provider calls, billing, repository settings, or backup/archive paths were changed, executed, or inspected.

## Source manifest and dispositions

| # | Source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B073-01 | `development/nova-recursive-self-improvement/STRONG-RSI-STATUS.md` | `c22c27a98ed4e1567423e952aedad0aa64d1c5db` | Preliminary review; no unique finding; preserves suspended/incomplete status and reactivation gates. |
| B073-02 | `development/nova-recursive-self-improvement/tests/test_benchmark_dispatcher.py` | `52cc5c05dd1e7099ec0a988523433ed96f67d9db` | Preliminary static review; no unique terminology finding. |
| B073-03 | `development/nova-recursive-self-improvement/tests/test_cycle_detector.py` | `6a7f5bf020284967599747379eba140acff8a70d` | Preliminary static review; extends SWEEP-F-0052 because tests explicitly include failed workflow-run records while naming record intervals “cycle length in passes”. |
| B073-04 | `development/nova-recursive-self-improvement/tests/test_evaluator.py` | `893e01fbc918a71fdd0257f1a6f01f55fe659499` | Preliminary static review; no unique finding; mocked integration-test scope is retained as a limitation. |
| B073-05 | `development/nova-recursive-self-improvement/tests/test_weak_rsi_report.py` | `a6b4e3440554701b3d47f00e8356c3f78306e898` | Preliminary static review; no unique terminology finding. |

## File-level review notes

### B073-01 — Strong RSI Status

The document distinguishes lifecycle status `SUSPENDED` from implementation readiness `INCOMPLETE`, identifies the inactive workflow template's location outside active GitHub Actions workflow discovery, and states that no Strong RSI provider call, cycle, candidate generation/execution, branch, or PR should be initiated during suspension. It also separates repository-scoped credential states from readiness and requires them to be freshly rechecked. A non-empty secret is not treated as sufficient.

The reactivation criteria distinguish capability readiness, provider readiness, data-use/commercial eligibility, independently approved task benchmark, sandbox integrity, zero mandatory regressions, evidence integrity, retention permissions, human review, operational proof, and public-claim scope. A valid `NO_CHANGE` result is not characterized as an improvement patch or candidate PR. These are positive concept-boundary and lifecycle safeguards. No unique finding was opened.

### B073-02 — Benchmark Dispatcher Tests

The tests use a clear decision vocabulary: `READY` for a matching enabled and independently reviewed profile; `BLOCKED` for disabled or unapproved profiles, wrong/missing commands, mixed/ambiguous scope, malformed registries, traversal/duplicate paths, and invalid fields. The tests exercise exact changed-path scope and command matching instead of treating the presence of a benchmark profile as enough.

The source is test code, and those labels represent the dispatcher outcome rather than the Strong RSI release decision. This review records the test scope and does not infer production readiness or claim that a test run occurred. No unique terminology finding was opened.

### B073-03 — Cycle Detector Tests

Tests distinguish exact full-state repetition (`REPEATED_STATE`) from component-level repetition and from `NO_REPEAT_IN_WINDOW`; malformed or incomplete evidence raises `DiagnosticUnavailable`, and API failure must produce `UNAVAILABLE`, not an asserted no-repeat. A positive-control test explicitly ensures the report does not claim that no repeat proves improvement.

Importantly, the recent-runs test includes scheduled/manual main-branch runs whose recorded conclusions are `failure`, and expects those records to remain in the selected history. This establishes that the existing tested behavior intentionally includes failed runs rather than filtering only successful runs. It also strengthens the terminology concern in SWEEP-F-0052: the index distance is a count of included workflow-run records, whereas `cycle_length_passes`/“RSI pass(es)” may imply completed or successful RSI cycles. The correct resolution is to name the measured unit accurately or explicitly define a different eligibility rule—not to assume the tests should exclude failures.

### B073-04 — Evaluator Tests

The tests distinguish `BLOCKED` readiness from a decision `PASS`; verify exact candidate commit/tree evidence; reject non-boolean benchmark claims and mismatched baseline/candidate commit identifiers; require strict candidate-better semantics in the benchmark test scenario; and test secret-stripping/path-validation controls. The integration test that asserts a `PASS` supplies a mocked benchmark result, so that individual test establishes evaluator handling of the return contract, not independent benchmark validity or end-to-end improvement. Other focused tests cover parsing and the benchmark path. That boundary is inherent to the isolated test setup and is recorded as a positive clarification rather than a defect.

No evaluator or test was executed; conclusions are limited to reading the assertions and fixtures.

### B073-05 — Weak RSI Report Tests

The tests distinguish `BLOCKED` from `HUMAN_REVIEW_REQUIRED`, verify zero provider calls when data-use eligibility is not approved or the selected provider's credential is missing, and verify that a successful provider response still produces a report-only human-review outcome with no source changes, candidate execution, PR creation, or merge. Provider choice is allowlisted and does not silently fall back to another provider. The allowlisted context-reader test distinguishes permitted public development notes from a local `.env` secret.

These assertions make credential presence, use eligibility, provider-call count, report outcome, human review, candidate execution, and merge state distinct. No unique terminology finding was opened.

## Findings and traceability updates

1. **SWEEP-F-0052 — Cycle diagnostic labels workflow-run intervals as “RSI passes” without defining eligible pass outcomes:** Extend affected paths to `development/nova-recursive-self-improvement/tests/test_cycle_detector.py`. Its recent-runs test explicitly includes failed scheduled/manual runs in the history and expects them to be retained. This confirms that the current test contract counts selected workflow-run records, not only successful runs. The terminology therefore needs to name that measured unit or the project must define a different eligibility rule; this finding does not assert that including failed records is wrong.
2. **No additional unique finding was opened.** The other four reviewed files preserve useful separation among lifecycle, eligibility, decisions, evidence quality, and report-only behavior.

## Batch disposition and counts

After recording these five full-file preliminary reviews, the row-derived sweep target is:

- Active files inventoried: **318**
- Preliminary full-file reviews: **281**
- Partial targeted screens: **5**
- Not yet reviewed: **32**
- Human validation of preliminary reviews: **pending**
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: **proposed; human approval pending**

Arithmetic check: 281 + 5 + 32 = 318.

No source/runtime files, backup/archive paths, tests, workflows, credentials, providers, billing, or repository settings were changed or used. The findings remain preliminary and human validation is required; this is not a formal ISO 704 clause assessment or conformity statement.
