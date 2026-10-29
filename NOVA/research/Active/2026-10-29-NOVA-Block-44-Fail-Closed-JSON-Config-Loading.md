# Active Navigation Plan — NOVA Block 44: Fail Closed on JSON Configuration Loading

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #156 merged after successful regression-test workflows  
**Objective:** Make the shared JSON configuration loader distinguish an absent optional file from an existing but unreadable, malformed, ambiguous, or structurally incorrect file, so monitoring and policy settings cannot be silently disabled by parse failures.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `a10553582189a2530a4a2bb40b59ad0f85f1fbda`  
**Working branch:** `fix/fail-closed-json-config-loading-2026-10-29`  
**Mode:** Offline regression tests and strict JSON configuration loading. No live provider calls, credential/configuration edits, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed those absent files.

## Discovery

The generic `load_json(path, default)` helper currently returns the supplied default not only when a file is absent, but also when an existing file cannot be read or contains malformed JSON. That behavior can hide a broken `watchlist.json` by substituting an empty source list, hide malformed provider rosters by substituting an empty providers list, or silently replace malformed health/capacity/action policy objects with empty dictionaries. Because the same helper is used by `operational_observer.py`, `reasoning.py`, `gpu_heartbeat.py`, `probe_scheduler.py`, and `router.py`, the risk is shared across several subsystems.

Block 42 made `load_health_state()` strict, including duplicate-key rejection, but generic configuration reads can still fall back silently. A successful JSON parse can also be ambiguous when duplicate object member names are present.

## Decision

Keep the current caller-supplied defaults only for a genuinely absent optional file. If a file exists, require it to be readable UTF-8 JSON, reject duplicate object keys at every nesting depth, and require the top-level JSON type to match a container default (`dict` or `list`). Raise a concise, content-redacted `RuntimeError` on failure; do not modify the source file. Preserve callers' valid parsed values and do not change their existing policy or roster semantics.

## Actions

1. Change `load_json()` in `NOVA/health.py` so only `FileNotFoundError` returns the provided default.
2. Reuse NOVA's duplicate-JSON-key detector and reject malformed, undecodable, unreadable, duplicate-key, and wrong-root-type existing files.
3. Add offline tests for missing-file fallback, valid JSON, malformed JSON, unreadable/undecodable files, duplicate top-level and nested keys, and root-type mismatch. Verify failed reads preserve file bytes.
4. Run the full NOVA Health Tests workflow, inspect the diff, and merge only after all checks pass.
5. Record the final PR, regression run, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Monitoring integrity:** A broken watchlist can no longer masquerade as a deliberate empty watchlist.
- **Policy integrity:** Malformed provider rosters or health/capacity/action policies can no longer be silently replaced with defaults.
- **Availability:** A malformed existing configuration now stops the affected run with an explicit error, requiring repair rather than proceeding with a false impression of valid configuration.
- **Compatibility:** Missing optional files still use existing caller-supplied defaults; generic valid JSON behavior remains unchanged.
- **Resources/cost:** Offline tests only; no provider requests or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** Validation checks JSON readability, object-key uniqueness, and top-level container type. It does not certify the semantic correctness or current truth of every value in every configuration file.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/156 — squash-merged.
- **Merge commit:** `9000e67db8e02e41d98d064e4601e0d7bf6b5920`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40831782271 — NOVA Health Tests passed on head `567e186ace5f4008593c28543a8e77fde694987a`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40831812178 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 190 offline tests passed. The added tests cover absent-file defaults, valid object/array input, malformed JSON, duplicate top-level/nested keys, unreadable and undecodable files, and wrong root types; rejected reads leave source bytes unchanged.
- **Review:** The diff changes only `NOVA/health.py`, `NOVA/tests/test_health.py`, and this Active plan. Generic defaults are now only used when the optional file is genuinely missing. Block 42 strict state loading and Block 43 analysis-cache provenance checks remain intact.
- **Boundaries confirmed:** No live provider calls, credential/configuration edits, operational-state branch writes, backup changes, or new dependencies were introduced.
