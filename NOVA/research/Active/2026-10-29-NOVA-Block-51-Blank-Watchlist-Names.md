# Active Navigation Plan — NOVA Block 51: Reject Blank Watchlist Source Names

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #163 merged after successful regression-test workflows  
**Objective:** Prevent whitespace-only source names from passing watchlist validation when the observer will use them as literal source identities rather than falling back to the URL.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `08e59ab1d6d8570da669a3166861a0a7be67a7d4`  
**Working branch:** `fix/reject-blank-watchlist-source-names-2026-10-29`  
**Mode:** Offline tests only; no source fetches or persistent state writes. No network requests, provider calls, credentials changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed those absent files.

## Discovery

Block 49's validator lowercases and trims provided names for identity uniqueness, and falls back to the normalized URL when a name is absent or whitespace-only. However, `observe_source()` selects `source.get("name") or source.get("url")`. A whitespace-only string is truthy in Python, so it remains the runtime identity. Two sources with whitespace-only names and distinct URLs can pass validation but collide in the same memory/event key at runtime.

## Decision

Treat a missing name as a request to use the URL identity, but reject any supplied name that is not a non-empty string after trimming. Keep case/whitespace normalization for uniqueness of valid names. This makes the validator's allowed configuration match runtime identity behavior without changing valid unnamed watchlist entries.

## Actions

1. In `validate_watchlist()`, reject a supplied name whose trimmed value is empty, with a content-redacted indexed diagnostic.
2. Add offline tests proving blank and whitespace-only names are rejected while an omitted name remains valid and uses the URL identity.
3. Keep the no-fetch-before-validation behavior and existing HTTP(S)/userinfo checks unchanged.
4. Run the full NOVA Health Tests workflow, review the diff, and merge only after all checks pass.
5. Record the pull request, regression workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** Prevents validated source identities from diverging from runtime memory/event keys.
- **Compatibility:** Watchlist entries with no `name` remain valid; provided names must be meaningful.
- **Resources/cost:** Offline tests only; no external reads or provider API usage.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This resolves source-key consistency only; it does not establish that source content is truthful.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/163 — squash-merged.
- **Merge commit:** `da42c3ec82f17325bb5fd82b982df73398c21687`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40835110689 — NOVA Health Tests passed on head `749518d583acd128681bde4c48a4fca4e444e6c9`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40835147723 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 204 offline tests passed. Empty and whitespace-only supplied names are rejected; an omitted name remains valid and can use the URL as identity.
- **Review:** The Block 49 source validator now cannot accept a supplied blank name that the runtime observer would treat as a literal source key. Existing HTTP(S)/credential checks and duplicate-source detection remain unchanged.
- **Boundaries confirmed:** No network requests, provider calls, state writes, credentials changes, operational-state branch writes, or backup modifications were made.
