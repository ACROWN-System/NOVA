# Active Navigation Plan — NOVA Block 47: Bounded Reasoning Retry and Recovery

**Date:** 2026-10-29  
**Status:** COMPLETE — PR #159 merged after successful regression-test workflows  
**Objective:** Avoid permanently losing a valid pending analysis after a transient provider failure, while limiting repeated provider usage and not charging the retry budget for failures that never reached an API request.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `d798a05d3f54022241dc62b974f6f07940932670`  
**Working branch:** `fix/bounded-reasoning-retries-2026-10-29`  
**Mode:** Offline tests only; provider calls, alerts, and persistent state writes mocked. No live API calls, secrets changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/reasoning.py::analyze_pending()` currently changes an event from `PENDING` to terminal `BLOCKED` as soon as the configured providers fail to produce a valid reasoning response. The observer only queues unchanged observations when analysis is invalidated or a current pending event already exists; it does not re-queue a blocked event with the same fingerprint. A transient 429/5xx/network failure can therefore permanently strand the source analysis even when the provider recovers. No bounded retry or recovery policy is currently recorded for reasoning events.

Repeated retries must also be controlled: a failed analysis cycle can call several providers/models. Retrying indefinitely could unnecessarily consume free quota or spend money after configuration mistakes.

## Decision

Add a policy-defined maximum number of reasoning cycles per event (default configured to 3). Count a cycle only when at least one provider request actually reached an API attempt, identified by an HTTP status or measured latency in the probe records.

- For a failed reasoning cycle below the limit, keep the event `PENDING` and record a sanitized attempt timestamp/status/reason so the next scheduled heartbeat may retry it.
- At the limit, mark the event `BLOCKED` with `retry_exhausted` and a clear reason, preventing unbounded provider use.
- If every provider was locally skipped (missing credentials, unsupported model contract, or other no-request gate), keep the event `PENDING` without incrementing the attempt count; record a configuration/capability wait status.
- If no active providers are available before provider selection, retain the current behavior: leave pending work untouched and make no provider calls.
- Successful analysis remains source-bound and follows existing action-policy gates.

## Actions

1. Add `reasoning.max_attempts_per_event` to the trusted health policy with a limit of 3.
2. Validate that the retry policy is a positive integer and not a boolean.
3. Add failure-state handling in `NOVA/reasoning.py` to distinguish real provider attempts from local skips, preserve pending status below the limit, and terminate only after the configured limit.
4. Add offline tests for retry-pending → retry-exhausted progression, no-request failures not consuming budget, and no provider calls after exhaustion.
5. Run the full NOVA Health Tests workflow, inspect the diff, and merge only after checks pass.
6. Record the PR, successful workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Recovery:** Temporary provider failures no longer permanently strand an analysis after the first unsuccessful cycle.
- **Cost control:** Provider use is capped per event by trusted policy; no-request gates do not consume retry count.
- **Availability:** Exhausted events remain visibly blocked rather than retrying indefinitely. Re-analysis of materially changed source content still creates a new fingerprint/event through the existing observer.
- **Safety:** No autonomy or action permissions change; AI analysis stays advisory under current policy.
- **Compatibility:** Existing events without an attempt count start at zero; absent retry policy defaults to a small fixed maximum.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This controls retries; it does not assert provider health from a failed reasoning response or automate manual review.

## Completion evidence

- **Pull request:** https://github.com/ACROWN-System/NOVA/pull/159 — squash-merged.
- **Merge commit:** `130d118c1d34212f5c24df0194f46e2e227c306d`.
- **Push workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833533253 — NOVA Health Tests passed on head `a7e4a77febe663ae35a4a41ee00f9611ca6ee478`.
- **Pull-request workflow:** https://github.com/ACROWN-System/NOVA/actions/runs/40833577720 — NOVA Health Tests passed on the same head commit.
- **Regression evidence:** All 195 offline tests passed. New tests cover retry-pending then retry-exhausted behavior, no provider calls after exhaustion, no-request attempts not consuming budget, and invalid retry-policy rejection.
- **Review:** Retry limit is read from trusted `health_policy.json`; it must be a positive integer (booleans are rejected). Each reasoning cycle only counts when a probe contains an HTTP status or measured latency. Missing credentials or locally blocked models remain pending without consuming the attempt budget.
- **Boundaries confirmed:** No live provider calls, alert emission, real state-file writes, credential changes, operational-state branch writes, or backup modifications were made.
