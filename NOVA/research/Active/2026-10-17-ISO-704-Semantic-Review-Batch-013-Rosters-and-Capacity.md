# ISO 704:2022 Preliminary Semantic Review — Batch 013 (Provider Roster, Health Policy and GPU Evidence Records)

**Review ID:** NOVA-ISO704-SEM-B013  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** This is a terminology, schema and evidence-state review. It is not a live provider qualification, GPU-account validation, financial assessment, or ISO clause-conformity finding.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B013-01 | `NOVA/roster.json` | `8cf9bac1c6a8d47568c5183177818b5a53ab1987` | REVIEWED — active/deferred/candidate distinctions present; current naming and candidate provenance need reconciliation |
| B013-02 | `NOVA/gpu_roster.json` | `71d8742cf53a1baa778d2833b8122eb3e77239ec` | REVIEWED — active provider list empty; candidate-specific and read-only boundaries explicit |
| B013-03 | `NOVA/health_policy.json` | `dda7f34d2ded354b2a3b70605f69df3a14a26a20` | REVIEWED — freshness and protected action rules are explicit; current policy remains design evidence, not runtime proof |
| B013-04 | `NOVA/gpu_capacity_evidence.json` | `2bdc37d79b4ed5ee84b2b4cec4289f86d7c854ee` | REVIEWED — rich evidence states and no-double-counting rule; Lightning no-card field needs an unambiguous resource scope |

## 2. Findings

### B013-F01 — Active roster comment retains HAAN Council naming

The active LLM roster comment says a provider-down marker may be restored by the “HAAN Council” after approving a replacement. The recorded naming decision prefers HSIAN for current terminology, but the dependent rename/integration work remains pending.

**Required action:** update this active comment only through the reviewed naming integration, preserving any historical governance text that requires it. The machine roster must not be treated as authority to rename an actual governance body; verify the applicable charter/decision record first. Until integrated, track it as a legacy current-path occurrence.

### B013-F02 — Candidate catalog uses free-form strings rather than consistent candidate records

The LLM roster correctly separates active providers from `candidates_not_in_roster`, and most candidate notes warn that current free access, data rights, payment-method eligibility or quotas remain unknown. However, candidate entries are free-form strings with inconsistent fields and timestamp/source granularity. Some include checked dates and explicit status, while others report “current” quotas or possible no-card access without a clearly scoped observation time, verification level or explicit lifecycle state. The list mixes direct model providers, gateways/aggregators, specialized APIs and community/volunteer services.

**Required action:** when maintaining the candidate catalog, use a consistent record schema with, at minimum, candidate ID/name, role (direct provider/gateway/aggregator/specialized service/community resource), upstream dependence when known, capability class, source URL, observation date, claim type (officially advertised / account-observed / tested), no-card/payment state, current-use/rights state, privacy/data boundary, availability status, and explicit blockers. Do not count an aggregator as independent upstream capacity or a directory claim as an account entitlement. Keep candidates excluded from the active routing roster until their required qualification gates pass.

This is an evidence-structure finding; this review does not refresh or endorse any candidate provider claim.

### B013-F03 — Lightning AI no-card field may overstate the GPU-credit evidence

The GPU evidence register labels Lightning AI's `free_without_payment_method` as `VERIFIED`, while the same record says the official pricing page and AI Studio guide conflict on the free allowance, that the pricing FAQ says the additional 25 credits require a card, that account GPU allocation is unverified, and that the actual no-card GPU allowance/recurrence must be checked. The wording does not make clear whether “VERIFIED” means only that an account can access a free CPU Studio or register without a card, or that actual GPU credits are usable without a card.

**Required action:** split these propositions into distinct fields. For example: account creation without card; free CPU workspace access without card; GPU-credit balance without card; selected-GPU allocation available without card; and prevention of paid overage. Mark each independently with evidence/date. Until the exact GPU-credit entitlement is established, its GPU capacity remains unverified and must not count toward recurring or one-time usable GPU-minutes.

### B013-F04 — Positive control: capacity types and measurement gaps are explicit

The GPU evidence register distinguishes advertised theoretical allowance from verified recurring capacity, active recurring capacity, one-time credits, reserved time, idle time, completed useful work and unknown/unmetered usage. Candidate rows carry source URLs/dates, account/use qualification dimensions, observed-at/valid-until placeholders and explicit NOT_RUN / UNKNOWN / UNVERIFIED states. The provisional 86,400-minute value is expressly marked unvalidated and not a requirement.

The GPU roster also states that a read-only token check does not establish a GPU allocation, and that provider-specific adapters are required. The health policy states that stale observations do not prove the underlying state is false, while an outdated observation cannot stand in for fresh evidence.

**Disposition:** preserve these controls. A structured evidence record is not proof the entry itself has been account-validated; its state values must remain honest and current.

## 3. State semantics

These records use several dimensions that should not be collapsed into one boolean:
- lifecycle/roster status: active, deferred, candidate, unconfigured;
- credential state: missing, configured, authenticated;
- terms/account eligibility: known, unknown, blocked, or verified for a defined use;
- model/API contract: blocked, verified for a specific model/operation, or not tested;
- resource amount: advertised, account-observed, recurring, one-time, reserved, used, or unknown;
- evidence freshness: source-observation date, observed-at time, and expiry/valid-until;
- intended-use scope: current non-commercial R&D versus future commercial-production qualification.

Where a field label such as `free_without_payment_method` could represent more than one condition, its schema needs explicit definition and unit/scope semantics.

## 4. Evidence and limitations

- These are current-main configuration/evidence files at exact blob SHAs, not live account results.
- No credentials or account balances were read, no live probes were called, and no roster activation change was made.
- The current provider/roster data must be separately refreshed after relevant PR merges or account observations.
- No ISO 704 clause result is assigned; the complete controlled standard baseline remains blocked.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Preliminary review of the LLM roster, GPU roster, health policy and GPU-capacity evidence register; recorded the legacy HAAN label, candidate-catalog structure and ambiguous Lightning no-card/GPU entitlement field.
