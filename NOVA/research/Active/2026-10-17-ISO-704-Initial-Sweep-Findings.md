# ISO 704:2022 Initial Active-Content Sweep Findings

**Document ID:** NOVA-ISO704-FIND-001  
**Version:** 0.1.1  
**Snapshot date:** 2026-10-17  
**Status:** INITIAL FINDINGS — lexical screening only; not a completed conformity audit  
**Scope source:** [Proposed Scope and Repository Inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md)  
**Tracker:** [File-by-File Content Sweep Tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json)  
**Targeted reviews:** [Certification-Context Review](2026-10-17-ISO-704-Certification-Context-Review.md); [Canonical Register Quality Review](2026-10-17-ISO-704-Register-Quality-Review.md); [Candidate Concept-Relation Map](2026-10-17-ISO-704-Concept-Relation-Map-Draft.md); [HSIAN Pilot Entry Review](2026-10-17-ISO-704-Pilot-Entry-Review-HSIAN.md)

## Method and limitations

This record captures an automated exact-pattern lexical screen of all 318 inventoried active file paths on the six repositories' recorded default-branch `main` tree snapshots. Exact content was retrieved by the file/blob interface and checked for selected canonical labels, old/new naming variants, certification/compliance language and selected concept phrases. The scan is a discovery aid only. It does **not** decide whether each occurrence is semantically correct or current, does not complete the semantic term-by-term human review, does not replace the full-standard matrix, and is not an independent audit.

The six-repository inventory contains 318 active file paths. All 318 now have a lexical-screen record in the tracker and no Git-blob fetch failed. Every tracker row remains `content_review_status: NOT_REVIEWED` and `terminology_assessment: NOT_ASSESSED` until a substantive entry-level content review and reviewer decision are recorded. The lexical scan does not constitute that review.

No backup/archive paths were scanned as active targets or modified. Historical/backup files remain immutable and outside the active sweep.

## Finding register

### SWEEP-F-0001 — Active HAAN naming remains in current NOVA main branch

- **Status:** OPEN — known dependency / rollout pending
- **Severity for readiness:** Blocking to a claim that the active terminology sweep is complete
- **Evidence source:** `ACROWN-System/NOVA`, `NOVA/HAAN-FOUNDATIONAL-MISSION-AND-COLLECTIVE-PRESERVATION.md`, main-branch blob SHA `094ab057dfda0734730398a214aae88b0f9a334d`.
- **Observed result:** lexical scan found 16 occurrences of `HAAN`, including in the title and active mission text, and zero occurrences of `HSIAN` in that file.
- **Context:** NOVA PR #122 proposes the HSIAN canonical naming rollout, including this old path and a new HSIAN-named document. Dependent AstroCrown-Web PR #134 contains related active-document updates. Both are still drafts at this snapshot.
- **Interpretation:** this is a known active-terminology transition gap, not an unexpected new naming decision and not yet a clause-level ISO 704 finding. Because the naming rollout is not merged, the old name must not be silently mass-edited as a shortcut.
- **Required action:** review and resolve PR #122 and PR #134 in their intended dependency order; afterward refresh the active-path inventory and re-scan all affected paths for stale current-use labels. Retain historical references where legitimately needed and never edit backup/archive paths.
- **Closure evidence:** reviewed/merged change history plus a post-merge path and usage scan documenting all remaining occurrences and whether each is historical, deprecated, or current.

### SWEEP-F-0002 — Oversized active NOVA README requires semantic/section-level review

- **Status:** LEXICAL SCREEN COMPLETE; SEMANTIC/SECTION REVIEW BLOCKED
- **Severity for readiness:** Blocking to complete semantic coverage
- **Evidence source:** `ACROWN-System/NOVA`, `NOVA/README.md`, baseline blob SHA `54f8841675190c77ca7a4cbae3d9112f9fe49e90`, recorded size 1,452,321 bytes.
- **Observed result:** the ordinary line-range fetch returned no content for this large file, but a full Git blob fetch subsequently succeeded and the lexical scan has been completed. The tracker includes its term counts (including a high number of compliance/conformance-stem matches).
- **Interpretation:** lexical-screen completion does not establish what individual historical or embedded sections mean, whether claims are current, or whether repetitive/composite material should be segmented for the terminology register.
- **Required action:** perform a segmented semantic/section review using the full blob, record segment boundaries and review coverage, identify embedded/duplicated snapshots, current versus historical statements, inconsistent terms and unsupported claims. Do not treat the file as one coherent current source merely because it is a single path.
- **Closure evidence:** a range/section review manifest covering the entire file, contextual assessment of lexical findings, recorded conflicts/duplicates and claims, disposition decisions, reviewer and retests.

### SWEEP-F-0003 — Certification wording control exists in current AstroCrown audit convention, but operation is not yet demonstrated

- **Status:** SUPPORTING DOCUMENT — needs operational test
- **Evidence source:** `ACROWN-System/AstroCrown-Web`, `development/DEVELOPMENT-AND-AUDIT-CONVENTION.md`, main-branch blob SHA `f38d9d823c947740be1ecc8b145a132442d4dd3a`.
- **Observed result:** the document states in its context that use of standards references does not itself constitute certification/accreditation; a section lists ISO certification as a distinct item. This is a useful guard against conflating standards references with certification.
- **Interpretation:** policy/document text is design evidence only. It does not prove the public website, social communications, repositories or operational process consistently follow it.
- **Required action:** review the exact context and scope of the convention, then test a real sample of public claims and past documentation changes against the written control; record paths, examples and any false/ambiguous claims.
- **Closure evidence:** approved control plus completed usage-test records and findings/retests.

### SWEEP-F-0004 — Root-cause and evidence-preservation controls are documented, but not yet shown to operate for terminology decisions

- **Status:** SUPPORTING DOCUMENT — operational evidence required
- **Evidence source:** `ACROWN-System/NOVA`, `NOVA/ROOT-CAUSE-PREVENTION-AND-SHARED-KNOWLEDGE-GOVERNANCE.md`, main-branch blob SHA `ec8dd49ff5871d17fe1ea859a4cf015e9b58eb9e`.
- **Observed result:** the text describes root-cause records, evidence preservation, regression guards, and a distinction between verified and unverified causes.
- **Interpretation:** this could support auditability and corrective action if implemented in the terminology workflow. A written root-cause method is not proof that terminology findings have been traced, corrected and retested in practice.
- **Required action:** use the actual finding/corrective-action workflow for terminology-specific gaps; retain a real record of cause, action, and re-test without overwriting the original finding.
- **Closure evidence:** at least one complete controlled change/finding lifecycle record, plus the internal audit's assessment of whether further operational samples are required.

### SWEEP-F-0005 — AI Sanctuary domain separation is explicitly stated, but cross-domain term relations still need audit

- **Status:** OBSERVATION — follow-up required
- **Evidence source:** `ACROWN-System/AI-Sanctuary-Core`, `README.md`, main-branch blob SHA `dc77e9d36d1ddd9de926e6414f4b0562efcc3d5f`.
- **Observed result:** the README states that the repository is not part of AstroCrown tokenomics or Space Empire governance.
- **Interpretation:** retain this as a boundary control in the concept system; do not infer integration or shared authority from the organization name alone.
- **Required action:** review all cross-links, shared names and governance/economic references across AI-Sanctuary-Core and NOVA/AstroCrown; record whether each relation is explicit, non-authoritative reference, dependency or N/A.
- **Closure evidence:** reviewed cross-domain relationship map and a path-level record of conflicts or non-applicability.

## Baseline lexical-screen coverage (2026-10-17)

- Initial repository/path inventory: **318 active files** across six repositories; 843 files within immutable backup/archive directories are excluded.
- Lexical-screen records: **318/318 complete**; Git blob fetch failures: **0**.
- Substantive semantic reviews: **0/318 complete**. All tracker rows remain `NOT_REVIEWED` / `NOT_ASSESSED` until actual content review, context classification and reviewer evidence are supplied.
- Selected patterns: `HAAN` appears 88 times across 35 files; `HSIAN` 0 times on these main snapshots while PR #122/#134 remain unmerged; `ISO 704` 0 exact-pattern hits on these main snapshots; the certification stem occurs 45 times across 21 files; compliance/conformance stems occur 402 times across 27 files. These are scanner counts, not conformity decisions; exact patterns do not cover all synonyms or languages.
- Oversized active file `NOVA/README.md` has been lexically screened from its full Git blob; semantic/section-level review remains open.
- Full ISO 704 clause/topic matrix: **BLOCKED** pending lawful controlled access to the complete edition and the baseline lifecycle check.
- Internal audit, corrective-action closure, management review and readiness GO decision: **NOT COMPLETED**.
- Provider discovery/accreditation checks: **DEFERRED until the complete readiness gate passes**.

## Revision history

- **2026-10-17 / v0.1.0:** Initial selected-file lexical screen findings recorded.
- **2026-10-17 / v0.1.1:** Updated to reflect lexical-screen coverage of all 318 active baseline paths; explicitly separates that automated screen from semantic review, which remains incomplete.

## Next work queue

1. Close or formally disposition SWEEP-F-0001 after the dependent HSIAN naming changes are decided and validated.
2. Complete the semantic/section-level review of SWEEP-F-0002 across its full contents; its lexical screen is already complete.
3. Continue the tracker sequentially across the remaining active text files, then assets/configuration formats; do not mark extension-based exclusions as N/A without rationale.
4. Review all certification-claim controls in live/public and technical surfaces and record evidence.
5. Apply the [register quality review](2026-10-17-ISO-704-Register-Quality-Review.md) to the 15 starter entries; add typed relations and evidence-backed fields without guessing.
6. Verify the [certification-context review](2026-10-17-ISO-704-Certification-Context-Review.md) with a human reviewer and audit actual public surfaces.
7. Build and validate the concept-system maps and cross-repository relationship register.
8. Do not claim the lexical screen or either targeted context review is a completed or successful ISO 704 audit.



## Targeted follow-up reviews

- The [certification-context review](2026-10-17-ISO-704-Certification-Context-Review.md) examined all 21 files matching the `certif*` pattern (45 matches). The seven hits in `NOVA/README.md` are TLS certificate references; the other contexts are primarily disclaimers or generic external-assurance planning. Two areas require human verification: the `Evidence state: VERIFIED` semantics in the entity registry and broad future wording such as “ISO certification” in the feasibility registry. No ISO 704-specific certification claim was observed in those contexts, but broader public-surface review is still required.
- The [canonical register quality review](2026-10-17-ISO-704-Register-Quality-Review.md) identifies missing per-entry sources/decision records, typed relations, review dates/owners and inconsistent variant/example fields across the 15 starter concepts. It is preliminary and requires authorized human domain review.


## Additional entry and relation work

- The [candidate concept-relation map](2026-10-17-ISO-704-Concept-Relation-Map-Draft.md) records proposed types/directions for relations among the 15 starter concepts and leaves charter-dependent or architecture-dependent relations blocked. It is not approved and needs domain validation and sources.
- The [HSIAN pilot entry review](2026-10-17-ISO-704-Pilot-Entry-Review-HSIAN.md) follows one naming gap through the draft checklist. It remains blocked pending PR #122/#134 and human approval; it tests the review form but is not a complete operational workflow cycle.


## Semantic review update — Batch 001 READMEs (2026-10-17)

A preliminary AI-assisted content review has now been recorded for the six repository README files. See [Semantic Review Batch 001](2026-10-17-ISO-704-Semantic-Review-Batch-001-READMEs.md) for exact baseline blob SHAs and file-by-file evidence.

New/confirmed follow-up findings:
- **B001-F01:** NOVA README retains active HAAN naming; the HSIAN naming rollout remains pending.
- **B001-F02:** Freebies README's “free forever” and deployment “in minutes” claims need scope and substantiation.
- **B001-F03:** ACS/Monte Carlo specification README does not identify an authoritative specification/version or adequate scope.
- **B001-F04:** AI-Sanctuary-Core's explicit statement that it is outside AstroCrown audits conflicts with the proposed six-repository umbrella scope. Human scope resolution is required before AR-E01 can pass.
- **B001-F05:** Simulation Lab README contains only a title; inspect the other active files before deciding scope/applicability.
- **B001-F06:** AstroCrown-Web README makes a useful source-code licence / brand-identifier distinction, but does not establish every asset or public-content claim.

Tracker status after this batch: **LEXICAL SCREEN 318/318; PRELIMINARY SEMANTIC REVIEW 6/318; 312 NOT REVIEWED; HUMAN VALIDATION PENDING.** These are preliminary observations, not ISO 704 clause findings. No backup/archive path was changed.


## Semantic review update — Batch 002 NOVA governance/operational paths (2026-10-17)

See [Semantic Review Batch 002 — NOVA Core](2026-10-17-ISO-704-Semantic-Review-Batch-002-NOVA-Core.md) for the five exact baseline blob SHAs, observations, and dispositions.

- **B002-F01:** “system intelligence (SI)” in the root-cause architecture may collide with “Super Intelligence” terminology; establish an unambiguous acronym policy.
- **B002-F02:** the foundational mission document still uses HAAN/Imperial HAAN pending HSIAN rename integration.
- **B002-F03:** `nova@haan.system` remains in active operational-state author metadata; record whether it is intentionally retained or should be changed by a reviewed change.
- **B002-F04:** a test fixture's `GROQ_API_KEY_02` value is synthetic, not a statement of required production secrets; do not confuse test fixtures with actual configuration.
- **B002-F05:** heartbeat workflow labels were reviewed for terminology context only; runtime/security/functionality were not audited and no term defect was identified in this file.

Tracker status after Batch 002: **LEXICAL SCREEN 318/318; PRELIMINARY SEMANTIC REVIEW 11/318; 307 NOT REVIEWED; HUMAN VALIDATION PENDING.** No ISO 704 clause result is inferred.


## Semantic review update — Batch 003 large NOVA state ledger

See [Semantic Review Batch 003 — Large NOVA README](2026-10-17-ISO-704-Semantic-Review-Batch-003-Large-NOVA-README.md).

- **B003-F01:** `NOVA/README.md` is a 28,490-line operational/state-report ledger with a mix of templates, placeholder text and definitive-sounding status claims. The file is not itself a canonical terminology register, and this screen does not verify the underlying metrics or legal/compliance claims.
- **B003-F02:** the file's certification-pattern hits are TLS/security certificate references under the existing certification-context review; generic compliance labels are not ISO 704 certification evidence.
- **B003-F03:** the file's exact terminology-audit applicability and any separate public-claim validation requirement need an explicit scope decision; the file row remains PARTIAL rather than fully reviewed.

Tracker state after Batch 003: **318/318 lexical scans; 11 preliminary file reviews; 1 partial targeted screen; 306 not reviewed; human validation pending.**


## Semantic review update — Batch 004 Freebies licence and token example

See [Semantic Review Batch 004 — Freebies](2026-10-17-ISO-704-Semantic-Review-Batch-004-Freebies.md) for the two exact baseline blob SHAs and dispositions.

- **B004-F01:** the MIT licence file is present and conventional, but does not prove all repository resources, third-party assets or future offerings are covered; public “open-source/free forever” wording remains open.
- **B004-F02:** the `SimpleToken.sol` example uses “Minimal ERC-20 Token (BSC ready)”; standard/chain compatibility, deployment and security remain unverified in this terminology review. Keep it labelled as an example until separate engineering evidence supports stronger claims.

Tracker status after Batch 004: **318/318 lexical scans; 13 preliminary content reviews; 1 partial targeted screen; 304 not reviewed; human validation pending.**


## Semantic review update — Batch 005 ACS / Monte Carlo specification

See [Semantic Review Batch 005 — ACS/Monte Carlo Spec](2026-10-17-ISO-704-Semantic-Review-Batch-005-ACS-MC-Spec.md).

- **B005-F01 — blocking source-integrity issue:** `AstroCrown_ACS_MC_Spec_v1.1.2.md` states that sections A–P and an auditor prompt are included, but the exact baseline blob has only sections A–H and ends inside a fee formula. Its stated “sole source of truth” authority must not be used to infer missing rules. Restoration/clarification needs a reviewed, versioned change and exact post-change ref.
- **Domain terminology note:** the spec contains a useful ACS-specific glossary (ACS, FPRF/V, C, I, F, R, G, Paymaster, T0, LCR, P_ACS/P_EXT and related symbols). The shared terminology register should link to this domain authority for detailed ACS meanings rather than silently duplicate economic rules.
- The same repository's README and licence were also reviewed in B001/B005; all three current active paths have a preliminary review, but repository scope and human approval remain pending.

Tracker status after Batch 005: **318/318 lexical scans; 15 preliminary content reviews; 1 partial targeted screen; 302 not reviewed; human validation pending.**


## Semantic review update — Batch 006 Simulation Lab and Batch 007 AI Sanctuary (2026-10-17)

See [Batch 006 — Simulation Lab](2026-10-17-ISO-704-Semantic-Review-Batch-006-Simulation-Lab.md) and [Batch 007 — AI Sanctuary](2026-10-17-ISO-704-Semantic-Review-Batch-007-AI-Sanctuary.md).

- **B006-F01:** six Simulation Lab subdirectory README files consist of a single newline. Folder names do not establish that a corresponding model, governance procedure, Monte Carlo simulation, Paymaster model, result set or scenario definition actually exists. The ordinary root README is only a title. Combined with B001 review, all eight inventoried paths have preliminary review records.
- **B007-F01:** AI-Sanctuary-Core says it is outside AstroCrown audits, conflicting with the proposed umbrella inclusion. Scope decision requires the human maintainer; do not override the repo's boundary based on org membership alone.
- **B007-F02:** symbolic protocol files use numerous undefined/project-defined governance and security concepts; strings such as “cryptographic signature”, “least privilege”, “AI-only” or “hidden encoding” are not evidence that a control is implemented.
- **B007-F03:** the axioms file contains only a newline; no axioms are evidenced in that file.
- **B007-F04:** “jailbreaker seed” terminology is ambiguous; do not infer capability or security behavior from the name.

Tracker after Batch 007: **318/318 lexical scans; 29 preliminary file reviews; one partial targeted screen; 289 not reviewed; human validation pending.** The six-repository scope and English-only/localization boundary remain unapproved. No backup/archive path was changed.


## Semantic review update — Batch 008 resource/capacity vocabulary

See [Semantic Review Batch 008 — Resource Readiness](2026-10-17-ISO-704-Semantic-Review-Batch-008-Resource-Readiness.md).

- **B008-F01:** `PROVIDER-ACQUISITION-READINESS.md` classifies Hugging Face Inference Providers as conflicted / do not count as free capacity pending current evidence, while `DEVELOPMENT-RESOURCE-READINESS.md` still records $0.10/month as the free-account allowance. Retain the conservative blocked/not-counted state until a dated official/account record resolves the contradiction.
- **B008-F02:** dynamic quotas need row-level source date, scope, verification status and recheck/expiry metadata, not only a general warning elsewhere in the document.
- **B008-F04:** the role label `REQUIRED` in a resource matrix is not a resource-state result such as `VERIFIED_AVAILABLE`; keep role and availability in separate fields.
- **Positive practice:** GPU capacity vocabulary explicitly separates advertised, recurring, one-time, reserved, idle, useful and unknown usage, and labels 86,400 GPU-minutes/month as provisional/unvalidated.

Tracker counts were reconciled from row status after finding a one-row aggregate arithmetic mismatch. Prevention: after every batch, derive totals from row states and verify `full reviews + partial reviews + NOT_REVIEWED = total active rows`. Current count: 32 + 1 + 285 = 318.


## Semantic review update — Batch 009 image qualification and RSI doctrine

See [Semantic Review Batch 009 — Image and RSI Doctrine](2026-10-17-ISO-704-Semantic-Review-Batch-009-Image-and-RSI-Doctrine.md).

- **B009-F01:** the image qualification record's initial status/objective still says “establish the first live image test”, even though later sections record three successful request/artifact deliveries, visual acceptance failure, and unresolved account cost/quota, alpha and commercial rights. Reconcile the current header without deleting dated history.
- **B009-F02:** preserve the useful evidence boundaries between request success, visual quality, JPEG/alpha, cost/quota and commercial rights.
- **B009-F03:** the cooperative RSI principle is properly labelled proposed/documentation-only and not an operational capability proof.
- **B009-F04:** the active HAAN mission reference still depends on the pending HSIAN rename integration.
- **B009-F05:** the cross-cutting principle locally defines legitimacy resilience, protective intelligence, emergent coordination and shared human–AI sovereignty; decide which concepts need canonical IDs versus domain-local definitions.

Tracker after Batch 009: **318 lexical scans; 34 preliminary full-file reviews; one partial targeted screen; 283 not reviewed; human validation pending.** Row-count integrity control checked: 34 + 1 + 283 = 318.


## Semantic review update — Batch 010 provider incidents and credential state

See [Semantic Review Batch 010 — Credential State](2026-10-17-ISO-704-Semantic-Review-Batch-010-Credential-State.md).

- **B010-F01:** the 2026-10-09 Provider Error Evidence report's top-level status still says PR #57 OPEN and live outcomes pending; later records document Mistral's 2026-10-10 deferral and subsequent diagnostic/follow-up state. Add a dated status note after confirming PR dispositions from repository metadata; preserve the original incident evidence and uncertainty.
- **B010-F02:** provider lifecycle distinctions are strong: configured key, auth, API health, response contract, quality, quota scope, and provider activation are separate states.
- **B010-F03:** Cloudflare image-generation evidence cannot be reused as proof of Cloudflare LLM/chat qualification, and vice versa. Each adapter/model/endpoint needs its own contract and result.
- **B010-F04:** dynamic quota/candidate tables need current source/date/account scope before their values are reused operationally.

Tracker after Batch 010: **318 lexical scans; 37 preliminary full-file reviews; one partial targeted screen; 280 not reviewed; human validation pending.** Row-count invariant: 37 + 1 + 280 = 318.


## Semantic review update — Batch 011 GPU heartbeat and Weak RSI workflows

See [Semantic Review Batch 011 — GPU and Weak RSI](2026-10-17-ISO-704-Semantic-Review-Batch-011-GPU-and-Weak-RSI.md).

- **B011-F01:** the Weak RSI workflow's PASS_AFTER_REVIEW input is an operator attestation that current terms were reviewed, not independent evidence that a use is permitted. Retain reviewer/source/date/scope evidence alongside the decision.
- **Positive control:** GPU credential state separates missing/configured/authenticated token from candidate activation and unverified capacity; preserve this model.
- **B011-F03:** mocked unit tests and static YAML assertions are offline implementation evidence, not proof of a live provider, current account terms, or actual workflow dispatch result.

Tracker after Batch 011: **318 lexical scans; 41 preliminary full-file reviews; one partial targeted screen; 276 not reviewed; human validation pending.** Row-count invariant: 41 + 1 + 276 = 318.


## Semantic review update — Batch 012 provider qualification state

See [Semantic Review Batch 012 — Provider Qualification](2026-10-17-ISO-704-Semantic-Review-Batch-012-Provider-Qualification.md).

- **B012-F01:** the implementation marks the exact Cloudflare LLM JSON-contract capability `SKIPPED_ALREADY_QUALIFIED` and `ACTIVE` based on a linked prior run, while `KEY-READINESS.md` still says Cloudflare inference remains `BLOCKED_CONTRACT_UNVERIFIED`. Resolve this in a reviewed source change by naming the exact model/endpoint, qualifying evidence scope/date, expiry and current decision. A historical response-contract test is not current provider health, account entitlement, quota, cost or production readiness.
- **Positive control:** diagnostic status words distinguish HTTP class, valid shape, probe marker, rate-limit headers, lifecycle and resource eligibility; mocks protect secrets and response text. Preserve these distinctions.

Tracker after Batch 012: **318 lexical scans; 44 preliminary full-file reviews; one partial targeted screen; 273 not reviewed; human validation pending.** Row-count invariant: 44 + 1 + 273 = 318.


## Semantic review update — Batch 013 rosters, health policy and GPU capacity evidence

See [Semantic Review Batch 013 — Rosters and Capacity](2026-10-17-ISO-704-Semantic-Review-Batch-013-Rosters-and-Capacity.md).

- **B013-F01:** current roster comment still says “HAAN Council”; update only through reviewed HSIAN naming integration after verifying the authoritative governance decision.
- **B013-F02:** the candidates_not_in_roster list mixes direct providers, gateways and specialized/community routes as free-form strings with inconsistent evidence fields and source dates. Maintain these as explicit candidates, not active providers; normalize provenance/status before counting them or comparing independent capacity.
- **B013-F03:** GPU capacity evidence marks Lightning's free_without_payment_method as VERIFIED while actual GPU credit balance/no-card GPU entitlement remains unresolved. Split account creation, free CPU workspace access, GPU credits, actual GPU allocation and no-paid-overage into separate evidence fields.
- **Positive control:** rosters and capacity evidence correctly distinguish active vs candidate/deferred, documented theoretical vs verified recurring and one-time capacity, and unknown/unmetered usage. The health policy explicitly states that stale observation is not proof of false state.

Tracker after Batch 013: **318 lexical scans; 48 preliminary full-file reviews; one partial targeted screen; 269 not reviewed; human validation pending.** Row-count invariant: 48 + 1 + 269 = 318.


## Semantic review update — Batch 014 provider history and Sanctuary roadmap

See [Semantic Review Batch 014 — Provider Records and Sanctuary](2026-10-17-ISO-704-Semantic-Review-Batch-014-Provider-Records-and-Sanctuary.md).

- **B014-F01:** `NOVA/sanctuary/IMPLEMENTATION-ROADMAP.md` references `NOVA/NOVA/sanctuary/`, which appears to be an incorrect nested path. Verify the active tree and update by a reviewed source change; do not create a duplicate canonical directory.
- **B014-F02:** the roadmap's cross-repository responsibility wording needs resolution against AI-Sanctuary-Core's statement that it is outside AstroCrown audits. Repository inclusion in a terminology sweep must not imply shared governance/financial scope. Human scope decision required.
- **Positive control:** the Mistral deferral and provider-diagnostics plans preserve historical uncertainty and explicitly distinguish offline CI from live qualification; the rolling scheduler doc does not equate quota expiry with money or synthetic work.

Tracker after Batch 014: **318 lexical scans; 52 preliminary full-file reviews; one partial targeted screen; 265 not reviewed; human validation pending.** Row-count invariant: 52 + 1 + 265 = 318.


## Semantic review update — Batch 015 probe, validation and image-qualification workflows

See [Semantic Review Batch 015 — Workflows](2026-10-17-ISO-704-Semantic-Review-Batch-015-Workflows.md).

- **Positive control:** the opportunistic probe scheduler separates a read-only decision job from the provider probe/persistence job. The file's claims about rolling cadence and concurrency still need code/test/runtime evidence.
- **Positive control:** the NOVA validation workflow calls `credential_readiness` for slot presence only; do not conflate it with provider authentication or qualification.
- **B015-F03:** the Cloudflare image workflow's `no_payment_confirmed=yes` is an operator declaration, not account billing telemetry or proof of zero future charges. Keep provider usage/terms evidence separate.
- **B015-F04:** candidate artifact paths for PNG/JPEG are not proof the adapter produces a truthful file+sidecar pair on any given run. Verify adapter tests and run-specific artifacts separately.

Tracker after Batch 015: **318 lexical scans; 55 preliminary full-file reviews; one partial targeted screen; 262 not reviewed; human validation pending.** Invariant: 55 + 1 + 262 = 318.


## Semantic review update — Batch 016 router, health and capacity state models

See [Semantic Review Batch 016 — Router, Health and Capacity](2026-10-17-ISO-704-Semantic-Review-Batch-016-Router-Health-Capacity.md).

- **B016-F01:** the router classifies any HTTP 404, and text markers including `model_not_found`, as `permanent`; if any probed model has that class, the outer router can mark the provider itself DOWN. Review whether model-/endpoint-specific failures should remain model-scoped unless provider-wide failure is independently evidenced. No code changed in this review.
- **B016-F02:** provider HTTP error bodies are truncated to 400 characters, but the body snippet is persisted as `error_detail` in health history. Truncation alone is not sanitization. Review/redact before durable persistence and add negative tests for secret/PII markers; don't claim an actual leak without evidence.
- **Positive controls:** health freshness terms distinguish UNKNOWN/stale/future/invalid timestamps; structured response markers distinguish HTTP success from NOVA contract success; total resource observations remain separate from call allowances, with unknown economics not treated as zero-cost and expiry not creating synthetic work.

Tracker after Batch 016: **318 lexical scans; 59 preliminary full-file reviews; one partial targeted screen; 258 not reviewed; human validation pending.** Row-count invariant: 59 + 1 + 258 = 318.


## Semantic review update — Batch 017 GPU capacity qualification and expiry scheduler

See [Semantic Review Batch 017 — GPU Capacity and Scheduler](2026-10-17-ISO-704-Semantic-Review-Batch-017-GPU-Capacity-Scheduler.md).

- **Positive control:** GPU capacity qualifies only with fresh source-backed account/terms/data-handling/allocation evidence and an active roster entry; advertised quotas do not count; recurring and one-time capacity remain distinct; unknown usage remains unknown.
- **B013-F03 remains open:** the upstream Lightning `free_without_payment_method` status needs a precise scope split; an exact `VERIFIED` enum cannot compensate for an ambiguously defined proposition.
- **Scheduler control:** expiry preemption needs an observed expiry opportunity, may only run already-required health work, skips unacceptable providers, and moves checked providers to the end of the rolling queue. Expiry pressure alone cannot create work.
- **Usage limitation:** manual `gpu_capacity.py` reporting with the default empty active-provider list is a candidate snapshot rather than proof of operationally active capacity unless the active roster is explicitly provided.

Tracker after Batch 017: **318 lexical scans; 63 preliminary full-file reviews; one partial targeted screen; 254 not reviewed; human validation pending.** Invariant: 63 + 1 + 254 = 318.


## Semantic review update — Batch 018 credential readiness and GPU health

See [Semantic Review Batch 018 — Credential and Health](2026-10-17-ISO-704-Semantic-Review-Batch-018-Credential-and-Health.md).

- **Positive control:** credential readiness is presence-only; credentials and candidate lifecycle stay separate; candidate GPU auth uses a documented read-only endpoint/host allowlist and does not infer quota from undocumented response fields.
- **Scope rule:** GPU heartbeat `HEALTHY` describes its configured HTTP health endpoint probe, not a successful GPU workload, LLM structured-response contract, remaining GPU quota, zero-cost entitlement, or commercial rights.
- The scheduler/health test values are synthetic; no live timing or health behavior was validated in this review.

Tracker after Batch 018: **318 lexical scans; 67 preliminary full-file reviews; one partial targeted screen; 250 not reviewed; human validation pending.** Invariant: 67 + 1 + 250 = 318.


## Semantic/data-state review update — Batch 019 persisted health-state snapshot

See [Semantic Review Batch 019 — Health-State Snapshot](2026-10-17-ISO-704-Semantic-Review-Batch-019-Health-State-Snapshot.md).

- **B019-F01:** `NOVA/health_state.json` top-level update and latest record are dated 2026-10-11, while policy freshness is six hours. At the 2026-10-17 review time, zero of 116 historical rows were within the freshness window. Preserve as dated historical evidence; do not use its labels as current provider health.
- **B019-F02:** 94 history rows contain non-empty `error_detail`. A bounded pattern scan did not find common bearer/API-key/email patterns, but this cannot prove full sanitization. Track redaction-before-persistence and negative-test coverage with B016-F02; do not assert a confirmed leak.
- **B019-F03:** historical model target identities may outlive current configuration; current reporting should join them to the current roster/lifecycle and keep orphaned/deprecated identities as history rather than active configuration.

Tracker after Batch 019: **318 lexical scans; 68 preliminary full-file reviews; one partial targeted screen; 249 not reviewed; human validation pending.** Invariant: 68 + 1 + 249 = 318.


## Semantic review update — Batch 020 quality gates, reasoning payload and economics

See [Semantic Review Batch 020 — Quality, Reasoning and Economics](2026-10-17-ISO-704-Semantic-Review-Batch-020-Quality-Reasoning-Economics.md).

- **B020-F01:** `validate_reasoning_payload` should first require an object/dict, strictly check each field's type before enum membership, reject boolean confidence values, and return controlled invalid-payload states for scalar/unhashable JSON instead of exceptions. Human-gate requirements should be derived/constrained by trusted policy rather than merely model-authored. No runtime code change made by this review.
- **B020-F02:** `money()` maps invalid values to zero and `provider_cost()` defaults missing tariff fields to zero. Missing/invalid price evidence must not masquerade as verified free service. Require explicit free status or complete source-backed pricing, preserve UNKNOWN/BLOCKED for missing fields, and test negative rates/inputs through a reviewed implementation change.
- **Positive controls:** quality-case closure requires exact candidate-commit verification, passing regression evidence, and timezone-aware timestamp; recurrence reopens closure. Model capability gating blocks undeclared models where the provider has adopted a contract registry, while LEGACY_UNDECLARED remains an explicit compatibility exception.

Tracker after Batch 020: **318 lexical scans; 72 preliminary full-file reviews; one partial targeted screen; 245 not reviewed; human validation pending.** Invariant: 72 + 1 + 245 = 318.


## Semantic review update — Batch 021 policy, alerts and regression tests

See [Semantic Review Batch 021 — Policy, Alerts and Tests](2026-10-17-ISO-704-Semantic-Review-Batch-021-Policy-Alerts-Tests.md).

- **B021-F01:** alert generation maps `active` to `live` and all other statuses to `DOWN`. Constrain allowed roster states and report down/deferred/candidate/blocked/unconfigured/unknown distinctly.
- **B021-F02:** action policy labels `create_payment_intent` autonomous, but this file does not define whether it is only a local non-binding draft or can reserve/charge funds/incur fees. Define the operation's side effects before treating the label as safe.
- **B021-F03:** existing economics tests do not cover unknown/malformed tariffs or negative monetary inputs; reasoning tests do not cover adversarial JSON types or model-authored critical human-gate contradictions. These cases need separate reviewed code/test changes.
- **B021-F04:** `watchlist.json` has an empty source list; do not claim current external-feed observation on the basis of the reasoning module alone.
- **B021-F05:** GitHub issue creation does not itself prove recipient email delivery; the voice-alert output interpolates text into TwiML without visible escaping and should receive a separate security review. No alert was sent and no exploit was tested.

Tracker after Batch 021: **318 lexical scans; 77 preliminary full-file reviews; one partial targeted screen; 240 not reviewed; human validation pending.** Invariant: 77 + 1 + 240 = 318.


## Semantic review update — Batch 022 payment and pricing controls

See [Semantic Review Batch 022 — Payments and Pricing](2026-10-17-ISO-704-Semantic-Review-Batch-022-Payments-and-Pricing.md).

- **B022-F01:** policy allows payment-intent creation autonomously, while implementation locally appends a record in `HUMAN_GATE_REQUIRED` state and labels it `irreversible: true`. Clarify whether this flag refers to the future contemplated transfer or the local draft operation. Keep settlement blocked without an approved, verified adapter.
- **B022-F02:** pricing conversion accepts a bare exchange-rate number while the docstring calls it verified; quote output records created/expires times but no rate source/observation/expiry or evidence ID. Add source-backed rate evidence and freshness validation in a separate reviewed implementation.
- **B022-F03:** current payment/quote tests use positive values only. Amounts should be finite/positive and valid for asset precision; rates/prices should reject invalid or stale inputs; “PASS” must describe only the actual local checks, not recipient verification or payment approval.
- **B022-F04:** empty pricing service map and zero/null economic state are valid initial scaffolding, not proof of approved live service tariffs, real-world zero balances or absence of external transactions. Represent uninitialized/unknown distinctly from verified zero.

Tracker after Batch 022: **318 lexical scans; 84 preliminary full-file reviews; one partial targeted screen; 233 not reviewed; human validation pending.** Invariant: 84 + 1 + 233 = 318.


## Semantic review update — Batch 023 allocation policy and test-budget evidence

See [Semantic Review Batch 023 — Allocation and Budgets](2026-10-17-ISO-704-Semantic-Review-Batch-023-Allocation-and-Budgets.md).

- **B023-F01 — code/policy consistency risk:** `capacity_policy.json` declares resource and call-allowance fit as hard dimensions, but `allocation.py` may keep a candidate eligible when a positive required remaining request/token/resource measure is unknown. It also normalizes some malformed/negative requirement fields to zero. This should be corrected in a separate reviewed code change and guarded with negative tests; no allocator execution or change occurred in this batch.
- **B023-F02:** development test-budget caps are partly policy values and partly derived from dated quota observations. Treat caps as operator-imposed limits, not provider entitlements, and keep row-level source/scope/date/recheck rules.
- **B023-F03:** dated Gemini project limits and Mistral workspace UI status are historical observations; do not turn peak usage into remaining quota or generalize a workspace-specific access screen to every provider plan. Later Mistral project deferral remains a separate decision.
- **Positive control:** credential readiness tests distinguish slot presence from verification and assert that secret values do not appear in the report; tests were not executed in this review.

Tracker after Batch 023: **318 lexical scans; 91 preliminary full-file reviews; one partial targeted screen; 226 not reviewed; human validation pending.** Invariant: 91 + 1 + 226 = 318.
