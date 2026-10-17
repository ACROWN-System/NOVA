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


## Execution update — 2026-10-18 — semantic review Batch 076

- Reviewed five previously unreviewed active AstroCrown-Web verification documents at exact blob SHAs from baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`: competitor verification benchmark, verification architecture, tracking system, strategic prioritization and gap analysis.
- Reconciled the row-level tracker with exact source commit/blob, evidence ID, disposition, reviewer/date and findings for all five files. Updated top-level counts to 296 preliminary full-file reviews + 5 partial targeted screens + 17 not reviewed = 318 active paths.
- Opened preliminary SWEEP-F-0056 for missing item-level source provenance in competitor benchmark observations; SWEEP-F-0057 for undefined qualitative category criteria in strategic prioritization; and SWEEP-F-0058 for the proposed archive subtree’s relationship to the immutable archive-path and active-review-exclusion rules.
- Extended SWEEP-F-0054's context to the tracking system's explicit distinction between evidence state and operational status. This distinction is a useful positive control; repeated labels must retain their field semantics.
- Confirmed that the Gap Analysis uses NOT CONFIRMED/BLOCKED rather than asserting unavailable items are absent. Its current MDN HTTP Observatory naming is consistent with the official MDN Observatory FAQ checked 2026-10-18.
- No runtime code, tests, workflows, external providers, credentials, billing, repository settings or immutable backup/archive contents were accessed, executed or changed.
- Human validation is pending, formal ISO 704 clause-level assessments completed remain 0, and scope remains proposed/not human-approved. Overall status remains **NOT READY FOR AN ISO 704 AUDIT**.

### Impact Analysis — Batch 076

**IF modified:** benchmark claims can be traced to their sources; priority labels can be applied consistently without collapsing independent dimensions into a score; and the meaning/placement of the archive layer can be reconciled with immutable-path rules before implementation. Tracking records can preserve evidence-state versus operational-status semantics.

**IF not modified:** competitor claims remain difficult to reproduce, independent reviewers may apply qualitative categories differently, and the proposed archive path may conflict with the scope-exclusion/immutability rules. Status values may be interpreted outside their intended field dimension.

**Verification still required:** verify the final PR changed-file list; ensure no backup/archive path is added; confirm tracker arithmetic and exact source SHAs; human-validate all new findings; resolve the source-of-truth and archive classification; acquire lawful controlled access to the complete applicable ISO 704 edition before filling the clause/topic matrix. No audit-readiness claim is authorized.


## Execution update — 2026-10-18 — semantic review Batch 077

- Reviewed five previously unreviewed AstroCrown-Web verification documents at exact blob SHAs from baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`: Investigation Backlog, U.S. Federal SI Terminology and Audit Context, Assessments README, Benchmarks README and Evidence Extracts README.
- Reconciled each row in the tracker with the exact reviewed source commit/blob, evidence ID, disposition, reviewer/date and findings. Updated the counts to 301 preliminary full-file reviews + 5 partial targeted screens + 12 not reviewed = 318 active paths.
- Opened preliminary SWEEP-F-0059 for the document-level `Evidence state: VERIFIED` label in the Federal SI terminology file, because the same document includes verifiable official-source propositions, derived AstroCrown relevance and a candidate project policy without explicitly scoping that overall status.
- Checked the official White House Executive Order 14434 and 15 U.S.C. § 9401(3) on 2026-10-18. The review preserves the distinction between executive-branch terminology direction, existing statutory definition, proposed future legislative language, and AstroCrown policy candidacy. No legal opinion is claimed.
- Recorded positive controls in the unresolved-research backlog’s warning against silent evidence-state rewriting; the assessments layer’s facts/interpretation/candidacy/blocked distinction; the benchmark layer’s anti-duplication rule; and the extracts layer’s source-authority rule.
- No runtime code, tests, workflows, provider calls, credentials, billing, repository settings or immutable backup/archive contents were executed, changed or inspected.
- Human validation remains pending; formal ISO 704 clause-level assessments completed remain 0; scope remains proposed/not human-approved; overall status remains **NOT READY FOR AN ISO 704 AUDIT**.

### Impact Analysis — Batch 077

**IF modified:** the federal terminology document’s evidence metadata can accurately distinguish source-backed legal propositions from project interpretations and candidate policy; research, assessment, benchmark and extract artifacts remain semantically separated; and review counts match the verified source rows.

**IF not modified:** downstream users could treat a document-level VERIFIED label as approval of recommendations, even though the document itself labels its project policy as a candidate. The review queue and derivative evidence layer would also be more vulnerable to confused scope if their existing boundary rules were not retained.

**Verification still required:** inspect the final PR diff and changed-path list; ensure no backup/archive path was added; verify tracker arithmetic and exact source SHAs; human-validate all findings; review status-field use in related records; acquire lawful controlled access to the full applicable ISO 704 edition before populating the clause/topic matrix. No audit-readiness claim is authorized.


## Execution update — 2026-10-18 — semantic review Batch 078

- Reviewed five previously unreviewed AstroCrown-Web verification documents at exact blob SHAs from baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`: evidence README, snapshot README, dated external-source index, operations changelog and verification entity schema.
- Reconciled all five tracker rows to their exact reviewed source commit/blob, evidence ID, disposition, reviewer/date and finding references. Updated counts to 306 preliminary full-file reviews + 5 partial targeted screens + 7 not reviewed = 318 active paths.
- Opened preliminary SWEEP-F-0060 because the External Source Index is a useful discovery list but does not on its own give each entry a reproducible claim-level provenance record or establish individual currentness; the index/provenance distinction should be explicit.
- Opened preliminary SWEEP-F-0061 because `operations/SCHEMA.md` lists the intended entity fields but does not by itself define structural or semantic constraints. The owner should clarify whether it is a conceptual field inventory or normative schema and align it with the status/evidence vocabularies.
- Recorded positive controls in the evidence layer’s source/snapshot/extract distinctions; the snapshots instruction not to overwrite historical captures; and the changelog’s dated history and append-not-overwrite intention.
- Checked the White House Executive Order 14434 URL and 15 U.S.C. § 9401 as representative official-source spot checks on 2026-10-18. This did not validate every URL or source in the dated index.
- No runtime code, tests, workflows, credentials, external provider calls, billing, repository settings or immutable backup/archive contents were executed, changed or inspected.
- Human validation remains pending; formal ISO 704 clause-level assessments completed remain 0; scope remains proposed/not human-approved. Overall status remains **NOT READY FOR AN ISO 704 AUDIT**.

### Impact Analysis — Batch 078

**IF modified:** the distinction between a source-discovery list and claim-level provenance can be made explicit; consequential claims can link to appropriate, versioned evidence; and the entity schema can be made unambiguous about whether it is a field catalogue or the normative record contract. This helps prevent a URL’s presence or a field name’s existence being treated as more evidence than it provides.

**IF not modified:** users may mistake a discoverability index for confirmation of a claim’s source scope/currentness, or treat a bare list of field names as a complete validation contract. Those risks would make the evidence system harder to reproduce and compare.

**Verification still required:** verify the final PR changed-file list and immutable-path boundary; reconcile tracker arithmetic and exact source SHAs; human-validate findings; perform any full URL/currentness audit called for by the source policy; resolve the intended schema role and its relation to the separate controlled-status vocabulary; and obtain lawful controlled access to the full applicable ISO 704 edition before populating its clause/topic matrix. No audit-readiness claim is authorized.

## Execution update — 2026-10-18 — human-approved planning scope and $0-only access policy

- The human maintainer explicitly approved the proposed six-repository planning scope: NOVA, Freebies-, AstroCrown_ACS_MC_Spec, AI-Sanctuary-Core, ACROWN-SIMULATION-LAB and AstroCrown-Web.
- English is the initial assessment language. Translation/localization and any assertion of cross-language equivalence remain outside the initial scope unless a later explicit scope change and supporting evidence are recorded.
- AI-Sanctuary-Core remains a separate identity/governance domain; its inclusion for scoped terminology review does not integrate its governance with AstroCrown tokenomics or Space Empire governance.
- The human maintainer reaffirmed a hard $0-only access policy. No standard purchase, paid subscription/membership, billable inquiry, hired adviser/provider or other cost is authorized. Only existing lawful access or verified no-cost consultation routes may be pursued.
- If lawful no-cost access to the complete applicable ISO 704 edition is not confirmed, AR-E02 remains BLOCKED and the clause/topic-to-evidence matrix stays unpopulated. Public abstracts and snippets are insufficient.
- Updated the scope proposal, audit-readiness dossier, standard-access investigation and machine-readable sweep tracker to reflect the decision. Scope direction is approved for planning; final baseline freeze, assessment period, exact refreshed commit/path manifest, roles/independence, external-publication boundaries, human validation, partial-screen completion/disposition and the Batches 029–036 report-artifact gap remain open.
- No purchase, billable inquiry, provider outreach, standard copy acquisition, runtime/code/test/workflow change or backup/archive modification was performed.

### Impact Analysis — scope approval and $0-only access policy

**IF recorded and followed:** the intended repositories and initial language are stable for planning, domain separation is explicit, and the access-cost boundary is enforceable and auditable. Work can continue on internal evidence without either guessing at clauses or implicitly authorizing spending.

**IF not recorded or followed:** the scope could keep being described as unapproved, project domains could be conflated, or the team could mistake an information lead for authorization to incur fees or use non-controlled text.

## Execution update — 2026-10-18 — standard access research

- The official ISO product page and BIS library/standards pages were rechecked. ISO lists ISO 704:2022, Edition 4, as published; the page offers sample/preview access and displays CHF 204. The BIS library page lists paid annual reference membership. The public BIS portal does not verify free access to the complete ISO 704 text.
- No lawful no-cost route to the complete applicable text was confirmed in the inspected public sources. This does not establish that existing institutional access is unavailable.
- Updated the access investigation, readiness dossier AR-E02 and tracker. AR-E02 remains BLOCKED and the clause/topic-to-evidence matrix remains a template only. The approved $0-only access policy remains in force.
- No purchase or billable inquiry was made; no source/runtime changes or backup/archive changes were made.

### Impact Analysis — standard access research

**IF recorded:** the project can distinguish public preview access from a controlled full-text baseline and retain a traceable reason for the current BLOCKED status.

**IF not recorded:** the access state could be inferred from partial public material instead of verified evidence.

## Execution update — 2026-10-18 — scope decision and expanded no-cost access search

- Human maintainer approval is recorded for the six-repository planning scope and English as the initial assessment language. The final assessment baseline is not frozen. AI-Sanctuary-Core remains a distinct identity/governance domain.
- The $0-only rule is binding. No purchase, paid library membership/subscription, billable enquiry, hired service, or provider outreach is authorized.
- The expanded search found no verified lawful no-cost online access to the complete applicable ISO 704 text. ISO's official OBP free preview is restricted to selected sections; full text has not been verified as free.
- The official ISO product record still lists ISO 704:2022 Edition 4 as published. A separate public standards-body listing shows ISO/PWI 704 at proposal stage, not a published successor. The latter requires authoritative lifecycle confirmation before final baseline freeze.
- IIT Delhi Central Library is a possible in-person route to ask about: it lists subscriptions to ISO standards and a library-visit facility for outside users, but public pages do not confirm no-cost access for a non-member to this exact standard. Only a free informational inquiry is appropriate. AR-E02 remains BLOCKED and the clause matrix remains template-only.
- Added the detailed report [Expanded Search — Lawful No-Cost Access to ISO 704 and Current Lifecycle](2026-10-18-ISO-704-Expanded-Free-Access-and-Lifecycle-Research.md), updated the access investigation and dossier, and reflected the access lead in the tracker.
- Batches 079 and 080 have recorded preliminary dispositions for the last seven outstanding active paths: 5 files in Batch 079 and 2 in Batch 080. Tracker arithmetic is 313 preliminary full-file reviews + 5 partial targeted screens + 0 unreviewed = 318. Human validation remains pending for all 313 full-file reviews; formal clause-level assessments remain zero. Finding SWEEP-F-0062 remains open.

### Execution incident — branch target omission and prevention

One create-file call for the expanded access report omitted its optional branch argument, so GitHub created the file on the default branch. Verification caught the mismatch; the report was recreated on the intended ISO review branch and deleted from the current default-branch tree with a follow-up commit. The current branch contains the artifact only at the intended path; no runtime/source file or backup/archive path was changed.

**Root cause:** the write API defaults to the repository's default branch when `branch` is omitted, and the call did not enforce explicit target-ref input.

**Prevention:** every create/update/delete call in this workstream must explicitly specify the intended branch, then re-fetch the exact path on that same branch immediately after the write. Where a routing mistake is suspected, verify the default-branch tree separately; do not rewrite history.

### Impact Analysis — expanded access and branch control

**IF followed:** scope/cost decisions and standard-access limits stay auditable, and write operations stay inside the intended review branch.

**IF not followed:** the project risks treating a preview or proposal as a controlled standard, incurring an unauthorized cost, or bypassing review-branch change control.



## Decision correction — source-bounded conformance work without certification (2026-10-18)

The earlier sequencing statement that full clause-level conformity work must remain entirely blocked until complete-text access is confirmed is refined as follows. **Only completion of the controlled baseline, the complete clause inventory/matrix, and the overall readiness conclusion remain blocked by the unresolved full-text gap.** The absence of a purchased copy or external certificate is not a reason to suspend all terminology improvement.

- Continue improvements to NOVA's canonical terminology concepts, definitions, designations, domains and relations using internally evidenced practices and principles directly available from identified public previews.
- Keep public-preview work in the separate [ISO 704:2022 Public-Preview Partial Mapping](2026-10-18-ISO-704-Public-Preview-Partial-Mapping.md). Use original paraphrase, direct source/edition/location references and scope labels. Mark every unseen clause/annex NOT ASSESSED; never infer PASS, FAIL or N/A from a table of contents, abstract, search snippet or memory.
- Keep the full clause/evidence matrix as a controlled template until the complete applicable edition and inventory are reconciled. The partial map is not a complete matrix, a full-conformity finding or an audit/certification claim.
- ISO says it does not itself provide certification or conformity assessment (https://www.iso.org/contact-iso.html). The bounded search found no evidence of a dedicated third-party ISO 704 certification scheme; this is not proof none exists. External certification/provider discovery is not the objective and remains unauthorized unless the human maintainer separately changes scope.
- The $0-only policy remains binding. No purchase, paid subscription/membership, billable enquiry, hired adviser/provider or other cost is authorized.

**Impact Analysis — IF this correction is followed:** accessible text can drive real improvements while full coverage remains transparently unresolved and payment/certification are not mistaken for conformance prerequisites. **IF not followed:** the process may unnecessarily suspend useful improvement, or conversely overstate coverage based on partial source visibility.


## Quality-preservation rule — ISO 704 as a means, not a destructive checklist (2026-10-18)

The purpose of applying ISO 704 is to **increase the quality, precision, coherence, retrieval and operability of terminology** across NOVA and its scoped project domains. The standard must not be applied mechanically in a way that weakens those qualities, discards essential context, flattens domain boundaries, or forces unrelated architecture and workflow documentation into terminology-entry shapes.

Apply the [Quality Preservation and Non-Regression Plan](2026-10-18-ISO-704-Quality-Preservation-and-Non-Regression-Plan.md) to material changes:

- Establish the real problem, existing intent and supporting evidence before changing a concept or document.
- Compare the proposed state with the current state, including benefits and possible losses to meaning, nuance, usability, navigation, automation, retrieval, maintainability, security boundaries, compatibility and domain integrity.
- Prefer additive clarification (separate definition, scope note, example, relation, synonym/alias or cross-reference) over destructive simplification when both solve the problem.
- Preserve useful explanatory material even when a more concise canonical definition is introduced. A definition, an explanatory account and an operational procedure have different purposes and should not be collapsed into one artifact.
- Record alternatives, including no change, and use ACCEPT / ADAPT / REJECT / DEFER with rationale. Use the required Impact Analysis: **IF modified** and **IF not modified**.
- Do not alter runtime or business meaning merely to satisfy a preferred label or make a matrix easier to complete. Changes affecting a schema, API, workflow, permission, security boundary or public commitment need the appropriate separate change process.
- When the project's sound domain requirements and a proposed interpretation appear to conflict, do not hide the conflict or claim automatic conformity. Investigate the actual source, assess alternatives and document the decision and any residual non-conformity/uncertainty honestly.

This is a project quality control, not permission to misrepresent an actual ISO provision. The full applicable text is not yet available for every provision; any conflict with a genuinely mandatory requirement must be assessed once it can be read. Unseen provisions remain NOT ASSESSED.

**Impact Analysis — IF applied:** ISO 704 techniques help correct real terminology weaknesses while preserving the project's conceptual richness and operation. **IF not applied:** cargo-cult standardization can flatten useful distinctions, add needless bureaucracy, damage navigation or create paper compliance without operational improvement.
