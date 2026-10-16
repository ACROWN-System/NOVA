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
