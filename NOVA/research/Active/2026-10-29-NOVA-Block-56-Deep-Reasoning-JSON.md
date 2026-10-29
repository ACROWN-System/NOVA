# Active Navigation Plan — NOVA Block 56: Fail Closed on Deeply Nested Reasoning JSON

**Date:** 2026-10-29  
**Status:** ACTIVE — prevent deeply nested model output from escaping the controlled reasoning failure path  
**Objective:** Ensure a deeply nested or otherwise decoder-hostile reasoning response is treated as invalid JSON and follows the bounded retry policy rather than raising an uncaught exception.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `947fdc0311ae8ccfc74c7aa8ab44dde4e77e9db6`  
**Working branch:** `fix/fail-closed-on-deep-reasoning-json-2026-10-29`  
**Mode:** Offline tests only; provider responses, state loading/writes, and alerts are mocked. No provider calls, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/reasoning.py::analyze_pending()` parses the model response with ordinary `json.loads(response_text)` before calling `validate_reasoning_payload()`. The validator already catches `RecursionError` and returns `INVALID_JSON`, but the earlier parse only catches `json.JSONDecodeError`. An extremely deeply nested response can therefore raise an uncaught `RecursionError` before the strict validator runs, escaping the per-event failure handler and interrupting the controlled retry lifecycle.

## Decision

Treat `RecursionError` from the initial response parse as invalid provider JSON and call the existing `_record_reasoning_failure()` path. Keep bounded-attempt accounting, pending/exhausted state semantics, strict reasoning validation, policy gates, and provider usage rules unchanged.

## Actions

1. Catch `RecursionError` with `json.JSONDecodeError` in the initial reasoning response parse.
2. Add a regression test with deeply nested invalid JSON, a mocked provider response, and mocked state I/O to prove the event follows bounded retry handling rather than raising.
3. Run the full NOVA Health Tests workflow, inspect the changed-file diff, and merge only after all checks pass.
4. Record the PR, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Reliability:** Malformed deep JSON cannot crash the controlled reasoning cycle before validation.
- **Cost control:** Existing bounded retry limit remains authoritative; no new provider calls are introduced by the fix.
- **Safety:** The invalid response is never accepted as analysis; existing policy gates and advisory-only semantics remain intact.
- **Compatibility:** Valid reasoning responses are unchanged.
- **Resources/cost:** Offline regression tests only.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This catches recursion-depth parsing failure; it does not change payload schema requirements or assess analysis truth.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
