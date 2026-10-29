# Active Navigation Plan — NOVA Block 53: Strict Local Roster Loading

**Date:** 2026-10-29  
**Status:** ACTIVE — remove direct local roster readers that bypass strict JSON parsing  
**Objective:** Make the router and credential-readiness CLI reject duplicate-key or structurally invalid local provider roster files instead of interpreting ambiguous provider configuration.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `a62253059699392886925029dc4f0371f8c27112`  
**Working branch:** `fix/strict-local-roster-loading-2026-10-29`  
**Mode:** Offline file-based regression tests. No provider calls, credential changes, production state writes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

Block 44 made the shared `load_json()` helper strict, and Block 48/45 strengthened operational-state loading. However, `NOVA/router.py::load_roster()` still reads `NOVA/roster.json` with direct `json.loads()`. `NOVA/credential_readiness.py` likewise reads the configured LLM and GPU roster paths using direct `json.loads()`. These paths bypass duplicate-key rejection; a repeated `providers`, `status`, or credential-environment field can silently be interpreted using the last value, potentially changing which provider is treated as active or which secret slot is reported.

## Decision

Use the shared `loads_json_no_duplicate_keys()` parser for both local roster readers. Require each root to be a JSON object containing a `providers` array. If the GPU roster has a `candidates` field, require it to be an array as well. Keep valid roster values unchanged and preserve the existing fail-fast behavior when files are missing or unreadable.

## Actions

1. Update `router.load_roster()` to use strict JSON parsing and validate the object/providers-array shape.
2. Add a strict file-loading helper in `credential_readiness.py` and use it for LLM/GPU roster paths.
3. Add offline tests for duplicate top-level/nested roster keys and wrong root/container types.
4. Run the full NOVA Health Tests workflow, review the focused diff, and merge only after all checks pass.
5. Record the pull request, successful regression workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** Provider eligibility and credential-readiness reports cannot silently depend on last-value-wins parsing.
- **Compatibility:** Valid current rosters remain unchanged; absent `candidates` remains acceptable for older GPU roster formats.
- **Availability:** Invalid existing roster files fail explicitly instead of producing a misleading eligibility report.
- **Resources/cost:** Offline tests only; no provider calls or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This checks JSON ambiguity and container shape; it does not verify whether the configured providers' live status or credentials are valid.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
