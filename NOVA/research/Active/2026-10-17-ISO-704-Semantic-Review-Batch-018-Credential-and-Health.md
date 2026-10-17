# ISO 704:2022 Preliminary Semantic Review — Batch 018 (Credential Readiness, GPU Heartbeat and Supporting Tests)

**Review ID:** NOVA-ISO704-SEM-B018  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/STATUS REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA `main`, exact blob SHAs below  
**Boundary:** This is a terminology and evidence-state review only. No workflows/tests were executed, no credentials were read, and no live endpoint was called.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B018-01 | `NOVA/tests/test_probe_scheduler.py` | `256ec7772b4cfe9df669c7196b84376da6be15c5` | REVIEWED — test examples distinguish scheduled checks from capacity-expiry preemption |
| B018-02 | `NOVA/tests/test_health.py` | `0d5adf9f1df52707b59bda15315963a2329ba23f` | REVIEWED — mock tests distinguish unconfigured, degraded, stale and health evidence states |
| B018-03 | `NOVA/credential_readiness.py` | `b0c1e7489e9089d07aebb99254be7214d7848552` | REVIEWED — presence-only status is explicit and secret values are not returned |
| B018-04 | `NOVA/gpu_heartbeat.py` | `a351cb4c8bf4ad486fdf8791a6702125518eaa5a` | REVIEWED — candidate authentication, active GPU health endpoint and GPU allocation are separated |

## 2. Findings and positive controls

### B018-C01 — Credential state does not imply authentication or entitlement

The credential-readiness module returns `CONFIGURED_NOT_VERIFIED` when a named environment slot is non-empty and `REQUIRED_NOT_CONFIGURED` when it is empty. It does not return secret values or make live requests. Candidate GPU credentials remain `CANDIDATE_NOT_ACTIVATED` even if their environment slot is configured.

The GPU heartbeat's candidate check uses a narrowly declared/read-only endpoint and an explicit host allowlist; it blocks redirects so the bearer credential is not forwarded to another host. Its output states that a token-authenticated response still leaves GPU quota/capacity unverified and does not infer balances from undocumented response fields.

**Disposition:** preserve these status dimensions. Do not promote a configured slot, credential authentication, provider API pass, terms eligibility or GPU allocation into the same boolean.

### B018-C02 — The word HEALTHY is scoped to the endpoint and probe contract

The GPU heartbeat uses a provider-declared health URL and treats a successful accepted HTTP response as its bounded health probe. The module documentation says it is credential-independent at this stage and that GPU capacity is evidence-gated/offline; it does not allocate a GPU. This contract is not the same as NOVA's structured LLM health-payload contract, a real GPU job, a quota/credit observation, commercial-use permission or proof of a no-payment account.

**Required action:** preserve this endpoint/probe scope in operational summaries and any downstream public language. A `HEALTHY` GPU heartbeat must be described as “the configured health endpoint passed the recorded HTTP probe” unless separate evidence proves a broader property.

### B018-C03 — Candidate authentication statuses describe evidence type, not activation

The GPU candidate output has separate fields for candidate lifecycle, whether a credential slot is configured, authentication probe status, API status and GPU capacity status. An accepted read-only response may produce `CREDENTIAL_AUTHENTICATED_READ_ONLY`, but capacity remains `UNVERIFIED`. HTTP failures are categorized into authentication rejection, payment-required-or-credit-exhausted, scope/policy denial, rate limiting, redirect blocked, or generic HTTP error.

These are bounded diagnostic classifications. The payment/credit combined outcome remains ambiguous for the exact cause by design and should not be converted into a definitive “payment method is required” conclusion without more provider-specific evidence.

### B018-C04 — Positive test vocabulary: stale is not dead, unknown is not zero

The health tests cover explicit freshness, prior analysis preservation, fingerprint-based reuse and the fact that unconfigured credentials do not count as a provider failure. The scheduler tests cover legitimate expiry preemption, rolling queue order and reuse of a total resource only for already-required work. They are deterministic tests using synthetic timestamps and state rather than a live timing measurement.

**Disposition:** preserve the separation between synthetic/test values, observed runtime telemetry and independent account/terms evidence. These tests were read but not run in this review.

## 3. Evidence and limitations

- No secret values were read or persisted, no workflow was dispatched, and no health or credential endpoint was called.
- Code-level review supports the intended semantics but does not prove repository settings, workflow execution, provider terms, quota or GPU workloads.
- The GPU heartbeat's health scope is its configured HTTP endpoint, not GPU allocation or LLM response-contract qualification.
- No ISO 704 clause result is assigned because the full controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed probe scheduler tests, health tests, credential-presence report and GPU-heartbeat implementation.
