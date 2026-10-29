# Active Navigation Plan — NOVA Block 41: Validate Operational State Before Loading

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #153 merged after successful regression-test workflows  
**Objective:** Make operational-state loading reject malformed or duplicate provider identities before writing loaded state, and make identity matching consistent with the publication validator.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at handoff:** `fba8b3d2df651d27fd59496c33512ab8b1b11292` (Block 40 merged)  
**Working branch:** `fix/validate-operational-state-before-loading-2026-10-29`  
**Mode:** Offline regression coverage and fail-closed validation; no live provider calls, credentials/configuration changes, operational-state branch writes, or backup changes.

The current `main` tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` navigation-plan convention as the available fallback and does not claim to have followed the absent files.

## Discovery

Block 40 added `_validate_publishable_state()` to reject invalid JSON and malformed or duplicate provider identities before operational state is published. However, `merge_dynamic_roster()` still validates only that each roster's `providers` member is a list, and its persisted name index uses exact-name dictionary keys. A legacy or manually corrupted state branch could therefore contain duplicate normalized identities and let dictionary last-value-wins semantics decide the saved down marker. A single provider whose stored name differs only by case or surrounding whitespace would not match the current repository's identity.

The current `main` roster and `nova-operational-state` roster each contain three unique providers (`groq`, `gemini`, `cloudflare`). The fix is preventive and keeps the existing provider set unchanged.

## Decision

Use one provider-roster validator for both publication and merge/loading. Require a JSON object roster with a providers array; every entry must be an object with a non-empty string name; and provider identities must be unique after trimming and case-folding. Use that same normalized identity for matching the persisted roster to the current repository roster. Preserve the existing authority rule: current repository configuration wins, except an active current provider may inherit a valid persisted `down` marker.

Malformed data must fail before `load_operational_state()` writes either state file. Do not change provider routing, credentials, credentials policy, live API behavior, or state-branch publication mechanics.

## Actions

1. Add the shared provider-roster validation helper and use it in publishing and roster merging.
2. Normalize provider identities for lookup only after validating uniqueness.
3. Add offline regression tests for duplicate normalized persisted identities and case/whitespace-insensitive matching of a valid down marker.
4. Run the existing NOVA Health Tests workflow and inspect its result before considering the block complete.
5. Open a focused pull request; do not merge if validation fails.

## Impact analysis

- **Safety:** Prevent ambiguous persisted records from silently affecting provider status.
- **Integrity:** Make load-time validation match publish-time validation and prevent dictionary last-value-wins behavior.
- **Compatibility:** Current valid provider names remain accepted; repository configuration remains authoritative except for the existing down-marker rule.
- **Resources/cost:** Offline tests only; no provider API usage or additional dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This does not validate the broad semantic truth of operational health data; it validates JSON/object/roster structure and provider identity before using saved state.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/153 — squash-merged.
- **Merge commit:** `edd659be7cfdb207c1e0e06dea066d4e30e3f0c6`.
- **PR workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40829926281 — NOVA Health Tests passed on head `a5cfd9b923e9662ca865ca7732dc42ddf309446f`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40829889129 — NOVA Health Tests passed on the same head commit.
- **Review:** The changed implementation and regression tests were inspected. The shared validator is used by publish and merge/load paths; duplicate normalized identities fail before state writes; normalized matches preserve only the permitted `down` marker and keep current repository configuration authoritative.
- **Boundaries confirmed:** No live provider calls, new dependencies, credential/configuration changes, operational-state branch writes, or backup modifications were made for this block.
