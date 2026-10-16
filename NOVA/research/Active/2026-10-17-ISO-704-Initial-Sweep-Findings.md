# ISO 704:2022 Initial Active-Content Sweep Findings

**Document ID:** NOVA-ISO704-FIND-001  
**Version:** 0.1.0  
**Snapshot date:** 2026-10-17  
**Status:** INITIAL FINDINGS — lexical screening only; not a completed conformity audit  
**Scope source:** [Proposed Scope and Repository Inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md)  
**Tracker:** [File-by-File Content Sweep Tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json)

## Method and limitations

This record captures the first lexical/content-fetch pass over selected active text files on their default `main` branches. Exact file content was retrieved and checked for selected canonical labels, old/new naming variants, certification and compliance language, and certain concept phrases. The scan is a discovery aid only. It does **not** decide ISO 704 conformity and does not substitute for semantic term-by-term human review, the full-standard matrix, or independent audit.

The six-repository inventory contains 318 active file paths. Fifteen files have so far been fetched and lexically screened in the tracker. Every tracker row remains `content_review_status: NOT_REVIEWED` and `terminology_assessment: NOT_ASSESSED` until a substantive entry-level content review and reviewer decision are recorded. The current lexical scan results do not change that.

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

### SWEEP-F-0002 — Oversized active NOVA README is not yet content-screened

- **Status:** BLOCKED — segmented review required
- **Severity for readiness:** Blocking to complete active-path coverage
- **Evidence source:** `ACROWN-System/NOVA`, `NOVA/README.md`, baseline blob SHA `54f8841675190c77ca7a4cbae3d9112f9fe49e90`, recorded size 1,452,321 bytes.
- **Observed result:** the file exceeds the present single-fetch size used in the initial sweep and has not been included among the 15 completed lexical fetches.
- **Interpretation:** absence of scan results is not evidence that terminology is consistent.
- **Required action:** inspect the file in bounded, sequential line ranges or another lawful text-processing method, record exact range/coverage, and identify embedded/duplicated sections or links that need normalization. If it contains composite snapshots, classify the segments rather than assuming the entire file is one coherent current source.
- **Closure evidence:** range manifest covering the entire active file, lexical results, recorded conflicts/duplicates and reviewer approval of the disposition.

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

## Initial scan coverage

- Initial repository path inventory: **318 active files** across six repositories.
- Files fetched and lexically screened in first pass: **15**.
- Files left without content review: **all 318** at the semantic reviewer-status level, because lexical screening does not satisfy content review.
- Oversized active file explicitly identified for segmented review: `NOVA/README.md`.
- Full ISO 704 clause/topic matrix: **BLOCKED** pending lawful controlled access to the complete edition and the baseline lifecycle check.
- Internal audit, corrective-action closure, management review and readiness GO decision: **NOT COMPLETED**.
- Provider discovery/accreditation checks: **DEFERRED until the complete readiness gate passes**.

## Next work queue

1. Close or formally disposition SWEEP-F-0001 after the dependent HSIAN naming changes are decided and validated.
2. Complete segmented review of SWEEP-F-0002 across all lines.
3. Continue the tracker sequentially across the remaining active text files, then assets/configuration formats; do not mark extension-based exclusions as N/A without rationale.
4. Review all certification-claim controls in live/public and technical surfaces and record evidence.
5. Build and validate the concept-system maps and cross-repository relationship register.
6. Do not claim the first lexical batch is an exhaustive audit or a successful audit.

