# ISO 704:2022 Semantic Review — Batch 044 (RSI Engine, Sandbox and Provider Boundary)

**Review ID:** NOVA-ISO704-SEM-B044  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** RSI engine, Docker sandbox adapter, provider HTTP client, preflight and candidate schema  
**Boundary:** Not a live execution test, security certification, formal ISO 704 clause assessment, or certification decision.

## 1. Method

The full source content was reviewed against the exact AstroCrown-Web main-branch blob SHA recorded for each file. The focus was whether code-level control descriptions agree with the stated readiness/suspension policy and whether terms such as PASS, READY and SUSPENDED are backed by explicit gates. AI-assisted preliminary review only; designated human validation remains mandatory. No code, secrets, workflow, settings or policy values were changed, and no tests or provider requests were run.

## 2. File-by-file review

### B044-01 — RSI engine
- **Path:** `development/nova-recursive-self-improvement/rsi_engine.py`
- **Blob SHA:** `527fe3e05bded99bf0b6ece47b2fc2cc1a63bf8f`
- **Disposition:** `PRELIMINARY_REVIEW_ENGINE_READINESS_VS_SUSPENSION_GUARD`
- **Assessment:** Engine starts a cycle by checking `implementation_ready(policy)` and otherwise records BLOCKED before the proposer call. It also describes bounded call/attempt/token usage, payload/path/content validation, a detached candidate worktree, a trusted control-plane copy outside that worktree, supervised evaluator termination and labelled cleanup.
- **Finding B044-F01 / SWEEP-F-0015:** `implementation_ready(policy)` checks only `implementation_readiness.status == READY`, `require_explicit_ready == true`, and `promotion_blocked_until_ready == true`. It does not check `strong_rsi_safety.lifecycle_status` or `provider_calls_permitted_while_suspended`. If the readiness field were accidentally or improperly changed to READY while lifecycle remains SUSPENDED, the engine-level guard would not enforce the separate suspension field before a provider call.
- **Action:** Add a single authoritative fail-closed readiness predicate that checks both implementation readiness and the Strong RSI lifecycle/explicit release state, and require all provider-entry points to use it. Add negative tests for READY+SUSPENDED and for a nonzero/invalid suspended-call policy. Do not change policy to READY as a workaround.
- **Limitations:** No engine/tests or provider request were run; this is a source-inspection finding.

### B044-02 — Sandbox runtime
- **Path:** `development/nova-recursive-self-improvement/sandbox_runtime.py`
- **Blob SHA:** `de48f556f927d3831eb39a8125ac828e69162da9`
- **Disposition:** `PRELIMINARY_REVIEW_FAIL_CLOSED_DOCKER_BOUNDARY_WITH_RESIDUAL_RISKS`
- **Assessment:** Requires a SHA-256-pinned Python image and exact image-ID match; blocks if Docker/image verification fails; uses read-only mounts, no network, dropped capabilities, non-root UID, no-new-privileges, bounded resource/output limits and a restricted environment; and tries to stop/remove labelled containers and independently re-query the daemon. The module itself says these measures do not prove complete sandbox security.
- **Boundary:** Source review only; no actual Docker self-test was run.

### B044-03 — Provider client
- **Path:** `development/nova-recursive-self-improvement/provider_client.py`
- **Blob SHA:** `71318c98a48b3af7226ab82cb0970942250d8f19`
- **Disposition:** `PRELIMINARY_REVIEW_ALLOWED_PROVIDER_HOST_TLS_REDIRECT_AND_RESPONSE_BOUNDARIES`
- **Assessment:** Enforces an exact HTTPS hostname allowlist, port 443, no URL user-info/query/fragment, and explicit rejection of HTTP redirects; uses default certificate verification, bounded response reads, JSON-object response parsing and secret redaction in provider errors. It declares a default Groq host consistent with the currently checked policy/client config.
- **Boundary:** No live provider request, endpoint/redirect test, or secret handling experiment was run.

### B044-04 — Non-mutating provider preflight
- **Path:** `development/nova-recursive-self-improvement/preflight.py`
- **Blob SHA:** `ff409ca3c716fc84d5b8f4246d7afe0b825b0337`
- **Disposition:** `PRELIMINARY_REVIEW_PREFLIGHT_READINESS_AND_LIFECYCLE_GAP`
- **Assessment:** Preflight blocks unless implementation readiness is READY, validates base URL/model, requires explicit commercial-eligibility PASS and benchmark command, and only then checks provider secret presence/configuration.
- **Finding:** The preflight shares the same suspension/lifecycle gap as the engine: it never requires an explicitly released lifecycle state or confirms that the suspended-provider-call count is zero. See SWEEP-F-0015.
- **Boundary:** No preflight or provider call was run.

### B044-05 — Candidate payload schema
- **Path:** `development/nova-recursive-self-improvement/candidate.schema.json`
- **Blob SHA:** `7b9c2c656af0be56545e91d814154904e976240f`
- **Disposition:** `PRELIMINARY_REVIEW_CANDIDATE_CONTRACT_AND_RUNTIME_VALIDATION_BOUNDARY`
- **Assessment:** Provides a strict JSON-object contract with required candidate fields, constrained candidate ID syntax and no extra properties; the description correctly points to protected validation beyond the schema. `baseline_commit` has a minimum length of 7 rather than requiring a full SHA at schema level, but runtime candidate validation compares it against the actual cycle baseline. The schema must therefore be described as structural intake validation, not a full integrity gate by itself.
- **Limitations:** No schema or runtime validator tests were run.

## 3. Finding

### SWEEP-F-0015 — Strong RSI suspension is not independently enforced by engine/preflight readiness guards
- **Status:** OPEN — authorization/lifecycle control gap.
- **Affected paths:** `development/nova-recursive-self-improvement/rsi_engine.py`; `development/nova-recursive-self-improvement/preflight.py`; central readiness predicate in the protected engine.
- **Policy source:** `rsi_policy.json` says `implementation_readiness.status = INCOMPLETE`, `strong_rsi_safety.lifecycle_status = SUSPENDED`, `active_workflow_path = null`, `provider_calls_permitted_while_suspended = 0`, and `reactivation_requires_explicit_human_release = true`.
- **Observed issue:** Both engine and preflight currently check only the implementation-readiness fields. Neither reads the lifecycle status or explicitly enforces zero provider calls while SUSPENDED.
- **Risk:** If someone changes only readiness to READY, while the lifecycle stays SUSPENDED, the code-level preflight/engine guard is not sufficient to enforce the policy's suspension rule. Current readiness remains INCOMPLETE so this scenario was not executed and no provider call occurred in this review.
- **Required remediation:** Define an explicit allowed lifecycle state and human reactivation/release record within trusted policy; make the shared readiness predicate require both the readiness and released lifecycle state; verify every provider-entry point uses the guard; add fail-closed tests for READY+SUSPENDED, missing/unknown lifecycle state and the suspended-call limit. Preserve the current INCOMPLETE/SUSPENDED values; no setting is to be relaxed merely to pass tests.
- **Closure evidence:** reviewed fix PR; tests proving zero provider calls when lifecycle is SUSPENDED, even if implementation readiness is mistakenly READY; successful negative preflight test; source cross-check; current policy still SUSPENDED/INCOMPLETE. Independent review required before any reactivation.
- **Interpretation:** This is a source-inspection finding requiring implementation/test remediation, not proof that the current suspended workflow made a provider request.

## 4. Counts and limitations

- Five files received preliminary full-file reviews; human validation remains required.
- Tracker counts after this batch: **136 preliminary full-file reviews + 5 partial targeted screens + 177 not reviewed = 318 active paths**.
- Formal ISO 704 clause-level assessments completed: **0**.
- No code/tests/settings/secrets/provider calls were changed or executed.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Initial five-file preliminary content review; recorded SWEEP-F-0015. This is not a formal ISO 704 clause assessment.
