# Active Navigation Plan — NOVA Block 54: Strict Alert API JSON Responses

**Date:** 2026-10-29  
**Status:** ACTIVE — prevent ambiguous alert API responses from influencing issue deduplication or notification bookkeeping  
**Objective:** Reject duplicate JSON object keys in GitHub and Twilio API responses consumed by NOVA alerts, with particular care that ambiguous issue listings never cause NOVA to create or comment on an issue using last-value-wins interpretation.

## Navigation and source of truth

**Repository:** https://github.com/ACROWN-System/NOVA  
**Base branch:** `main`  
**Base commit at start:** `50dbf5f0e55376111a62843ca4eadcfa6e3f92f9`  
**Working branch:** `fix/strict-alert-api-json-responses-2026-10-29`  
**Mode:** Offline mocked-response tests only. No GitHub issues/comments, Twilio calls, live provider requests, credential changes, operational-state branch writes, or backup modifications.

The current repository tree does not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This plan follows the existing `NOVA/research/Active/` convention as the available fallback and does not claim to have followed absent files.

## Discovery

`NOVA/alerts.py` consumes GitHub issue-listing, issue-comment, issue-creation, and Twilio message/call response bodies using ordinary `json.loads()`. A response containing duplicate object member names is silently interpreted by last-value-wins parsing. In the issue-listing path, the resulting data controls which open issue NOVA reuses versus whether it creates a new issue. Ambiguous provider/API JSON must not be treated as reliable deduplication evidence.

## Decision

Use the shared `loads_json_no_duplicate_keys()` helper for all alert API response bodies. A duplicate-key or invalid response must follow the existing failure path. In particular, a GitHub open-issue listing that cannot be parsed strictly must fail closed without issuing a comment or creating an issue.

Keep issue-title matching, pull-request exclusion, comment/create flow, severity thresholds, alert message content, and Twilio credential policy unchanged.

## Actions

1. Import `loads_json_no_duplicate_keys()` in `NOVA/alerts.py` with support for package and direct-script execution.
2. Replace all four ordinary response-body JSON parses in the alert module with the shared strict parser.
3. Add an offline test with duplicate keys in the GitHub open-issue listing; assert that `send_github_issue()` returns false and performs no POST.
4. Run the full NOVA Health Tests workflow, review the changed-file diff, and merge only after checks pass.
5. Record the PR, successful regression workflows, and merge commit here before marking this plan COMPLETE.

## Impact analysis

- **Alert deduplication integrity:** An ambiguous listing cannot silently choose which issue record NOVA acts upon.
- **Failure handling:** Invalid response bodies use the existing guarded alert failure path.
- **Compatibility:** Valid unique-key GitHub/Twilio responses behave unchanged.
- **Resources/cost:** Offline tests only; no live API or SMS/voice calls.
- **Secrets/backups:** Unchanged.
- **Scope boundary:** This verifies JSON unambiguity, not the truth of an API response or completion of a remote side effect when the response itself is malformed.

## Completion evidence

Record the pull request, successful regression workflows, final review, and merge commit here before marking this plan COMPLETE.
