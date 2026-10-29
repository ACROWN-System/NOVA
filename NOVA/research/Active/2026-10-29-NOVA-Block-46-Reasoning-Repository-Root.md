# Active Navigation Plan — NOVA Block 46: Honor the Reasoning Repository Root

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #158 merged after successful regression-test workflows  
**Objective:** Make `NOVA/reasoning.py --repo PATH --pending` use the supplied repository's `NOVA/` state, roster, and policy files rather than silently ignoring `PATH`.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `faa59bf6ffdabcc7d91f813b5494d5dcc8c78d49`  
**Working branch:** `fix/honor-reasoning-repo-root-2026-10-29`  
**Mode:** Offline regression tests; provider calls and alert emission mocked/avoided. No real health-state writes, live provider calls, credential changes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This record follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`main()` parses `--repo` and passes `Path(args.repo).resolve()` to `analyze_pending(root)`, but `analyze_pending()` immediately executes `del root` and uses module-global `HEALTH_STATE_PATH`, `ROOT`, `HEALTH_POLICY_PATH`, `WATCHLIST_PATH`, and `ACTION_POLICY_PATH`. Therefore, an explicit repository root is ignored. A caller intending an isolated workspace can instead read the script checkout's operational state and write analysis results back into that checkout.

The observer runner already follows the correct convention by deriving all state paths from the function's root argument. The reasoning runner should align with that pattern.

## Decision

Treat the supplied root as the repository root. Derive a local `nova_root = root.resolve() / "NOVA"`; use that path for health state, roster, health policy, watchlist, and action policy throughout `analyze_pending()`. Keep module-level paths only as default constants for compatibility where needed; the runtime function must not use them when a root is supplied. Preserve stale-event superseding, provider order, policy gates, alert behavior, and output format.

## Actions

1. Replace the discarded root and module-global runtime paths in `analyze_pending()` with paths derived from the supplied repository root.
2. Update the stale-pending-event regression test to use a temporary repository root and assert that state read/write and configuration reads use that root.
3. Add/retain a test showing no provider selection is attempted once stale pending events are superseded and no current event remains.
4. Run the full NOVA Health Tests workflow, inspect the changed-file diff, and merge only after checks pass.
5. Record the PR, workflow evidence, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Isolation:** A sandbox or alternate checkout no longer risks reading or overwriting the script checkout's state.
- **Correctness:** The CLI's documented `--repo` argument now has effect for every reasoning input and state write.
- **Compatibility:** Running from the repository root with the default `--repo .` resolves to the same `NOVA/` directory as before.
- **Resources/cost:** Offline tests only; no AI/provider API usage.
- **Safety:** External analysis remains advisory and governed by current policy. No action permissions are broadened.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This corrects filesystem scoping; it does not itself validate external source truth or change reasoning semantics.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/158 — squash-merged.
- **Merge commit:** `f1eaa61395b9ba7f0623ccf7179b408eee9ad6a6`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833024059 — NOVA Health Tests passed on head `769a9580cd8ba8dbf9d6b968fe8a2460f3e2b696`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833050056 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** The offline reasoning tests passed, including assertions that the chosen repository root supplies the health state, provider roster, health policy, watchlist, action policy, and health-state destination.
- **Review:** `analyze_pending(root)` no longer discards `root`. It derives all runtime paths from `Path(root).resolve() / "NOVA"` while retaining current defaults, source-bound analysis, stale-event superseding, provider selection, policy, and alert semantics.
- **Boundaries confirmed:** No live provider calls, alert emission, real state-file writes, credentials changes, or backup modifications were made.
