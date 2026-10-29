# Active Navigation Plan — NOVA Block 52: Reject Duplicate Keys in Provider Response Envelopes

**Date:** 2026-10-29  
**Status:** ACTIVE — apply consistent duplicate-key protection to external provider JSON  
**Objective:** Ensure provider response envelopes used for health routing, GPU credential qualification, and provider qualification are rejected if they contain duplicate JSON object keys, rather than allowing last-value-wins parsing.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** latest verified `main` following Block 51  
**Working branch:** `fix/reject-duplicate-keys-in-provider-envelopes-2026-10-29`  
**Mode:** Offline tests only; all provider responses are mocked. No provider APIs, credentials, state writes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

NOVA already rejects duplicate JSON keys in persisted state, configuration, reasoning JSON, and the inner model health payload. However, external API response envelopes in `NOVA/router.py`, `NOVA/gpu_heartbeat.py`, and `NOVA/provider_qualification.py` are still parsed with ordinary `json.loads()`. A response with duplicate members such as `choices`, `candidates`, or `usage` is silently interpreted with last-value-wins semantics even though the selected value controls probe validity and persisted usage/diagnostics.

## Decision

Expose a shared `loads_json_no_duplicate_keys()` parser from `NOVA/health.py`, backed by NOVA's existing duplicate-key object hook. Use it for provider success/error envelopes in the LLM router, GPU credential-read-only probe, and provider qualification workflow. Duplicate-key or malformed JSON must continue through each consumer's existing failed/invalid response path; no response is to be reinterpreted by discarding one duplicate value.

Keep request contracts, markers, capability gates, provider ordering, error classification, alert/action policy, and secrets handling unchanged.

## Actions

1. Add the shared strict JSON text parser to `NOVA/health.py`.
2. Use it for successful and error response envelope parsing in `NOVA/router.py`, and successful credential/qualification response parsing in `NOVA/gpu_heartbeat.py` and `NOVA/provider_qualification.py`.
3. Ensure duplicate-key parse errors are caught as invalid/failed responses without raw-body logging or uncaught exceptions.
4. Add offline tests for the shared parser and at least one mocked duplicate-key provider envelope in each affected consumer.
5. Run the full NOVA Health Tests workflow, inspect the focused diff, and merge only after all checks pass.
6. Record PR, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Integrity:** Duplicate JSON object members cannot silently change which provider response field is used.
- **Failover:** Ambiguous provider responses follow existing failure handling instead of being counted as valid health/qualification results.
- **Compatibility:** Proper unique-key JSON responses are unchanged.
- **Resources/cost:** Offline tests only; no live provider requests or new dependencies.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This validates response JSON unambiguity, not factual truth of provider claims or the validity of a unique-key response beyond the existing schema/marker checks.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
