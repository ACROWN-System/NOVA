# Active Navigation Plan — NOVA Block 58: Validate Capacity-Preemption Policy

**Date:** 2026-10-29  
**Status:** ACTIVE — validate runtime allocation/freshness policy before expiry-aware scheduling  
**Objective:** Prevent malformed or out-of-range capacity-preemption settings from causing scheduler crashes or distorting decisions about whether required probes should be advanced to reuse expiring capacity.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `9d51e4fed109fbec575cc03367a16af13f760741`  
**Working branch:** `fix/validate-capacity-preemption-policy-2026-10-29`  
**Mode:** Offline tests only; policy files and state are mocked. No provider requests, state writes, credentials changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

After Block 57, the scheduler's health timing values are validated, but `select_probe_candidate()` still reads `capacity_policy.json.runtime_allocation` via direct `.get()` calls and converts `urgency_window_seconds`, `minimum_remaining_reserve_fraction`, and optional `maximum_capacity_observation_age_seconds` with `float()`. It also reads `health_policy.json.freshness.heart_observation_max_age_seconds` without checking that `freshness` is a JSON object. Boolean/numeric-string/non-finite values may be coerced, the reserve fraction can be outside [0,1], and malformed nested containers can raise exceptions. These values directly influence preemption, reserve protection, and the freshness of evidence used in scheduling.

## Decision

Validate both nested policy sections before calling `ensure_probe_schedule()` or mutating the probe queue:

- Require `capacity_policy.json.runtime_allocation` and `health_policy.json.freshness` to be mappings.
- Require urgency-window and observation-age settings to be finite JSON numbers (reject booleans and strings); optional maximum observation ages may be `null`.
- Require `minimum_remaining_reserve_fraction` to be finite and within [0,1].
- Require any supplied maximum observation age to be non-negative.
- Preserve the existing one-second minimum urgency window and absent-field behavior.
- Pass the already validated health freshness age into the provider status check rather than re-reading and reinterpreting the policy inside the provider loop.

## Actions

1. Generalize the finite-number helper to identify the relevant policy file in diagnostics.
2. Add a policy reader for runtime allocation and health freshness fields.
3. Validate these policy values at the start of candidate selection, before queue/state mutation.
4. Add offline tests for valid/default values, wrong nested container types, booleans/strings/non-finite values, reserve fractions outside [0,1], negative ages, and no state mutation on invalid policy.
5. Run the full NOVA Health Tests workflow, review the focused diff, and merge only after all checks pass.
6. Record the pull request, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Scheduling integrity:** Invalid numeric policy can no longer alter reserve gating or expiry-preemption ordering through coercion.
- **Fail-closed behavior:** Malformed policy fails before the queue changes.
- **Compatibility:** Defaults remain unchanged; finite urgency values retain the existing one-second minimum; valid reserve fractions and ages are accepted.
- **Resources/cost:** Offline tests only; no provider calls.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates the capacity-preemption numeric policy only; the capacity evidence schema and economic qualification rules remain unchanged.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
