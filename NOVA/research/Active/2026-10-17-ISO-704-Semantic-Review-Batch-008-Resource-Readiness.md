# ISO 704:2022 Preliminary Semantic Review — Batch 008 (NOVA Resource and Capacity Vocabulary)

**Review ID:** NOVA-ISO704-SEM-B008  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR THREE FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob identifiers below  
**Boundary:** This is a terminology, scope and source-consistency review. It is not a live provider qualification, account verification, GPU-capacity measurement, economic validation, or ISO clause-conformity result.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B008-01 | `NOVA/PROVIDER-ACQUISITION-READINESS.md` | `d3727058c5be66fc771a96ae66a4eb9623cd7058` | REVIEWED — strong evidence-state distinctions; cross-document free-tier conflict identified |
| B008-02 | `NOVA/DEVELOPMENT-RESOURCE-READINESS.md` | `0a5ec010a302ac50c0a6957f3027fe4f39210f11` | REVIEWED — useful resource lifecycle/scoping model; table-level freshness fields need improvement |
| B008-03 | `NOVA/GPU-CAPACITY-ACCOUNTING.md` | `96328223b305ab4d16e48f62776e7e4a8a28468f` | REVIEWED — accounting vocabulary is carefully bounded; reliability and usage metering remain unverified |

## 2. Findings

### B008-F01 — Conflicting Hugging Face inference-credit statements across two active NOVA documents

`NOVA/PROVIDER-ACQUISITION-READINESS.md` classifies Hugging Face Inference Providers as **CONFLICTED / DO NOT COUNT AS FREE CAPACITY YET**, noting a discrepancy between an earlier $0.10/month excerpt and a later/current pricing-page audit reporting no included inference credit on the Free plan.

`NOVA/DEVELOPMENT-RESOURCE-READINESS.md`, however, separately describes the Hugging Face Inference Providers free-account allowance as **$0.10/month, subject to change**. The two active documents therefore expose materially inconsistent resource states for the same candidate.

**Required action:** preserve the conservative disposition—do not count the allowance as available capacity while the conflict is unresolved. Reconcile the current official price/account evidence in one dated provider observation, then update both dependent records through a reviewed change. Record the exact claim, model/service, account/plan scope, source observation time and result; do not silently choose one table. This finding concerns NOVA LLM inference credits, not any ISO certification provider.

### B008-F02 — Dynamic quota and free-tier claims need row-level evidence freshness

The files correctly state that free allocations, model catalogs, account limits and provider terms change, that public quotas do not establish account eligibility, and that credentials do not prove activation or capacity. Some table rows nevertheless use terms such as “current”, “required” or list explicit quota figures without placing a source observation date and verification state on the row itself. A general statement later in the document is not enough to show when each table entry was last observed.

**Required action:** for each value that may affect decisions, keep row-level source URL, observation timestamp, scope (credential/project/account/org/provider), evidence type, status (advertised / account-observed / independently tested), expiry or recheck date, and owner. A historical observation must remain recognizable as historical after the provider changes terms. This is an evidence-design improvement; no live account status is asserted by this review.

### B008-F03 — Positive control: resource types and operational states are distinguished

These documents repeatedly distinguish:
- advertised quota from account-verified allocation;
- credential presence from provider activation;
- one-time promotional credits from recurring capacity;
- allocated GPU-minutes from completed useful work;
- LLM calls/tokens from GPU-minutes and dollar credits;
- current non-commercial R&D use from later commercial-production qualification;
- required development capability from provider state/availability;
- quality, latency, reliability and authentication as separate measures.

The GPU capacity specification correctly labels 86,400 GPU-minutes/month as a **provisional, unvalidated comparison reference**, not a requirement, and explicitly says feasibility is not established. Preserve these distinctions: collapsing them would introduce a misleading impression of readiness.

**Caution:** describing this accounting rule is not evidence that the metering pipeline has been implemented, that every provider row is current, or that a reliability score is measured. The GPU capacity document explicitly says empirical reliability and useful-work metering remain incomplete.

### B008-F04 — “Required” is a development role, not an operational status

The resource-readiness table uses `REQUIRED` for minimum development roles, while the same body defines actual resource states such as `REQUIRED_NOT_CONFIGURED`, `CONFIGURED_NOT_VERIFIED`, `VERIFIED_AVAILABLE`, `BLOCKED` and `UNKNOWN`. These are different dimensions but the bare word “required” can be misread as “already configured” or “verified available”.

**Required action:** keep role/need separate from state. When the resource-state table is used, make the role property an explicit field (e.g. `development_role: REQUIRED`) and represent availability state independently. Do not treat the words “minimum resources” or “required” as evidence that quotas/credentials are present.

## 3. Terms and concept-system observations

The GPU accounting document provides a useful domain distinction between a provider's resource allocation, account credits, recurring allowance, one-time credits, reserved time, idle time, useful-work time, unknown/unmetered usage and planning reference. These are not synonyms and should remain distinct concepts if later added to the canonical cross-project register or its domain-specific sub-register.

Likewise, resource readiness, provider qualification, live smoke-test success, response quality, capacity measurement and production readiness denote different decisions. A successful transport/API probe is not a substitute for quality or policy qualification. This aligns with the wider evidence principle but remains internal design evidence, not proof of ISO 704 conformity.

## 4. Evidence and limitations

- Exact baseline blob identifiers are listed above.
- This batch did not access provider accounts, call an external provider API, test quota exhaustion, meter GPU work or independently refresh these dynamic provider facts.
- Provider pricing/eligibility claims remain date-bound assertions in repository documents, not newly verified facts from this review.
- The current evidence documents are proposed controls; they do not prove every control operates.
- No code/configuration or provider roster was changed by this terminology review.
- No ISO 704 clause is assessed because the complete controlled standard baseline remains blocked.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Reviewed NOVA's provider acquisition, development resource and aggregate GPU capacity documents. Recorded one conflicting free-credit status, an evidence-freshness improvement, and distinctions worth preserving.
