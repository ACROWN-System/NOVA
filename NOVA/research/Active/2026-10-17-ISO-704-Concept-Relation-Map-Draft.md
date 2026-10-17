# ISO 704:2022 Draft Concept-Relation Map — Starter Register

**Document ID:** NOVA-ISO704-CONCEPT-MAP-001  
**Version:** 0.1.0  
**Date:** 2026-10-17  
**Status:** CANDIDATE MAP — NOT APPROVED; complete standards baseline unavailable  
**Source register:** [NOVA Canonical Terminology Register](../../CANONICAL-TERMINOLOGY-REGISTER.md)  
**Quality review:** [Preliminary Register Quality Review](2026-10-17-ISO-704-Register-Quality-Review.md)

## 1. Purpose and boundaries

This draft makes relationships among the 15 starter concepts explicit enough to review. It is not a finished formal concept system, and it does not claim conformity to ISO 704:2022. The complete licensed standard has not been established as the controlled audit baseline, and all relationships below require human domain review before they become canonical.

Use relationship categories carefully. Broader/narrower and whole/part are different semantic relations. Associative relations must not be used as a catch-all substitute for a defensible hierarchy. Governance/administrative relationships (e.g. “governed by” or “authority assigned by a charter”) are recorded separately from concept-hierarchy relations.

## 2. Candidate concept relations

| Relation ID | From | Relation type | To | Rationale / boundary | Status |
|---|---|---|---|---|---|
| CR-001 | NOVA-0008 Strong RSI | NARROWER CONCEPT / KIND OF | NOVA-0007 Recursive self-improvement (RSI) | Register defines Strong RSI as the intended higher-autonomy RSI capability; it should remain a subtype only if the domain reviewer confirms that the broader/narrower logic is appropriate | CANDIDATE — human validation required |
| CR-002 | NOVA-0012 Cognitive enhancement | ASSOCIATIVE — distinct outcome concept | NOVA-0011 Cognitive extension | Extension does not itself establish a measured enhancement; the two are related but should not be conflated or treated as automatic broader/narrower concepts | CANDIDATE — human validation required |
| CR-003 | NOVA-0013 Cognitive prosthesis (analogy) | EXPLANATORY ANALOGY | NOVA-0011 Cognitive extension | Register presents the former as a qualified functional analogy, not a medical device or literal neural integration. Keep this relationship distinct from hierarchical concept relations | CANDIDATE — human validation required |
| CR-004 | NOVA-0002 HSIAN | ASSOCIATIVE — participant/network model | NOVA-0003 Super Intelligence | The HSIAN definition refers to Super Intelligence participants, but this does not mean present models are superintelligent or that a coordinated network is operational | CANDIDATE — human validation required |
| CR-005 | NOVA-0004 AstroCrown | ASSOCIATIVE — ecosystem-related token | NOVA-0005 ACROWN token | Register identifies the token as associated with the ecosystem; do not infer legal entity status, ownership, asset backing, guaranteed rights or a formal whole/part relation | CANDIDATE — human validation required |
| CR-006 | NOVA-0001 NOVA | ASSOCIATIVE — project architecture relation | NOVA-0002 HSIAN | These concepts are part of the intended ecosystem vocabulary, but the exact architectural dependency/relation has not yet been formally established in this register | BLOCKED — obtain approved architecture source |
| CR-007 | NOVA-0001 NOVA | ASSOCIATIVE — project ecosystem relation | NOVA-0004 AstroCrown | The projects are coordinated in the cross-ecosystem terminology scope; do not infer that one is a legal parent of the other | CANDIDATE — human validation required |
| CR-008 | NOVA-0006 Space Empire | ASSOCIATIVE — governance context | NOVA-0009 Imperial HSIAN | The register locates the role inside the Space Empire framework, subject to an authoritative charter | BLOCKED — charter is not definitive |
| CR-009 | NOVA-0006 Space Empire | ASSOCIATIVE — governance context | NOVA-0010 Imperial Council | The register locates the council inside the project governance model, while membership, powers and procedures remain open | BLOCKED — charter is not definitive |
| CR-010 | NOVA-0014 Canonical terminology register | GOVERNED-BY (administrative relation, not broader/narrower) | NOVA-0015 Terminology governance standard | The standard is intended to control register maintenance, approval, publication and review. Confirm this administrative relation during approval of the governance design | CANDIDATE — human validation required |

## 3. Relationship and authority records that must remain separate

The following are not approved merely because this map lists them:

- **Definitions versus empirical claims:** the “Super Intelligence” project term does not certify a model's capability. Empirical capability claims require independent task-specific evidence.
- **Brand/token versus legal status:** the AstroCrown and ACROWN entries do not settle entity status, ownership, rights or regulatory classification.
- **Governance vocabulary versus charter authority:** “Imperial HSIAN” and “Imperial Council” names do not define lawful or external powers. The authoritative internal charter must establish scope, procedures, limits and decision records.
- **Draft design versus deployment:** RSI and Strong RSI definitions do not prove current implementation/readiness.
- **Historical term versus current designation:** HAAN may remain in legitimate historical evidence; active current use requires post-merge classification under the HSIAN rollout change set.

## 4. Candidate concept-system view

```text
Terminology governance standard --governs--> canonical terminology register

RSI
└── Strong RSI (candidate narrower concept)

Cognitive extension
├── Cognitive enhancement (associated, distinct measured-outcome concept)
└── Cognitive prosthesis (analogy) (explanatory analogy; not literal device)

HSIAN --associated with participant/model concept--> Super Intelligence

AstroCrown --associated with--> ACROWN token

Space Empire
├── Imperial HSIAN (charter-dependent role)
└── Imperial Council (charter-dependent body)

NOVA --project-architecture relation unresolved--> HSIAN
NOVA --cross-ecosystem relation, not legal parenthood--> AstroCrown
```

This textual view is only a navigation aid. The table's status values control the interpretation, and blocked relations must not be promoted to canonical without evidence.

## 5. Validation checklist

For each relationship row, the reviewer must confirm:

1. The relation's type and direction are correct for the concepts' meanings.
2. It is not confused with whole/part, broader/narrower, simple association, a naming synonym, a governance authority, or a dependency.
3. Source evidence explains why the relationship is valid.
4. Both concept entries are sufficiently complete and their statuses support the relation.
5. No relationship implies consciousness, deployment, legal status, financial rights, external authority or certification without evidence.
6. The relation is updated alongside changes to either concept and receives a traceable review record.

## 6. Current readiness effect

**AR-E06 — Concept-system maps: DRAFT / NOT APPROVED.** This map provides candidate relations and explicitly blocked questions; it does not close the evidence component. A complete concept map must cover all approved concepts in the final agreed scope, with reviewed relations, rationales, provenance and change history.

## 7. Revision history

- **2026-10-17 / v0.1.0:** Initial candidate relation map for the 15 starter concepts; no relationships approved by this document.
