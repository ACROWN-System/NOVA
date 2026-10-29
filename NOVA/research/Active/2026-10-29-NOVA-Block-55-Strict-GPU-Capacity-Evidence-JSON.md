# Active Navigation Plan — NOVA Block 55: Strict GPU Capacity Evidence JSON

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #167 merged after successful regression-test workflows  
**Objective:** Make the GPU-capacity evidence register use the shared duplicate-key rejecting JSON parser, so duplicate fields cannot silently alter provider qualification or calculated capacity.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** latest verified `main` after Block 54  
**Working branch:** `fix/strict-gpu-capacity-evidence-json-2026-10-29`  
**Mode:** Offline file-based regression tests. No provider calls, credential changes, state writes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/gpu_capacity.py::load_capacity_evidence()` reads the evidence register with `json.load()`, then checks only that the root is an object and `providers` is a list. Unlike the rest of NOVA's hardened JSON paths, it still accepts duplicate object member names with last-value-wins semantics. Duplicate fields such as a provider's `recurring_capacity`, `qualification`, timestamps, or GPU-minute values could therefore change which evidence is considered when deciding operational GPU capacity.

## Decision

Use `loads_json_no_duplicate_keys()` from `NOVA/health.py` to parse the evidence register. Preserve the existing semantics: missing/unreadable files remain explicit errors; the root must be an object; `providers` must be a list. Continue returning valid evidence unchanged and let malformed/ambiguous JSON fail closed before capacity reporting.

## Actions

1. Import the shared strict parser into `NOVA/gpu_capacity.py` with package and direct-script compatibility.
2. Replace `json.load()` in `load_capacity_evidence()` with strict JSON parsing.
3. Add offline tests for duplicate top-level and nested keys, wrong root type, invalid providers container, and a valid evidence-register round trip.
4. Run the full NOVA Health Tests workflow, review the focused diff, and merge only after all checks pass.
5. Record the pull request, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** GPU capacity calculations cannot silently rely on a last-value-wins interpretation of conflicting evidence.
- **Availability:** Ambiguous evidence is rejected rather than interpreted as a valid register.
- **Compatibility:** Valid evidence registers remain unchanged; existing root/providers shape checks remain.
- **Resources/cost:** Offline tests only; no GPU allocations or provider calls.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates JSON unambiguity and container shape, not the truth/freshness of evidence content, which remains governed by the existing evidence qualification logic.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/167 — squash-merged.
- **Merge commit:** `18b295006249f9cd3c447fa09e9b8f34e5256033`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40837525213 — NOVA Health Tests passed on head `8ba1e75079a1ff2105178bebcd1e4fead8928966`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40837565095 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 217 offline tests passed. New tests cover valid evidence loading, duplicate top-level/nested object keys, wrong JSON root type, and a non-list `providers` field.
- **Review:** `load_capacity_evidence()` now uses `loads_json_no_duplicate_keys()` while retaining its existing root-object/providers-list checks and explicit missing-file error behavior. Capacity qualification calculations remain unchanged for valid registers.
- **Boundaries confirmed:** No GPU allocations, provider calls, credential changes, state writes, operational-state branch writes, or backup modifications were made.
