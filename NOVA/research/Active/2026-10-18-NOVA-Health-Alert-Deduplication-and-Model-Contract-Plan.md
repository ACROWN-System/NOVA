# Active Plan — NOVA Health-Alert Deduplication and Model-Specific Contract Gating

**Date:** 2026-10-18  
**Status:** ACTIVE — implementation and regression verification  
**Repository:** ACROWN-System/NOVA  
**Branch:** fix/nova-health-alert-root-cause-2026-10-18  
**Objective:** Stop repeated invalid health-probe configurations from consuming quota and opening dozens of duplicate issues; preserve valid fallback models; keep automated alerting within the $0-only policy.

## Existing-state evidence

- NOVA's current main-branch `NOVA/alerts.py` calls GitHub's issue-creation endpoint for every alert and does not look for an existing open issue of the same identity.
- `NOVA/router.py` raises an alert every time an observation reports `UNACCEPTABLE`, with no health-state transition guard. It supplies severity `urgent`, which invokes both SMS and voice channels through Twilio as well as GitHub issue creation. The Twilio implementation explicitly notes that SMS/voice are not free at production scale and rely on trial credit. This is not safe under the current $0-only operating boundary.
- The current operational-state branch's last observations (2026-10-17) show Groq `openai/gpt-oss-120b` repeatedly returning HTTP 400 `tool_use_failed`, while Groq `openai/gpt-oss-20b` returned HTTP 200 with the exact required JSON health contract. Gemini `gemini-3.8-flash` had a high failure streak and most recent HTTP 200 with `INVALID_JSON`, while `gemini-3.1-flash-lite` returned HTTP 200 and passed the JSON contract (though latency may still affect its health classification).
- The same main-branch issue queue contains 63 repetitive automated alerts: 26 for Groq 120B, 11 for Groq 20B, 22 for Gemini 3.8 Flash, and 4 for Mistral. Mistral has already been formally deferred from the active roster under the user-approved $0/no-payment-method policy.
- These are observations of the probe/model contract, not proof that Groq or Gemini as providers are wholly unavailable. Model-level capability and provider-level health must remain distinct.

## Scope

1. Add model-specific structured-JSON contract records for Groq 120B/20B and Gemini 3.8 Flash/3.1 Flash Lite based on observed evidence.
2. Apply the same pre-network `model_capability_decision` gate to Gemini as already exists for OpenAI-compatible providers. Models not marked `VERIFIED` must be blocked before a network call.
3. Record alerts only on a transition into `UNACCEPTABLE`, not every observation in an existing failure streak.
4. Use model-specific health alert titles so different models are not conflated.
5. Deduplicate open GitHub health issues by exact alert title; when a matching issue is already open, append a comment to preserve the new episode evidence instead of creating another issue.
6. Change automated health alerts to the GitHub-only `notice` channel. SMS/voice must not be triggered by a routine automated health probe without separate explicit cost authorization.
7. Add offline regression tests for contract gating, malformed non-object JSON, alert transition behavior, deduplication, and the no-Twilio severity choice where practical.
8. Preserve old issue contents as history; after merge and confirmed behavior, close resolved/historical alert issues with specific, truthful reasons. Never delete issue history.
9. No backups/archive paths may be modified. No secret, credential, billing setting, live-provider probe, or outbound SMS/voice call will be used during branch implementation or offline tests.

## Acceptance and non-regression criteria

- Verified structured-JSON models remain eligible; unverified model contract cannot reach the HTTP transport.
- A model-level block does not disable a different model from the same provider when that model has a separate verified contract record.
- The JSON validator returns a deterministic failure result for non-object JSON rather than raising an accidental attribute error.
- An existing `UNACCEPTABLE` streak does not produce a new GitHub issue on every sample; a future transition after recovery can generate one new alert.
- If an alert issue already exists and is still open, record new transition evidence on that issue instead of creating another open duplicate.
- Automated provider-health issues remain available through GitHub, but do not trigger potentially billable SMS/voice.
- Unit tests and compile checks pass; evidence of behavior is tied to exact PR head SHA. No live provider or paid-channel call is required to verify the patch.
- Do not classify a model as permanently defective; use `BLOCKED_UNVERIFIED` until requalification.
- Keep model capability state distinct from health state and provider availability.

## Implementation approach

- Keep existing roster model IDs and history. Add explicit `model_contracts` rather than deleting models or rewriting provider identity.
- Use exact probe pass/failure observations from `nova-operational-state` as evidence; these do not prove general model reliability, only whether the model satisfied this narrow required health response contract.
- Make alerts idempotent and recovery-aware without suppressing the first transition alert.
- Do not run the heartbeat manually or invoke provider APIs for this change. The pull-request pipeline should be offline-only; review the live-on-push trigger and $0 boundary before merge.
- Close the four Mistral issue records only as no longer planned, because Mistral is already deferred by explicit policy; preserve their diagnostic payloads and explain why they are closed.

## Impact Analysis

**IF modified:** repeated identical failures stop generating a noisy flood of issues and repeated potentially billable notifications; ineligible model/contract combinations stop before consuming provider quota; successful fallback models remain usable with separate evidence; root cause is addressed instead of hiding symptoms.

**IF not modified:** every heartbeat can create more issues for the same unchanged fault, SMS/voice may be invoked despite the $0-only boundary, and a failing model can repeatedly consume requests while healthy alternatives exist.

## Write and verification controls

- All GitHub writes explicitly specify `fix/nova-health-alert-root-cause-2026-10-18`.
- After each file write, fetch the exact path using that branch and confirm the returned content matches.
- Do not touch paths under any backup/archive directory, regardless of capitalization.
- Do not merge the code change until tests pass and the proposed workflow-trigger behavior and cost boundary are recorded.
