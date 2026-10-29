# Active Navigation Plan — NOVA Block 59: Validate Router Health Policy Before Probes

**Date:** 2026-10-29  
**Status:** ACTIVE — reject malformed health-probe policy before any provider request  
**Objective:** Validate heartbeat freshness, latency, and failure settings up front so invalid policy cannot consume a provider request and then abort before the response is recorded.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `1ea8abad8ed7719fdd7bc42de3d4192efa017512`  
**Working branch:** `fix/validate-router-health-policy-before-probes-2026-10-29`  
**Mode:** Offline tests only; provider calls, roster/state reads, and state writes are mocked. No live provider requests, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/router.py::intelligent_router()` reads the health policy and converts `freshness.heart_observation_max_age_seconds` before selecting providers, but does not validate the nested sections or numeric semantics. More importantly, `latency.max_samples_per_target`, `latency.degraded_multiplier`, `latency.minimum_samples_for_comparison`, and `failure.unacceptable_consecutive_failures` are converted only while recording the first provider's response. If one is malformed, the router may make a live API request, then throw during `record_probe()` argument construction before persisting that response or finishing failover.

Booleans are also accepted by Python's `int()`/numeric conversions, and non-finite multipliers can yield nonsensical health classifications.

## Decision

Validate all health-probe settings before loading/mutating runtime state or making a provider call:

- Require the `freshness`, `latency`, and `failure` sections to be JSON objects when present.
- Treat a missing freshness age as unspecified; if supplied, require a non-negative integer.
- Require `max_samples_per_target`, `minimum_samples_for_comparison`, and `unacceptable_consecutive_failures` to be positive integers, rejecting booleans.
- Require `degraded_multiplier` to be a finite positive JSON number, rejecting booleans and strings.
- Keep existing policy defaults for absent fields and pass validated values unchanged into the health recorder.

## Actions

1. Add a health-probe policy validator in `NOVA/router.py`.
2. Call it immediately after reading `health_policy.json`, before state loading/provider ordering/API requests.
3. Reuse the validated values later when calling `record_probe()`; remove late unvalidated `int()`/`float()` conversions.
4. Add offline tests for defaults and malformed section/value cases, plus an end-to-end guard that invalid latency policy causes no provider call.
5. Run the full NOVA Health Tests workflow, review the diff, and merge only after all checks pass.
6. Record the PR, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Cost/resource use:** Invalid policy can no longer consume a provider call before failing.
- **Health integrity:** Non-finite multipliers, booleans, and invalid failure thresholds cannot distort health classification.
- **Compatibility:** Missing fields retain existing defaults; valid current JSON policy remains unchanged.
- **Failure behavior:** Invalid health policy raises an explicit configuration error before provider calls or state writes.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates heartbeat health policy only; capacity-preemption policy and provider ordering are handled by their existing logic and prior validation work.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
