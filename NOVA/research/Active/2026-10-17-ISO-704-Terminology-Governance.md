# Active Research Plan — ISO 704:2022 Terminology Governance

**Date:** 2026-10-17  
**Status:** ACTIVE — documentation proposal in a review branch  
**Repository:** ACROWN-System/NOVA  
**Branch:** docs/terminology-governance-iso704-2026-10-17  
**Objective:** Establish an auditable cross-ecosystem terminology governance standard and initial canonical terminology register, designed around the public scope of ISO 704:2022 and using ISO 1087:2019 as its terminology-work vocabulary reference.

## Navigation and source-of-truth note

The standalone NAVIGATION-PROTOCOL.md and NAVIGATION-PLAN-TEMPLATE.md were not located in the inspected active paths of either public repository. This plan therefore uses the available repository structures and an explicit scope/evidence/impact/verification record. Initial repository reconnaissance and creation of the working branch preceded this plan; this sequencing deviation is recorded rather than described as strict compliance with an unavailable protocol.

Authoritative public standard metadata:
- ISO 704:2022, Terminology work — Principles and methods: https://www.iso.org/standard/79077.html
- ISO 1087:2019, Terminology work and terminology science — Vocabulary: https://www.iso.org/standard/62330.html
- ISO information on certification: https://www.iso.org/certification.html

## Findings and constraints

- A brand book alone is insufficient; the project needs concept-level records distinguishing referents, concepts, definitions, designations, domains and typed relationships.
- The canonical standard and register belong in NOVA to reduce competing definitions across projects; AstroCrown-Web provides public-facing application guidance and links to the canonical record.
- ISO 704:2022's public description supports terminology work, concept relations, term/proper-name formation and definitions. The full licensed standard has not been made available as a controlled audit baseline.
- Provider discovery and accreditation checks are deliberately deferred until a complete internal audit-readiness package passes its documented gate. The priority is scope, controlled access to the full edition, a clause/topic-to-evidence matrix, objective evidence of actual operation, internal audit, corrective-action retesting and a human readiness decision. No conclusion is made about certificate availability; do not search for or contact providers before the readiness gate passes.
- Initial canonical entries include NOVA, HSIAN, Super Intelligence, AstroCrown, ACROWN token, Space Empire, RSI, Strong RSI, Imperial HSIAN, Imperial Council, cognitive extension/enhancement/prosthesis analogy, canonical terminology register and terminology governance standard. These are a starting set, not an exhaustive inventory.

## Scope

1. Add NOVA/TERMINOLOGY-GOVERNANCE-STANDARD.md with definitions discipline, concept-system relationships, status lifecycle, multilingual controls, governance, audit controls and a preliminary ISO thematic evidence map.
2. Add NOVA/CANONICAL-TERMINOLOGY-REGISTER.md with stable concept identifiers, definitions, relations, approved/candidate/deprecated status and open issues.
3. Add AstroCrown-Web public-facing terminology/brand language application guidance linked to the canonical NOVA source.
4. Maintain reviewable branch/PR workflow and explicit cross-repository merge order.
5. Preserve a strict immutable backup boundary: do not add, update, rename, move or delete any path beneath backup/, Backup/ or any case variant.
6. Mark full clause-level ISO 704 conformity BLOCKED until lawful access to the exact full edition, a controlled clause/topic-to-evidence matrix and objective evidence audit. Complete the package defined in [the Audit-Readiness Dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md) before beginning any provider discovery, enquiry or accreditation check.
7. Do not change runtime code, provider operation, access controls, payment, deployment or RSI readiness.

## Impact Analysis

**IF modified:** project terminology can be governed and audited consistently across technical work, public communication and future localizations. A reusable terminology register can identify conflicting meanings, prevent accidental legal/scientific overclaims and keep term history traceable.

**IF not modified:** inconsistent names, duplicate or overlapping definitions and contradictory claims can reappear across repositories and user-facing content, making governance and auditing harder.

## Required verification

- Confirm both canonical files exist on this branch and their links resolve within the branch.
- Inspect every changed path and prove that no backup/archive path is included.
- Review every initial entry for concept/term/definition distinction, status, scope note and unsupported claims.
- Check for the former HSIAN/HAAN naming references in the active source-of-truth scope; preserve immutable history and do not mass-rewrite old backups.
- Verify any linked claims against official source pages and label unverified details BLOCKED/CANDIDATE.
- Re-check all final file paths and the complete PR diff after changes.

## Current execution status

- Canonical governance standard and initial register drafted on this branch.
- AstroCrown-Web application guide and audit record are in progress on the corresponding branch.
- No PR is merged or deployed; no external certification is claimed; provider discovery and accreditation checks are deferred until the complete evidence package passes the readiness gate; no paid standards/software purchase is authorized; and no backup folder is modified.


## Execution update — 2026-10-17

- Draft canonical standard and initial register are committed on this branch.
- Opened [NOVA draft PR #124](https://github.com/ACROWN-System/NOVA/pull/124); it contains the standard, register and this plan (3 added paths).
- Cross-repository application guide is in [AstroCrown-Web draft PR #135](https://github.com/ACROWN-System/AstroCrown-Web/pull/135).
- Repository comparisons show no changed paths under backup/, Backup/ or any case variant.
- The full ISO 704:2022 clause-level review remains BLOCKED; the HSIAN active-name rollout and full-repository terminology sweep remain incomplete.
- The PRs are draft and unmerged. Review the HSIAN canonical mission PR #122 and then NOVA terminology PR #124 before merging dependent AstroCrown-Web PR #135.


## Execution update — 2026-10-17 — readiness-first sequencing

- Added [the ISO 704:2022 Audit-Readiness Dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md), which defines 20 evidence components, scope and evidence-handling rules, operational proof, internal audit, corrective-action retesting, management review, a final manifest and a mandatory GO/NO-GO gate.
- Added [the controlled clause/topic-to-evidence matrix template](2026-10-17-ISO-704-Clause-Evidence-Matrix.md). It is deliberately empty at clause level; populating it is BLOCKED until lawful controlled access to the complete ISO 704:2022 edition is established.
- Provider discovery, accreditation checks, enquiries and applications are DEFERRED until all readiness gates pass. This sequencing does not conclude whether a suitable scheme exists.
- Updated [NOVA draft PR #124](https://github.com/ACROWN-System/NOVA/pull/124) to disclose the current sequence and limitations. It now contains five active paths, all under `NOVA/`; the branch comparison has no changed paths under `backup/`, `Backup/` or any case variant.
- Current status: **NOT READY FOR AN ISO 704 AUDIT**. The dossier is a work plan/evidence register, not proof that the evidence has all been produced. No paid access, application or other financial commitment is authorized.


## Execution update — 2026-10-17 — scope baseline

- Created [the proposed scope and repository inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md) plus [the machine-readable active-path inventory](2026-10-17-ISO-704-Active-Path-Inventory.json).
- Git tree metadata snapshots were retrieved for the six currently accessible active repositories: NOVA, Freebies-, AstroCrown_ACS_MC_Spec, AI-Sanctuary-Core, ACROWN-SIMULATION-LAB and AstroCrown-Web.
- The baseline enumerates 318 active files and excludes 843 files under immutable backup/archive paths from the active path list. This is only a path inventory; every included file remains NOT_CONTENT_REVIEWED.
- The six-repository scope is proposed, not human-approved. AI-Sanctuary-Core remains a separately scoped domain, preserving its stated separation from AstroCrown tokenomics and Space Empire governance.
- Provider/scheme discovery remains deferred until the complete evidence package passes the readiness gate. No standards purchase or paid activity is authorized.


## Execution update — 2026-10-17 — file-level review control

- Added [the 318-record file-by-file content sweep tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json), carrying repository, path, blob SHA, provisional review queue, evidence IDs, findings and reviewer/result fields.
- Every item is explicitly marked NOT_REVIEWED / NOT_ASSESSED. Queue categories use extension and path hints only; they do not establish applicability, content review or conformance.
- The next work is a human-/tool-supported review of actual file content, with exact baseline refs and findings. Backup/archive contents remain excluded from the active review and immutable.


## Execution update — 2026-10-17 — initial content screen

- Lexically screened 15 active files across the six-repository main-branch baseline and recorded term counts/selected excerpts in the [content sweep tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json).
- Created [the initial findings log](2026-10-17-ISO-704-Initial-Sweep-Findings.md). A known active HAAN naming transition remains pending dependent PR #122 and PR #134; an oversized active NOVA README still requires segmented review; policy text supporting claim/evidence controls needs operational testing.
- The 15-file lexical scan is not semantic content review, and all 318 file records still require substantive review/classification. Overall readiness remains **NOT READY FOR AN ISO 704 AUDIT**.


## Execution update — 2026-10-17 — complete lexical screen baseline

- Completed the selected-token lexical scan for **318/318 active file paths** across six repository main-branch snapshots. All paths have a Git blob fetch record; no fetch failures remain.
- The scan stored counts/excerpts for selected patterns in the [content sweep tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json). High-level counts are summarized in the [readiness dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md).
- **This is not a completed semantic review:** all 318 tracker rows remain `NOT_REVIEWED` / `NOT_ASSESSED`. The large `NOVA/README.md` also needs section-level interpretation despite its successful lexical scan.
- Known active HAAN/HSIAN transition still awaits dependent PR #122 and #134; no mass-edit was made. All 843 backup/archive paths/files counted in the AstroCrown-Web baseline remain excluded from the active inventory and immutable.
- Current overall disposition remains **NOT READY FOR AN ISO 704 AUDIT**. The complete standard baseline, scope approval, full clause/topic evidence matrix, semantic review, operational pilot evidence, internal audit, corrective actions, management GO decision remain unfinished. Provider search/contact stays deferred.


## Execution update — 2026-10-17 — targeted semantic-context reviews

- Added [a preliminary certification-context review](2026-10-17-ISO-704-Certification-Context-Review.md) covering 21 files and 45 `certif*` lexical matches. The seven matches in the very large NOVA README are TLS-certificate operational references, not standards certification. Most other contexts are disclaimers; generic future “ISO certification” language and the entity-registry evidence-state column require human verification. This review found no ISO 704-specific certificate claim in those 21 contexts, which does not close the broader public-claims audit.
- Added [a 15-entry canonical-register quality review](2026-10-17-ISO-704-Register-Quality-Review.md). It records missing per-entry provenance/approval data, untyped relations, and other fields requiring evidence-backed completion and human review.
- These are preliminary targeted reviews. All 318 active path tracker rows remain semantically `NOT_REVIEWED` / `NOT_ASSESSED` at whole-file level; the overall package is **NOT READY FOR AN ISO 704 AUDIT**.


## Execution update — 2026-10-17 — relation and entry pilot artefacts

- Added [a candidate typed concept-relation map](2026-10-17-ISO-704-Concept-Relation-Map-Draft.md) for the 15 starter concepts. It distinguishes hierarchy/association from governance relations and leaves uncertain links blocked; no map relation is approved by this draft.
- Added [a one-entry HSIAN review pilot](2026-10-17-ISO-704-Pilot-Entry-Review-HSIAN.md) anchored to the current-main discrepancy and dependent PRs #122/#134. It is blocked pending rollout and human approval and does not count as operational-use evidence.
- These artefacts improve traceability, but AR-E05/AR-E06 remain open pending domain review and evidence; AR-E15 remains open until an authorized actual workflow cycle is recorded.


## Execution update — 2026-10-17 — branch-integrity incident and recovery

- Recorded [the branch-integrity incident](2026-10-17-ISO-704-Branch-Integrity-Incident.md): a generic file-creation action placed four supplementary review documents on `main` rather than the intended branch, despite a requested branch target.
- Recovery copied those four documents into PR #124 using an explicit tree/commit/ref update parented to the then-current PR head, then removed only those four paths from `main`. Current tree verification confirms they are present on the draft branch and absent on current `main`.
- The accidental add/remove commits remain in shared `main` history; no force-push/history rewrite was performed. All immutable backup/archive paths remain untouched.
- Prevention rule: for new files on non-default branches, use the explicit tree → commit → ref-update path and then verify the exact target ref, blob content, PR changed-file list and immutable-path boundary. A successful action response alone is insufficient.


## Execution update — 2026-10-17 — semantic review Batch 046

- Reviewed five previously unreviewed active NOVA paths against their recorded blob SHAs at baseline `2a1f5c496474aa099703432e99b3d3dfddfd3fd7`: `_headers`, `.github/pull_request_template.md`, `.github/workflows/nova_cloudflare_smoke_test.yml`, `.github/workflows/nova_health_tests.yml`, and `.gitignore`.
- Added [Semantic Review Batch 046](2026-10-17-ISO-704-Semantic-Review-Batch-046-NOVA-Controls-and-Security-Language.md); reconciled [the sweep tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json), [initial findings](2026-10-17-ISO-704-Initial-Sweep-Findings.md), and [scope inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md).
- New preliminary findings: SWEEP-F-0017 (overbroad security-header comments), F-0018 (Cloudflare request/response-contract traceability), F-0019 (PR workflow trigger versus verified required check), and F-0020 (.gitignore labels versus actual protection).
- **Coverage now:** 146 preliminary full-file reviews + 5 partial targeted screens + 167 not reviewed = 318 active paths. Human validation pending; formal ISO 704 clause-level assessments remain zero.
- No source/runtime file, workflow, secret, repository setting or backup/archive path was changed. Current PR remains a draft; there is no readiness or certification claim.


## Execution update — 2026-10-18 — semantic review Batches 074–075

- Reviewed 10 previously unreviewed AstroCrown-Web active paths at exact blob SHAs from baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`: five paths in Batch 074 and five in Batch 075. Source manifests and dispositions are recorded in the two linked batch reports.
- Reconciled the row-level sweep tracker to record source commit and blob SHA, review status, evidence ID, findings, reviewer/date and disposition for all ten files. Corrected the tracker’s stale top-level status text to match row-derived totals.
- Opened preliminary SWEEP-F-0053 for the Public Relations target-state list mixing verification, temporal/lineage and account/organization lifecycle status dimensions; SWEEP-F-0054 for the undefined relation between UNVERIFIED evidence state and BLOCKED decision status; and SWEEP-F-0055 for the NOVA replication-state field mixing replication extent, feasibility, workflow maturity and trust/independence dimensions.
- Recorded positive controls in report-only Weak RSI behavior; Public Relations versus GitHub pull-request terminology; internal preparation versus external authority; visibility versus credibility; and adoption metrics versus independent quality/assurance evidence.
- No application/runtime code, tests, workflows, providers, credentials, billing, repository settings or immutable backup/archive paths were executed, modified or inspected. Batch 074’s Python source and all tests remain static-review-only.
- **Updated coverage:** 291 preliminary full-file reviews + 5 partial targeted screens + 22 not reviewed = 318 active paths. Human validation remains pending; formal ISO 704 clause-level assessments completed: 0; scope remains proposed and not human-approved.

### Impact Analysis — Batches 074–075

**IF modified:** review status becomes traceable to exact source blobs; distinct status dimensions and the evidence-state/decision-state relationship become visible for human resolution; replication-state comparison can be standardized without implying external assurance. Tracker counts become consistent with documented dispositions.

**IF not modified:** the active review record would continue to overstate the number of unreviewed files while leaving the status taxonomy and replication-state ambiguities undisclosed; reviewers could compare unlike values or infer a decision result from an evidence label.

**Verification still required:** inspect the final PR diff and changed-path list; prove no backup/archive paths were added; verify tracker arithmetic and exact source SHAs; conduct designated human validation; reconcile dependent terminology rollouts and approved scope; obtain lawful controlled access to the complete ISO 704:2022 edition before populating its clause-level matrix. Overall status remains **NOT READY FOR AN ISO 704 AUDIT**.
