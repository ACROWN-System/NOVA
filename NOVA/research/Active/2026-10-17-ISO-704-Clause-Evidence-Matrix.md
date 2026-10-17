# ISO 704:2022 Clause/Topic-to-Evidence Matrix — Controlled Template

**Document ID:** NOVA-ISO704-MATRIX-001  
**Version:** 0.1.0  
**Status:** TEMPLATE ONLY — NOT A COMPLETED MATRIX  
**Date opened:** 2026-10-17  
**Owner:** Designated human maintainer  
**Standard baseline:** ISO 704:2022, Edition 4 — full controlled text not yet established  
**Readiness status:** COMPLETE MATRIX remains blocked until the applicable edition and full clause/section inventory are established; separate source-bounded preview mapping may proceed  
**Related dossier:** [ISO 704:2022 Audit-Readiness Dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md)

## 1. Purpose

Use this controlled template to assess every relevant section/clause of the exact ISO 704:2022 edition against project controls and objective evidence. The current file is only the structure for future work. It contains no clause-level conclusions and must not be presented as a completed conformity matrix.

Do not create rows from memory, search-result snippets, an abstract or another standard. Exact locations and content directly visible in an identified, traceable standards preview may be summarized in a separate partial mapping with source and coverage limits. Do not use this complete-matrix template to imply total coverage; the full inventory and final baseline still require the applicable edition and all relevant sections to be accounted for. Do not reproduce protected ISO text; capture a concise project-authored paraphrase and record the actual type of statement being assessed.

## 2. Matrix row schema

Create one row per clause/section or a documented grouping that preserves complete traceability. A grouping is acceptable only when every included clause can still be located and its applicability/result can be verified independently.

For each row, record:

- **Matrix row ID:** stable local identifier, for example `M-0001`.
- **ISO 704:2022 location:** exact clause/section identifier and heading as verified against the controlled copy.
- **Statement type/force:** requirement, principle, recommendation, descriptive explanation, definition, example, or other accurately characterized type. Do not call every passage a mandatory requirement.
- **Project-authored paraphrase:** short summary in original words; do not paste the copyrighted clause.
- **Applicability:** applicable / partly applicable / not applicable / blocked, with rationale and approved scope reference.
- **Project control:** procedure, register field, governance control or actual operational practice intended to address the point.
- **Quality / operability rationale:** the real terminology problem and expected improvement; do not propose a change merely to match a presentation pattern.
- **Non-regression review:** effect on meaning, necessary nuance, domain boundaries, discoverability, navigation, automation, retrieval, maintainability and backward compatibility.
- **Alternatives and disposition:** include no change where relevant; ACCEPT / ADAPT / REJECT / DEFER with documented rationale.
- **Evidence IDs:** IDs from the readiness dossier's evidence register, plus exact path, URL, version, branch/commit or snapshot.
- **Verification method:** inspection, record trace, interview, observation, sample review, repeatable search or other justified method.
- **Test result:** PASS / FAIL / BLOCKED / N/A. No result is assigned without actual verification.
- **Finding/reference:** link to a finding ID where a gap, conflict or uncertainty is recorded.
- **Owner and target date:** person accountable for closure, where relevant.
- **Correction/corrective action:** actions taken or planned to address a finding, with root-cause notes where appropriate. Describe any documentation/context-preservation or migration steps needed to avoid regression.
- **Closure and retest evidence:** exact record demonstrating the fix and the independent/appropriate re-test.
- **Reviewer/date:** who assessed the row and when; record conflicts of interest or limitations.
- **Notes / unresolved interpretation:** questions that require review; do not decide ambiguous points by guessing.

## 3. Empty row template

Duplicate this section for each verified section/clause or documented grouping. The fields intentionally remain unpopulated until the controlled edition is available.

### M-____ — [verified section/clause identifier]

- **ISO 704:2022 location:** BLOCKED — not populated
- **Statement type/force:** BLOCKED — verify against controlled edition
- **Project-authored paraphrase:** BLOCKED — write only after review
- **Applicability and rationale:** BLOCKED
- **Project control(s):** NOT MAPPED
- **Evidence IDs and exact source versions:** NOT MAPPED
- **Verification method:** NOT DEFINED
- **Result:** BLOCKED
- **Finding ID / gap:** PENDING
- **Owner / target date:** PENDING
- **Correction / corrective action:** PENDING
- **Closure / retest evidence:** PENDING
- **Reviewer / date:** PENDING
- **Open question / notes:** PENDING

## 4. Matrix-completeness controls

Before the matrix can support readiness:

1. Record the exact edition and controlled-copy metadata, lawful access basis and custodian.
2. Inventory every section/clause, definitions and other relevant material in the complete edition; reconcile the inventory against the document's contents.
3. Ensure every location is represented directly or through a documented and traceable grouping.
4. Record statement force accurately and justify all applicability / N/A decisions.
5. Link each applicable row to a real implemented control and objective evidence; document where evidence shows only design intent.
6. Assign results only after performing the stated verification method.
7. Link all FAIL/BLOCKED outcomes to findings and corrective-action records.
8. Re-test corrections and preserve original finding history.
9. Have a reviewer other than the row author review matrix completeness and any significant interpretation.
10. Confirm no copied proprietary clause text or prohibited standard distribution has entered the repository.
11. Include a manifest/version/commit for the final matrix snapshot.
12. Reconcile the matrix's row inventory to the full controlled standard before concluding it is complete.

## 5. Current status

**BLOCKED / NOT STARTED AS A COMPLETE CLAUSE-LEVEL ASSESSMENT.** The project has not established the complete applicable ISO 704:2022 baseline or reconciled every relevant clause/section. This template remains blank as the complete matrix. Source-bounded assessment of provisions directly visible in public previews may proceed in a separate record, currently [Public-Preview Partial Mapping](2026-10-18-ISO-704-Public-Preview-Partial-Mapping.md). No paid access is authorized by this template and no conclusion is drawn for text not directly inspected.

The readiness dossier defines the wider evidence package, internal audit, corrective-action and management decision gates. Provider discovery remains deferred until the full package passes those gates.


## 6. Project-action quality gate (does not replace the standard's own statement type)

For each proposed project change that follows from a completed row or partial preview mapping, ask:

1. Does the change correct an evidenced concept/term/definition/relation problem?
2. Does it improve clarity, retrieval, communication, interoperability, traceability or operability for the intended users and domain?
3. What semantic richness, explanatory context, domain-specificity or working behaviour could be lost?
4. Could a note, typed relation, separate definition, example, alias or cross-reference improve clarity without destructive rewriting?
5. What is the reasoned disposition if the current design is better for the stated project purpose?

Record **ACCEPT / ADAPT / REJECT / DEFER** as a project-action disposition, separately from any assessment result concerning the standard. Never use rejection of a proposed project change to imply the standard itself has been satisfied. The project-action gate may preserve project quality; it does not override an actual standard requirement or permit an unsupported conformity claim.
