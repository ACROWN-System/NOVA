# Active Navigation Plan — NOVA Block 50: Restrict Watchlist URL Schemes and Credentials

**Date:** 2026-10-29  
**Status:** ACTIVE — constrain external observation fetching to the intended HTTP(S) boundary  
**Objective:** Ensure watchlist URLs cannot select unrelated URL handlers or embed credentials that may be retained in persisted observation metadata.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** latest verified `main` following Block 49  
**Working branch:** `fix/restrict-watchlist-url-schemes-2026-10-29`  
**Mode:** Offline validation tests only; no source fetches or persistent state writes. No live provider requests, credentials changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed those absent files.

## Discovery

Block 49 validates that watchlist URLs are absolute and non-duplicated, but currently accepts any URL scheme as long as `urlsplit()` returns a scheme and network location. `fetch_text()` calls `urllib.request.urlopen()`, which is a general URL opener rather than an HTTP-only client. The validator should not allow the watchlist to select unrelated handlers such as `file:` or `ftp:`.

The current validation also permits URL userinfo (for example, `https://user:password@example.invalid/path`). URLs are stored in observation records and may be persisted in the dedicated operational-state branch, so embedded credentials could become retained or disclosed as part of normal source metadata.

## Decision

Restrict watched sources to absolute `http://` or `https://` URLs with a valid hostname and optional valid port. Reject userinfo (username or password fields) in URLs. Keep duplicate URL normalization, source identity checks, response-size limits, and untrusted-content handling unchanged. The validator must reject invalid URLs before health-state loading or any network request.

## Actions

1. Tighten `validate_watchlist()` in `NOVA/operational_observer.py` to permit only HTTP(S), require a hostname, validate port parsing, and reject URL userinfo.
2. Add offline tests for `file://localhost/...`, `ftp://...`, missing host, invalid port, and HTTP(S) userinfo.
3. Extend the runner test to prove rejected protocols/userinfo do not load operational state or call `urlopen`.
4. Run the full NOVA Health Tests workflow, inspect the focused diff, and merge only after all checks pass.
5. Record the PR, workflow runs, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Security boundary:** Prevents unrelated URL schemes from selecting non-HTTP URL handlers.
- **Credential hygiene:** Rejects credentials embedded in source URLs before they can be retained as source metadata.
- **Compatibility:** HTTP(S) URLs without userinfo remain supported; duplicate/source identity behavior is unchanged.
- **Availability:** Invalid URL entries fail explicitly before state access or fetch, requiring watchlist repair.
- **Resources/cost:** Offline tests only; no network requests or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This does not prevent access to every possible private or sensitive HTTP endpoint. The watchlist remains trusted configuration and source content remains untrusted data.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
