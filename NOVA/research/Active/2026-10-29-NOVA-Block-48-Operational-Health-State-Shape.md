# Active Navigation Plan — NOVA Block 48: Validate Health-State Shape at Operational Boundaries

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #160 merged after successful regression-test workflows  
**Objective:** Prevent the operational-state loader or publisher from accepting a health-state JSON object whose core state maps have invalid types and will be rejected later by `load_health_state()`.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** latest verified `main` after Block 47  
**Working branch:** `fix/validate-health-state-shape-at-operational-boundary-2026-10-29`  
**Mode:** Offline regression tests only. No live provider calls, operational-state branch writes, credential changes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

Block 42 made `load_health_state()` reject an existing health-state document if any present core map (`targets`, `observations`, `events`, or `provider_rotation`) is not a JSON object. However, `NOVA/operational_state.py` uses a separate parser at both state-branch load and pre-publication validation boundaries. That parser currently validates only duplicate-key ambiguity, JSON syntax, and an object root. A document such as `{"targets":[]}` can therefore be loaded from the state branch or published even though the runtime state loader will later reject it.

This mismatch can leave the dedicated state branch containing a state document that prevents the next heartbeat from loading successfully. Validation must happen before any local state writes or git worktree operations.

## Decision

Extract the shared core-map shape validation into a function in `NOVA/health.py` and call it from both `load_health_state()` and `operational_state.py` at both persistence boundaries:

- While loading state from the dedicated branch, validate health state before reading/writing any local state files.
- Before publishing, validate health-state core maps before creating a worktree or invoking git mutations.
- Preserve backward compatibility for older state documents where core maps are absent; defaults may still be filled by `load_health_state()`.
- Keep duplicate JSON-key validation, roster identity validation, and dedicated state-branch isolation intact.

## Actions

1. Introduce a reusable health-state payload validator in `NOVA/health.py`.
2. Use it from `load_health_state()`, `load_operational_state()`, and `_validate_publishable_state()`.
3. Add offline regression tests proving malformed core maps in state-branch input are rejected before local writes, and malformed local state is rejected before git/worktree operations.
4. Run the full NOVA Health Tests workflow, review the changed-file diff, and merge only after all checks pass.
5. Record pull-request, workflow, and merge evidence here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** State-branch load and publish rules match the runtime loader's requirements.
- **Availability:** Invalid state is rejected at the boundary that encounters it, with no partial local writes or state-branch publication.
- **Compatibility:** Missing core maps remain valid legacy input and can receive defaults; present malformed maps are rejected.
- **Resources/cost:** Offline tests only; no provider calls or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates top-level map types, not every nested health value's truth or semantic validity.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/160 — squash-merged.
- **Merge commit:** `e0eff016f33a1bb6b4d4538fdcdf2837a26ba51b`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833932270 — NOVA Health Tests passed on head `c4a8cbcf63d3a0ad24d386c07ab5391fb93cb26d`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833965265 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 196 offline tests passed. New tests reject each malformed core map during state-branch loading without local writes, and reject malformed local health-state maps before publication can create a git worktree.
- **Review:** `validate_health_state_payload()` is shared by `load_health_state()` and both operational-state boundaries. Missing core maps remain compatible with older state and can receive runtime defaults; present non-object core maps fail closed.
- **Boundaries confirmed:** No live provider calls, operational-state branch writes, credential changes, or backup modifications were made.
