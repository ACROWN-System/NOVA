# Active Navigation Plan — NOVA Block 43: Source-Bound, Time-Bounded Cached Analysis

**Date:** 2026-10-29  
**Status:** ACTIVE — reconcile stale PR #143 with the hardened main branch  
**Objective:** Ensure cached analysis is reused only for the exact current observation and within its own validity window, then queue re-analysis without duplicating pending events when provenance is missing, changed, or expired.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Current base branch:** `main`  
**Base commit at start:** `208ad238c9d8f9599988f2e576b14ed89de56b11`  
**Superseded review target:** [PR #143](https://github.com/ACROWN-System/NOVA/pull/143), whose branch is based on an older `main` commit (`7e855a62eaa79db603bb629e980a2395915f86cf`).  
**Working branch:** `fix/source-bound-analysis-cache-2026-10-29`  
**Mode:** Offline tests and focused code changes. No live provider calls, credential changes, external actions, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This record uses the existing `NOVA/research/Active/` plan convention as the available fallback and does not claim to have followed absent files.

## Discovery

PR #143 addresses a real provenance gap: cached analysis could be retained across unchanged observations without a verified source fingerprint; analysis age could be refreshed by repeated observation scans; and legacy cache entries without trustworthy provenance could avoid re-analysis. Its tests passed on its branch, but that branch predates recent changes to health-state loading, duplicate JSON handling, health/roster validation, and related tests. It must not be merged blindly or used to replace current files.

Review also identified a queue/reuse edge case: if a matching current event is already pending, `observe_source()` must not report cache reuse and leave the event pending for the reasoning stage. In this inconsistent state, prioritize resolving the pending analysis event rather than skipping it, while preserving duplicate-event suppression.

## Decision

Port the valid PR #143 changes onto current `main`, preserving newer merged safeguards:

- Record `analysis_fingerprint` and `analysis_observed_at` whenever reasoning succeeds.
- Preserve those fields across unchanged observations only when the fingerprint matches and the analysis timestamp is trustworthy.
- Never reuse analysis with a missing/mismatched fingerprint, an invalid/future timestamp, a stale observation under its freshness policy, or an expired analysis validity window.
- Base analysis TTL on `analysis_observed_at`, not the last-seen observation timestamp.
- Re-queue analysis for invalid provenance or expiry without duplicating an already-pending event for the same source and fingerprint.
- If a current matching event is already pending, do not label the observation as a reusable-cache result; leave the event for the existing reasoning stage to resolve.
- Keep analysis advisory; do not broaden action permissions or invoke providers during offline tests.

## Actions

1. Integrate the reviewed health-memory and cache-validity changes into the current `NOVA/health.py`, retaining Block 42 strict health-state loading.
2. Add analysis timestamp persistence in `NOVA/reasoning.py`, retaining current trust-boundary and JSON validation defenses.
3. Update `NOVA/operational_observer.py` to preserve analysis provenance and avoid duplicate pending event creation, including the pending-event/cache interaction.
4. Add regression tests for fingerprint preservation/mismatch, independent analysis TTL, legacy invalidation, pending-event handling, and no duplicate re-queue.
5. Run the full NOVA Health Tests workflow, inspect the current branch diff, and merge only after passing checks.
6. Close the stale PR #143 as superseded only after the replacement is merged; leave a clear cross-reference.

## Impact analysis

- **Integrity:** Binds analysis to the exact content fingerprint it claims to analyze.
- **Temporal validity:** Repeated scans do not extend an analysis's validity window.
- **Cost/resource use:** Avoids unnecessary provider calls for valid cache reuse and prevents duplicate queue entries; inconsistent pending events remain eligible for controlled re-analysis.
- **Safety:** No increase in autonomous action permissions. Source analysis remains advisory behind existing policy gates.
- **Compatibility:** Legacy entries without required provenance are preserved in bounded history as unverified and re-queued instead of silently trusted.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** A matching fingerprint and valid timestamp establishes cache eligibility only; it does not prove the analysis is factually correct or calibrated.

## Completion evidence

Record the replacement pull request, successful workflow runs, merge commit, and disposition of stale PR #143 here before marking this plan COMPLETE.
