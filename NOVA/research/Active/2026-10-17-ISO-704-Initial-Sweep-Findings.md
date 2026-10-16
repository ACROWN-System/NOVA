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
