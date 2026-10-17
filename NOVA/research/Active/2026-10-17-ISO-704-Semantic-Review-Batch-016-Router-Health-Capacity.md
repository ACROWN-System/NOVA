# ISO 704:2022 Preliminary Semantic Review — Batch 016 (Router, Health Telemetry, Capacity Semantics and Tests)

**Review ID:** NOVA-ISO704-SEM-B016  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/STATE-MODEL REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA `main`, exact blob SHAs below  
**Boundary:** Terminology and status semantics only; no tests were executed in this batch and no live provider was called.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B016-01 | `NOVA/router.py` | `9846d49b4ad812f8bf1228604f489c95eac84440` | REVIEWED — explicit health contract, but broad permanent/provider-down terminology needs review |
| B016-02 | `NOVA/tests/test_router.py` | `e0e2967c78d161d1e2b57019dc73690597e48a54` | REVIEWED — mock tests demonstrate distinct status classes; they are not live qualification evidence |
| B016-03 | `NOVA/health.py` | `d43758649c2e3413f2cda7c0bd669181039e800d` | REVIEWED — freshness/health/action states are explicitly differentiated |
| B016-04 | `NOVA/capacity.py` | `aea6e6f36f62b1b3862f01777f2d117b232b8da8` | REVIEWED — total resources, call allowances, economic comparability and unknowns are distinct concepts |

## 2. Findings

### B016-F01 — “Permanent” model/endpoint failure may be promoted to provider-wide DOWN

The router classifies every HTTP 404 as `permanent`, also uses response-body markers such as `model_not_found`, then returns a `permanent` provider signal if any probed model carries that class. The outer routing logic uses this signal to mark the provider's roster entry `down`, even though some markers explicitly refer to a *model* not being found. A missing/retired model or endpoint is not, by itself, proof that the provider as a whole is permanently unavailable or that all of its models fail.

**Required action:** review the intended state scope and make the vocabulary reflect it. Separate terminal model/endpoint configuration errors from a provider-wide confirmed retirement/unavailability. Before a provider status is changed to DOWN, require evidence that justifies that provider-level scope, or preserve a model-scoped failure and continue to another configured model where appropriate. This is a potential status-model defect found during content review, not a claim that an actual provider was incorrectly marked down in production. No code change is made in this batch.

### B016-F02 — Truncation is not the same as sanitization for persisted provider error detail

The HTTP exception path keeps the provider's error body in `error_detail` (truncated to 400 characters) and `record_probe` writes that field into the durable health observation. The separate root-cause case stores a sanitized summary and does not retain the raw detail. These two evidence paths therefore have different retention semantics. Truncating text limits size but does not ensure it is free from personal data, account details, reflected request content or other sensitive material.

**Required action:** describe each record path precisely rather than calling all provider telemetry “sanitized.” Review the provider-error body retention rule: define allowed fields, redact/scrub known sensitive formats before persistence, and prove with negative tests that representative secret/PII marker values do not enter durable history. Retain any required diagnostic codes/correlation IDs through bounded allowlists. This is a data-minimization/security follow-up; the current batch did not find a demonstrated secret leak in a live record.

### B016-F03 — Positive control: response-contract health is separate from HTTP success

The router's deterministic response contract requires a non-empty JSON response with `nova_health == OK` and `ack == NOVA_HEALTH_PROBE`. Its tests distinguish transport/API status, authentication status, JSON/shape validity, missing-marker outcomes and a deliberate capability contract gate that prevents the network call until a model's structured-JSON contract is verified. A syntactically successful HTTP response does not by itself establish NOVA health.

**Disposition:** preserve this distinction. A mock test passing confirms the tested software path only; it does not prove the same model's current live behavior.

### B016-F04 — Positive control: health observation freshness is not truth

The health module differentiates `UNOBSERVED`, `UNSPECIFIED`, `INVALID_FRESHNESS_POLICY`, `INVALID_TIMESTAMP`, `FUTURE_TIMESTAMP`, `FRESH` and `STALE`. Provider-level aggregation excludes observations outside the requested freshness window and returns `STALE` when all considered evidence is stale, instead of inferring that the underlying service is false or dead. Health states then separately include `HEALTHY`, `DEGRADED`, `UNACCEPTABLE`, `UNCONFIGURED` and `UNKNOWN`.

**Disposition:** this is a strong state-vocabulary control. Ensure downstream public/reporting language keeps the observation's scope and timestamp visible.

### B016-F05 — Positive control: capacity is split from rate limits and value is not inferred

The capacity module defines `TOTAL_RESOURCE` separately from `CALL_ALLOWANCE`, and states that missing measurement remains UNKNOWN—not unlimited or zero-cost. Economic net value becomes comparable only when required monetary-like terms share a unit; incomplete/unknown economics produce neutral or no-priority outcomes. Expiry pressure is explicitly barred from creating synthetic work, with a limited exception to reuse expiring capacity for already-required work.

**Disposition:** preserve resource/call/time/economic-unit distinctions. A capacity-opportunity label is a scheduling signal, not proof of account entitlement or measured cash savings.

## 3. Evidence and limitations

- Tests were read, not executed; no code changes, workflows or live providers were used.
- This review does not assert actual production malfunction. It records a scope-vocabulary risk in the permanent/provider-down path and a difference between truncated and redacted error details.
- Provider roster, model contracts, live health freshness, account quota, and payment eligibility remain separate evidence requirements.
- No clause-level ISO 704 finding or result is assigned because the complete controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed routing, router test, shared health telemetry and capacity helpers. Recorded model-vs-provider failure scope and truncation-vs-sanitization as follow-ups, while preserving the existing explicit state vocabulary.
