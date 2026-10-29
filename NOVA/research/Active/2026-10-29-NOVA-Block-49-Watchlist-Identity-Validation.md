# Active Navigation Plan — NOVA Block 49: Reject Ambiguous Watchlist Sources

**Date:** 2026-10-29  
**Status:** ACTIVE — prevent multiple external sources from sharing one observation/event identity  
**Objective:** Validate watchlist structure and require unique normalized source identities and URLs before NOVA reads or fetches any watched source.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** latest verified `main` after Block 48  
**Working branch:** `fix/reject-ambiguous-watchlist-sources-2026-10-29`  
**Mode:** Offline regression tests; all source-fetch and state access are mocked or stopped before execution. No live external GETs, provider calls, credentials changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed those absent files.

## Discovery

`NOVA/operational_observer.py` uses `source.get("name") or source.get("url")` as the source identity, and stores memory under `external-annotation:{identity}`. The watchlist loader validates that the JSON root is an object but does not validate the type or identity uniqueness of the `sources` array.

If two entries use the same name but different URLs, the second observation overwrites the same memory record and may mark the first source's pending event superseded. The first source can therefore lose its own current observation and may never be analyzed. Duplicate URLs under different names can also cause redundant external reads and conflicting histories.

## Decision

Validate the entire watchlist before loading operational state or making any HTTP request:

- Require `sources` to be a JSON array and each source entry to be a JSON object.
- Require every source to have a non-empty absolute URL string.
- If `name` is supplied, require a string; use a trimmed, case-folded name as its identity. If no usable name is supplied, use the URL as the identity.
- Reject duplicate normalized source identities and duplicate URLs. Normalize only URL scheme and authority case; preserve path, query, and fragment case.
- Keep source-fetch behavior, timeouts, response limits, analysis policy, and event semantics unchanged for valid unique watchlists.

## Actions

1. Add a watchlist validator in `NOVA/operational_observer.py` and call it before health-state loading or source fetching.
2. Add offline tests for duplicate names, duplicate URLs, wrong source-list types, and malformed source entries.
3. Prove the runner does not load or mutate state and does not fetch any source when validation fails.
4. Run the full NOVA Health Tests workflow, review the diff, and merge only after all checks pass.
5. Record the pull request, workflow evidence, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** Prevents two configured sources from sharing a memory/event identity.
- **Cost/resource use:** Prevents accidental repeated reads of the same URL due to duplicate watchlist entries.
- **Availability:** Invalid watchlists fail before state access or external requests and require repair.
- **Compatibility:** Valid watchlists with unique source identities and URLs retain existing behavior; missing names may still use the URL as identity.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates source identity/shape, not the truth or trustworthiness of fetched content. External content remains untrusted reasoning input.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
