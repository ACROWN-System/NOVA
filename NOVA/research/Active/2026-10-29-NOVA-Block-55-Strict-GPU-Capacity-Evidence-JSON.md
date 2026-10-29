# Active Navigation Plan — NOVA Block 55: Strict GPU Capacity Evidence JSON

**Date:** 2026-10-29  
**Status:** ACTIVE — prevent ambiguous capacity evidence from influencing GPU qualification totals  
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

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
