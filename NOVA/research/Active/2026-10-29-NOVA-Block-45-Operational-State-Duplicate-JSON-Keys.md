# Active Navigation Plan — NOVA Block 45: Reject Duplicate JSON Keys in Operational-State Persistence

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #157 merged after successful regression-test workflows  
**Objective:** Prevent duplicate JSON object member names inside operational-state files from being silently interpreted with parser last-value-wins behavior during state loading or publishing.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `c89ad0ce0b4008c7b80b4135ad13852cb16da4ba`  
**Working branch:** `fix/reject-duplicate-json-keys-operational-state-2026-10-29`  
**Mode:** Offline regression tests and strict operational-state parsing. No live provider calls, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed those absent files.

## Discovery

Blocks 42 and 44 made persisted health-state and generic configuration parsing reject duplicate object member names. The independent `NOVA/operational_state.py::_read_json_text()` still uses plain `json.loads()`. Python's standard decoder accepts duplicated object keys and retains only one occurrence. Therefore a corrupted or manually edited operational-state branch could contain ambiguous health fields or roster metadata that appears valid to the loader; publishing the same ambiguous files could pass validation even though later readers may disagree on the intended values.

Provider-name duplication is already validated separately by Block 41. This block addresses duplicate **JSON member names**, including nested objects, and preserves the existing provider-identity safeguards.

## Decision

Add a local duplicate-key-rejecting JSON object hook to `operational_state.py` and use it in `_read_json_text()`. Reject duplicate keys at any nesting depth with a concise `RuntimeError`; keep malformed JSON and non-object root checks. Apply the same parser to both state-branch loads and pre-publish validation by routing all four reads through the existing helper.

The parser must not expose the duplicate value or mutate local files before all persisted state files and the current roster have passed validation.

## Actions

1. Add duplicate-member detection to `_read_json_text()` in `NOVA/operational_state.py`.
2. Extend publish tests to cover duplicate nested/top-level keys in health-state and roster files, confirming rejection happens before any git/worktree operation.
3. Extend load tests to cover duplicate persisted JSON keys and confirm neither local state file is written after rejection.
4. Run the full NOVA Health Tests workflow, inspect the focused diff, and merge only after checks pass.
5. Record the PR, successful regression workflow, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** Removes last-value-wins ambiguity from operational-state parsing.
- **Compatibility:** Valid JSON and all unique-key records remain unchanged; malformed/ambiguous files fail closed.
- **Availability:** A state file containing duplicate keys now stops the affected load/publish attempt until repaired rather than being interpreted silently.
- **Resources/cost:** Offline tests only; no provider API calls or added dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This guarantees structural parsing unambiguity, not that the stored health observations or provider statuses are true.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/157 — squash-merged.
- **Merge commit:** `e2b72b102f2d5e743b002679a463b922cd6e81ec`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40832027688 — NOVA Health Tests passed on head `b8be24f9c113b99783c01d5fefc8cf6414e15a42`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40832057108 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 192 offline tests passed. The new tests cover duplicate nested member names in health-state data and duplicate top-level keys in rosters; both load and publish paths reject the records before modifying local files or beginning git/worktree operations.
- **Review:** `_read_json_text()` now uses duplicate-key detection before enforcing JSON-object roots. Existing provider identity validation and state-branch isolation remain unchanged.
- **Boundaries confirmed:** No live provider calls, credential/configuration changes, operational-state branch writes, backups, or new dependencies were introduced.
