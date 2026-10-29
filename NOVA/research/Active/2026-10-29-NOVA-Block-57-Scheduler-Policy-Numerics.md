# Active Navigation Plan — NOVA Block 57: Validate Scheduler Policy Numbers

**Date:** 2026-10-29  
**Status:** ACTIVE — prevent malformed scheduler settings from producing invalid scheduling intervals or deadlines  
**Objective:** Validate the nested health scheduler policy before using numeric settings, rejecting booleans, non-finite values, and wrong container types rather than silently coercing them or crashing later in scheduling.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `02688ec93d213647edffe2213bbd2fcf49ad8317`  
**Working branch:** `fix/validate-scheduler-policy-numerics-2026-10-29`  
**Mode:** Offline tests only; policy files are mocked and no scheduler state is persisted. No provider calls, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/probe_scheduler.py::_policy()` reads the `scheduler` field from `health_policy.json` and coerces `interval_seconds` and `opportunistic_preemption_safety_margin_seconds` with `float()`. It does not require the nested `scheduler` value to be an object, does not reject booleans (which Python treats as numbers), and does not reject NaN or infinity. Such values can later cause invalid time arithmetic, unusable schedules, or crashes rather than a clear configuration failure.

## Decision

Keep existing defaults for missing policy fields and preserve the documented minimums (interval is clamped to at least one second; safety margin is clamped to at least zero). For supplied values, require finite numeric values and explicitly reject booleans. Require the `scheduler` policy section itself to be an object. Raise a concise `ValueError` when the policy is malformed, before any state change.

## Actions

1. Add a small numeric-policy parser in `NOVA/probe_scheduler.py` that rejects booleans, non-numeric values, NaN, and positive/negative infinity.
2. Validate that `health_policy.json.scheduler` is a mapping before reading settings.
3. Add offline tests for a valid default policy, numeric integer/float compatibility, wrong scheduler container type, booleans, non-numeric strings, and non-finite numeric values.
4. Run the full NOVA Health Tests workflow, review the focused diff, and merge only after all checks pass.
5. Record the PR, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Scheduling correctness:** Invalid interval/safety settings cannot silently create unusable deadlines.
- **Compatibility:** Missing fields use current defaults; valid integer/float settings remain supported; existing minimum clamping is preserved.
- **Failure behavior:** Malformed policy fails explicitly before scheduling state is mutated.
- **Resources/cost:** Offline tests only; no provider calls.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates the two scheduler timing values only; it does not validate all fields in health or capacity policies.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
