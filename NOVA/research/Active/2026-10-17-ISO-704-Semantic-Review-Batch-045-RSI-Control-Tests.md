# ISO 704:2022 Semantic Review — Batch 045 (RSI Control Tests)

**Review ID:** NOVA-ISO704-SEM-B045  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Engine, sandbox runtime, provider client, preflight and evidence-verifier tests  
**Boundary:** Source/test review only; no tests executed; not a formal ISO 704 clause assessment or independent security certification.

## 1. Method

The complete text of each test file was reviewed against the exact AstroCrown-Web main-branch blob SHA. The assessment checks whether tests cover the policy's declared states and failures, whether test definitions are actually discoverable, and whether mock tests are distinguished from end-to-end evidence. Human validation remains mandatory. No code or tests were changed or executed in this batch.

## 2. File-by-file review

### B045-01 — RSI engine tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_rsi_engine.py`
- **Blob SHA:** `c50985507ef0d0881d8073227560e6eef3f67f75`
- **Disposition:** `PRELIMINARY_REVIEW_ENGINE_NEGATIVE_TEST_GAP_AND_DUPLICATE_TEST_NAME`
- **Assessment:** The test file covers supervisor timeouts, bounded drain/reap and cleanup, patch/path validation, secret-pattern detection, usage limits, incomplete readiness and static Strong RSI suspension policy fields.
- **SWEEP-F-0015 coverage gap:** It does not construct a policy with `implementation_readiness.status = READY` while `strong_rsi_safety.lifecycle_status = SUSPENDED`, nor assert zero proposer/provider calls in that state.
- **SWEEP-F-0016:** The class defines `test_workflow_has_always_run_sandbox_cleanup_before_evidence_upload` twice. In a Python class, the second method definition replaces the first under the same name; unittest discovers only the second definition. The earlier version contains additional assertions for job/cycle timeout limits that are therefore not executed by that duplicate name.
- **Action:** Add adversarial lifecycle tests and give each workflow-boundary test a unique method name, then verify discovery output counts the intended tests. Do not claim any test passed from this source review.

### B045-02 — Sandbox runtime tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_sandbox_runtime.py`
- **Blob SHA:** `bdf3d87f01e64544c549a680d2b06a965e9cfa17`
- **Disposition:** `PRELIMINARY_REVIEW_SANDBOX_NEGATIVE_TESTS_AND_BOUNDED_CLEANUP`
- **Assessment:** Covers immutable image references, local-image ID mismatch, missing Docker without host fallback, sandbox environment allowlist, run/evaluation identifiers, expected container flags, timeouts and unconfirmed-cleanup failure. Many Docker interactions are mocked; local process-output test covers bounded capture.
- **Evidence boundary:** These unit tests do not alone demonstrate successful operation on the intended GitHub runner/host; actual host self-test and independent security review are separate gates.

### B045-03 — Provider client tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_provider_client.py`
- **Blob SHA:** `549d9e3f6556cbf7ad568621699e781d8ddc2872`
- **Disposition:** `PRELIMINARY_REVIEW_PROVIDER_URL_REDIRECT_AND_SECRET_TEST_COVERAGE`
- **Assessment:** A local HTTP server supports negative cases for remote HTTP, non-allowlisted hostname, embedded URL credentials, query/fragment, redirect handling and bearer credential non-forwarding. It also tests model discovery/chat usage and that a configuration representation does not expose the API key.
- **Evidence boundary:** Test design is useful, but this review does not validate actual live-provider behavior, TLS trust in production, or current credentials.

### B045-04 — Preflight tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_preflight.py`
- **Blob SHA:** `64c52ab1b3ab2fca74a15eaade6c10fb55a38f3f`
- **Disposition:** `PRELIMINARY_REVIEW_PREFLIGHT_LIFECYCLE_NEGATIVE_COVERAGE_GAP`
- **Assessment:** Covers current INCOMPLETE readiness, exact commercial-eligibility PASS, required benchmark command and rejection of an unapproved host.
- **SWEEP-F-0015 coverage gap:** No test proves an explicitly SUSPENDED lifecycle blocks before the provider-secret stage. One test builds a minimal policy with `implementation_readiness.status = READY` but no `strong_rsi_safety` state and then checks the absent-secret response; that test does not establish lifecycle enforcement.

### B045-05 — Evidence verifier tests
- **Path:** `development/nova-recursive-self-improvement/tests/test_evidence_verifier.py`
- **Blob SHA:** `02bb0dc3c530c0c553c5f8aeba89b367e931edb0`
- **Disposition:** `PRELIMINARY_REVIEW_EVIDENCE_VERIFIER_LIFECYCLE_TEST_GAP`
- **Assessment:** Provides meaningful negative cases for exact manifest schema/inventory/hash, commit/tree/baseline bindings, decision/PASS states, protected paths, symlinks, applied-path set, executable modes and expected tree.
- **SWEEP-F-0015 coverage gap:** The fixture policy tests only implementation readiness. It does not include Strong RSI lifecycle state and contains no candidate-retention test for `READY + SUSPENDED`. Because the verifier uses the engine's readiness predicate, lifecycle enforcement should be tested at this privilege boundary as well.

## 3. Findings

### SWEEP-F-0015 — Extend suspension enforcement across all privileged entry points and tests
Batch 045 confirms the finding applies to the shared engine readiness predicate and its callers, including the engine cycle, evaluator, preflight and evidence verifier. The existing tests do not cover the adversarial combination where implementation readiness is READY but the Strong RSI lifecycle is still SUSPENDED. This is a policy-enforcement/test-coverage blocker, not evidence that a provider call has occurred: current policy remains INCOMPLETE/SUSPENDED.

**Required closure evidence:** trusted fail-closed lifecycle predicate; preflight, cycle, evaluation and retention each reject suspended/unknown state before external calls or privileged writes; tests prove zero provider calls and no candidate retention in READY+SUSPENDED; existing status values remain INCOMPLETE/SUSPENDED until separate approval.

### SWEEP-F-0016 — Duplicate Python test method masks workflow assertions
- **Status:** OPEN — test validity/coverage.
- **Affected path:** `development/nova-recursive-self-improvement/tests/test_rsi_engine.py`.
- **Observed issue:** Same test method name is defined twice. Python class binding keeps the latter definition, so the first method's unique assertions are not part of the discovered test suite.
- **Risk:** Reported suite pass would not prove the omitted first-method assertions were executed.
- **Required action:** Rename/split both tests so the workflow-order test and stronger timeout-limit/job-configuration assertions have unique test IDs; verify collection output and run the tests in CI.
- **Closure evidence:** reviewed code change, test discovery output showing both tests, and passing CI on that change.

## 4. Counts and limitations

- Five files received preliminary full-file reviews; human validation remains required.
- Tracker counts after this batch: **141 preliminary full-file reviews + 5 partial targeted screens + 172 not reviewed = 318 active paths**.
- Formal ISO 704 clause-level assessments completed: **0**.
- No tests were executed in this review.
- No source file, policy value, secret, workflow or setting was changed.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Initial five-file test-content review; confirmed missing lifecycle negative coverage and duplicate test method. Not a formal ISO 704 clause assessment.
