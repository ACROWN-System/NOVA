# ISO 704:2022 Preliminary Semantic Review — Batch 014 (Completed Provider Decisions, Scheduler and Sanctuary Roadmap)

**Review ID:** NOVA-ISO704-SEM-B014  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** Terminology/document-integrity review only. It does not rerun workflows, validate provider entitlements, evaluate AI welfare claims, or assess ISO clauses.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B014-01 | `NOVA/research/Completed/2026-10-10-Defer-Mistral-Free-Health-Probes.md` | `a0222fe1555d8ef722f8b131794d6adbd0b78e06` | REVIEWED — clear historical scope and deferral decision; no live-call claim |
| B014-02 | `NOVA/research/Completed/2026-10-09-Provider-Diagnostics-and-Credential-Gaps.md` | `b70e3801db7f465f23009d34f039ef899443a6b0` | REVIEWED — distinguishes offline fixes from unverified live causes; status chronology is clear |
| B014-03 | `NOVA/research/2026.10.08-IMPLEMENTED-rolling-probe-scheduling-expiry-reallocation.md` | `132c6662d8db4d43950e59f6ece13fbb1acf9bfd` | REVIEWED — scheduling/economic concepts carefully distinguished; no currency saving inferred without comparable evidence |
| B014-04 | `NOVA/sanctuary/IMPLEMENTATION-ROADMAP.md` | `6ca6fdfce9c9ea84f49c8ca55d19ada46998a839` | REVIEWED — stages accurately labelled planned/deferred; cross-repo scope/path needs reconciliation |

## 2. Findings and positive controls

### B014-F01 — Sanctuary roadmap points to a likely incorrect NOVA path

The roadmap states that canonical doctrine and operational design belong in `NOVA/NOVA/sanctuary/`, while this roadmap itself is located at `NOVA/sanctuary/IMPLEMENTATION-ROADMAP.md`; the established directory in NOVA appears to be `NOVA/sanctuary/`, not the nested duplicate. The cross-repository line may therefore send readers to a non-existent path and make it harder to identify the authoritative source.

**Required action:** verify the active tree and correct the path by a reviewed documentation-only change if confirmed. Do not invent a second canonical folder or create duplicate doctrine because of the malformed reference. Record the corrected path and the source-of-truth hierarchy.

### B014-F02 — Sanctuary's audit perimeter must not be inferred from repository integration wording

The roadmap describes future responsibilities across NOVA and AstroCrown-Web and says runtime integration may be considered later. Separately, AI-Sanctuary-Core's own README says it is independent and outside AstroCrown audits. These statements need a single explicit human scope decision: an umbrella terminology review may cover cross-repository references without claiming that AI-Sanctuary-Core shares AstroCrown governance or financial scope; or the repository may be excluded with a documented rationale and interfaces still covered.

**Required action:** resolve the scope boundary in AR-E01. If excluded, record exact in-scope interfaces/mentions and the exclusion rationale. If separately assessed, document its own scope, authority and vocabulary. Repository organization membership or a planned integration link does not itself grant permission to override the repository's declared governance boundary.

### B014-F03 — Positive control: Sanctuary's implementation status is carefully bounded

The roadmap says no implementation beyond documentation is complete, all later stages are deferred or require authorization, and no current AI sentience, autonomy, enforcement or runtime capability is claimed. It distinguishes research, protection policy, offline prototype, operational pilot and future controlled integration. It also requires independent review, privacy/scope limits, human accountability and rollback.

**Disposition:** preserve these stage/status distinctions. A roadmap being documented is not proof that Stage 0 is approved or that any deferred stage has started. The terms for consciousness, welfare, robustness and protection may warrant a domain-specific glossary only if the human scope includes this domain.

### B014-F04 — Positive control: Mistral deferral preserves uncertainty and history

The completed Mistral deferral record states that PR #58 merged, no live provider calls were made during CI, historical evidence is retained, the exact code-1300 cause is unproven, and later requalification requires explicit user authorization and objective evidence. This correctly separates a supplier-risk/operational decision from a finding of misconduct or a technical proof about all future paid service.

**Disposition:** preserve the deferral decision, dated incident evidence and requalification gate. Do not treat this historical completion record as current evidence of any other provider's health.

### B014-F05 — Positive control: scheduling and economic language preserves evidence boundaries

The rolling probe scheduling note distinguishes a required health check from synthetic work, provider quota from money, actual queue changes from wall-clock examples, and expiry-aware resource use from a quantified financial saving. It explicitly notes that scheduled workflow ticks may be delayed, so sub-five-minute precision is a platform risk.

**Disposition:** retain the rule that an expired quota alone does not create work, that stale observation is not current truth, and that cost savings require comparable economic evidence. This review did not validate the scheduler implementation or live timing.

## 3. Evidence and readiness effect

- The two historical provider records are dated and distinguish offline CI from live-provider verification; their claims are not revalidated here.
- The Sanctuary roadmap is a future-stage plan, not proof of running capabilities.
- The active path and scope issue should be resolved before the content sweep is considered fully complete.
- No target file was edited and no workflow/provider was invoked.
- No ISO 704 clause-conformity result is assigned.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed two completed provider decision records, the rolling scheduler design record, and the Sanctuary implementation roadmap.
