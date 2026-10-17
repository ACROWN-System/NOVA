# ISO 704:2022 Preliminary Semantic Review — Batch 019 (Persisted Health-State Snapshot)

**Review ID:** NOVA-ISO704-SEM-B019  
**Date:** 2026-10-17  
**Status:** PRELIMINARY DATA-RECORD REVIEW COMPLETE; SNAPSHOT STALE FOR CURRENT-STATE CLAIMS  
**Path:** `NOVA/health_state.json`  
**Baseline blob SHA:** `515c37cdb7d2fd9ff63191bd18a49397f486eee9`  
**Related policy blob SHA:** `dda7f34d2ded354b2a3b70605f69df3a14a26a20`  
**Boundary:** This is a structural and evidence-freshness review of persisted records. Raw error text, secret values, and full response bodies are not reproduced in this report. No provider was called and the file was not changed.

## 1. Snapshot summary

The baseline JSON parses successfully and contains:
- schema version 1;
- `updated_at` = `2026-10-11T17:06:28.300191+00:00`;
- 10 target records;
- 116 historical observation rows;
- observation timestamps ranging from 2026-10-07 to 2026-10-11;
- last-observation status counts of 3 UNCONFIGURED, 2 DEGRADED, 2 HEALTHY and 3 UNACCEPTABLE;
- recorded last-authentication values including NOT_CONFIGURED, UNKNOWN and PASS;
- 94 history rows with a non-empty `error_detail` value.

The health policy sets `heart_observation_max_age_seconds = 21600` (six hours) and explicitly states that a stale observation is not proof of the underlying state being false.

At the 2026-10-17 assessment date, **zero of the 116 historical observation rows were within the six-hour freshness window**. The newest stored observation was over five days old. The JSON is valid historical evidence, but none of its statuses should be presented as current provider health, credential state, API validity or availability.

## 2. Findings

### B019-F01 — Last stored health state is stale and cannot be used as current provider evidence

The top-level timestamp and newest observation are dated 2026-10-11. The configured freshness limit is six hours. Every observation in this baseline is outside that policy window at this review date. A displayed `HEALTHY` state can therefore mean only “healthy under this historical observation”; it is not current `HEALTHY` evidence.

**Required action:** keep the historical record intact, but ensure every summary consumer applies the health policy's freshness window and labels outdated states STALE/UNKNOWN for current decisions. The evidence package should record the snapshot's cutoff date and require a fresh permitted observation before any current-provider claim. Do not rewrite old event history or infer that a provider is now healthy or unhealthy from this stale file.

### B019-F02 — Durable error detail remains a distinct retention path

The snapshot includes 94 history rows with non-empty error detail. The record contains truncated provider-error material alongside sanitized class/status labels. A targeted heuristic scan of the retained details found no common bearer/API-key or email-pattern matches, but that is not proof the records contain no sensitive data: truncation is not a sanitizer and a pattern screen is incomplete by definition.

**Required action:** track this against B016-F02. Review the error-body persistence path and introduce or verify explicit allowlisting/redaction before durable storage; add tests showing representative secret/PII markers cannot be written to health history. Do not say a real secret leak occurred based on this review, and do not classify the entire telemetry file as fully sanitized.

### B019-C01 — Evidence dimensions are structurally distinct

The last-observation schema separates provider/model identity, credential environment-variable name, API status, authentication, response validity, quality status, health status, error class/detail, latency/baseline, action, observation time and (for some targets) capacity/rate-limit evidence. Response headers in the sampled snapshot are limited to a small set of rate-limit/request-ID names rather than all headers.

This is a useful schema for audit traceability, provided the values remain fresh enough for the intended decision and error-detail content is addressed.

### B019-F03 — Historical model/provider identities may outlive current configuration

The snapshot contains target identities for model variants that may no longer be configured as active providers/models. The historical target name and its past result must not be interpreted as proof the model remains on the current roster. The correct current roster is a separate source-of-truth artifact; the state history is retained for traceability.

**Required action:** when generating current dashboards/reports, join historical targets to the current roster/lifecycle configuration without deleting legacy target history. Distinguish current, deprecated, deferred and historical-only identifiers. Treat orphaned histories as history, not automatic configuration or authority.

## 3. Disposition

- Structural validity: JSON parses successfully.
- Data freshness at assessment date: STALE for current-state use.
- Historical evidence: retain with exact snapshot SHA and timestamp.
- Credential privacy: no obvious common token/email pattern was detected in the bounded screen, but this is not proof of complete sanitization.
- Current provider availability, quota, terms eligibility, cost, or capacity: NOT ESTABLISHED by this file.
- No data, credential, roster or runtime status was modified.
- No ISO 704 clause result is assigned; the complete controlled standard baseline remains blocked.

## 4. Evidence links

- [Persisted health-state snapshot](https://github.com/ACROWN-System/NOVA/blob/main/NOVA/health_state.json)
- [Health policy and freshness limit](https://github.com/ACROWN-System/NOVA/blob/main/NOVA/health_policy.json)
- [Router/health/capacity review Batch 016](2026-10-17-ISO-704-Semantic-Review-Batch-016-Router-Health-Capacity.md)

## 5. Revision history

- **2026-10-17 / v0.1.0:** Parsed and assessed the main-branch health-state snapshot without disclosing stored error text. Established that the full snapshot is stale under its own six-hour policy and flagged durable error-detail handling for separate redaction tests.
