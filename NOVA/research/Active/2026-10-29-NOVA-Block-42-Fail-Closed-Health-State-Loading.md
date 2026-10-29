# Active Navigation Plan — NOVA Block 42: Fail Closed on Corrupt Health State

**Date:** 2026-10-29  
**Status:** ACTIVE — protect persisted health-state history from silent reset  
**Objective:** Ensure a present but unreadable, malformed, or structurally invalid `NOVA/health_state.json` blocks runtime state loading instead of silently substituting defaults that a caller may later write over the original file.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `2c136a2e7b47d11111e05d9689d68961fb67763a`  
**Working branch:** `fix/fail-closed-on-corrupt-health-state-2026-10-29`  
**Mode:** Offline regression tests and strict local state loading. No live provider calls, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` navigation-plan convention as the available fallback; it does not claim to have followed absent files.

## Discovery

`NOVA/health.py` currently implements `load_health_state()` through `load_json(path, _state_defaults())`. The shared `load_json()` helper returns the supplied default when a file exists but raises an I/O or JSON decoding error. `load_health_state()` also replaces a valid JSON root that is not an object with defaults, and fills missing top-level defaults without rejecting malformed types for core state maps.

That recovery behavior is unsafe for operational state: a caller can proceed with an empty state and subsequently persist it, losing previously retained observations, events, provider rotation, or health history. The operational-state load/publish guards added in Blocks 40–41 do not prevent this local read path from concealing corruption.

## Decision

Keep the generic `load_json()` fallback semantics for non-operational configuration callers, but make `load_health_state()` strict for an existing state file:

- If the file does not exist, initialize the documented default state (first-run behavior).
- If it exists but cannot be read, is invalid JSON, has duplicate JSON object keys at any depth, or has a non-object root, raise an explicit, content-redacted error and do not synthesize replacement state.
- Require the core mapping fields `targets`, `observations`, `events`, and `provider_rotation` to be objects when present; absent fields can still be initialized for schema-compatible older state.
- Never modify, rename, or delete the existing file on a failed load.

## Actions

1. Implement strict health-state parsing, duplicate-key rejection, and top-level structural validation in `NOVA/health.py`.
2. Add offline tests for missing-file first-run defaults, malformed JSON, duplicate keys, undecodable bytes, non-object roots, and malformed core mapping fields.
3. Where an existing corrupt file is rejected, verify its bytes remain unchanged.
4. Run NOVA Health Tests on the pull request head and inspect the workflow result.
5. Open a focused pull request and merge only after all required checks pass.

## Impact analysis

- **Integrity:** Avoid silently resetting persisted operational history after a failed read.
- **Availability:** A corrupt file may now stop the affected run with an explicit error instead of appearing healthy with empty memory. This is deliberate fail-closed behavior requiring repair/recovery rather than concealed data loss.
- **Compatibility:** Missing state remains a valid first-run case; absent newer fields still receive defaults. Generic `load_json()` behavior is unchanged.
- **Resources/cost:** Offline tests only; no provider requests or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This checks JSON load integrity, duplicate-key ambiguity, and top-level state shape; it does not prove every nested observation or health claim is truthful.

## Completion evidence

Record the pull request, successful regression workflow, final review, and merge commit here before marking this plan COMPLETE.
