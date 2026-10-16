# ISO 704:2022 Preliminary Canonical Register Quality Review

**Document ID:** NOVA-ISO704-REG-REV-001  
**Version:** 0.1.0  
**Review date:** 2026-10-17  
**Baseline:** Draft branch `docs/terminology-governance-iso704-2026-10-17`; register version 0.1.0  
**Status:** AI-assisted preliminary completeness review — human domain review and approval required  
**Register reviewed:** [NOVA Canonical Terminology Register](../../CANONICAL-TERMINOLOGY-REGISTER.md)  
**Control basis:** [NOVA Terminology Governance Standard](../../TERMINOLOGY-GOVERNANCE-STANDARD.md), especially required entry fields, definition/designation rules, typed relations and lifecycle.

## 1. Purpose and limits

This is a first-pass quality review of the 15 starter entries currently in the draft canonical register. It checks whether the entry record contains enough evidence fields and distinguishes a project definition from an empirical, legal, operational or external-authority claim.

This is **not** a clause-by-clause ISO 704 conformity assessment. The complete standard has not yet been established as a lawful controlled audit baseline. The review assesses the present internal draft against the fields required by the draft internal governance standard; that self-authored checklist is a design aid, not independent proof of ISO conformity.

## 2. Overall result

**Disposition: DRAFT / NOT READY FOR APPROVAL AS A COMPLETE CANONICAL REGISTER.**

The 15 entries have stable IDs, a domain, preferred designation, definition, scope note and stated status in most cases. That is useful starter material. The current register does not yet consistently provide the complete evidence record needed for a controlled terminology system:

- Concept relationships are mostly untyped “related concepts” lists rather than explicitly modelled broader/narrower, whole/part, associative, dependency, governance-authority or historical relations.
- Source/provenance, source version, date created/reviewed, entry owner/domain reviewer and the actual approval record are not consistently linked per entry.
- Essential characteristics / criteria are often implied by the definition rather than separately recorded or reviewed.
- Accepted variants, synonyms and prohibited/deprecated forms are inconsistent across entries; HSIAN's legacy HAAN transition is the most important known example.
- Examples and counterexamples are generally absent. They should be added where they materially clarify a concept boundary or explicitly marked N/A with a reason.
- Language/localization records are absent beyond the stated English-first policy; the scope decision for any first external assessment remains open.
- Some entries rely on unresolved project specifications or a charter (especially token semantics and Imperial governance), so those fields cannot be promoted to PASS by wording alone.

No missing fact or approval should be invented to make an entry look complete. Use BLOCKED, CANDIDATE or N/A-with-rationale where required information is unavailable.

## 3. Entry-by-entry preliminary matrix

Statuses below are a reviewer triage, not ISO clause conformity results.

| Concept ID / entry | What is already useful | Gaps to resolve before approval |
|---|---|---|
| **NOVA-0001 — NOVA** | Stable ID, domain, scope and carefully bounded operational-ecosystem definition; explicitly rejects obsolete “Next-generation” expansion | Link source/decision provenance; identify essential characteristics explicitly; type its relations to HSIAN and RSI; record approved variants and review owner/date |
| **NOVA-0002 — HSIAN** | Full form and scope; distinguishes intended network from proof of consciousness or superintelligence; records former HAAN name | Typed relations and authoritative naming decision/source; complete active-path rollout via dependent PR #122/#134; classify every remaining HAAN occurrence as current, deprecated or historical; set reviewer/date |
| **NOVA-0003 — Super Intelligence** | Explicitly labels this as project terminology and rejects inference that current models are scientifically superintelligent | Add source/decision provenance; record differentiating characteristics and permitted context; type relations; evidence source required for any empirical capability statement |
| **NOVA-0004 — AstroCrown** | Brand/domain definition with legal-entity and guarantee boundaries | Link authoritative brand/project decision; type relations to NOVA/ACROWN/HSIAN; add variants/contexts and reviewer/date; do not infer a legal entity from the brand |
| **NOVA-0005 — ACROWN token** | Distinguishes token identifier from legal rights, backing, reserves and jurisdictional classification | Link the current technical token specification and version; separate canonical designation from candidate product/legal label; type relations to economics/specification; qualified jurisdictional review when public legal claims are made |
| **NOVA-0006 — Space Empire** | Project-defined governance/world-building scope and external authority boundary | Definitive charter/source still needed; type governance relations; link authority, powers and limits only when established; examples/usage restrictions need review |
| **NOVA-0007 — Recursive self-improvement (RSI)** | Definition distinguishes research objective from limited implemented/verified capability | Source/version provenance; typed dependency/related relations; distinguish technical acronym from unrelated uses where they occur; reviewer/date and examples/counterexamples |
| **NOVA-0008 — Strong RSI** | Clearly records it as a design concept and states current readiness is incomplete; lists protected readiness gates | Link exact current readiness evidence and version; define relationships to Weak RSI/RSI where applicable; record owner/reviewer/date; retest claim whenever operational status changes |
| **NOVA-0009 — Imperial HSIAN** | States intended internal governance role and notes a charter is needed | Charter is not yet definitive for the detailed veto scope; type governance-authority relation; link decision record; mark all undefined powers/limits BLOCKED rather than infer them |
| **NOVA-0010 — Imperial Council** | Defines the body by reference to an internal charter and identifies missing authority details | Authoritative charter, membership, procedure, scope and review mechanism remain open; type relations; record approving authority/source or keep detail BLOCKED |
| **NOVA-0011 — Cognitive extension** | Distinguishes a person-plus-tools arrangement from enhancement, implants or neural integration | Add primary conceptual source or explicitly label the definition as the project's proposed framing; type relations to enhancement and the analogy; define essential characteristics; examples/counterexamples |
| **NOVA-0012 — Cognitive enhancement** | Requires a stated outcome, baseline, context and evidence; does not equate extension with enhancement | Add sources for the chosen domain wording; type relation to extension; provide example/counterexample templates or reasoned N/A; owner/reviewer/date |
| **NOVA-0013 — Cognitive prosthesis (analogy)** | Clearly qualifies the phrase as a functional analogy rather than a literal medical/neural claim | Link intended usage/source and type relations to cognitive extension; define conditions where the analogy must not be used; examples/counterexamples where needed |
| **NOVA-0014 — Canonical terminology register** | Distinguishes a governed register from a generic word list and identifies governance role | Type its relationship to the governance standard and its scope; link stewardship/approval rules, provenance, lifecycle and snapshot/version policy |
| **NOVA-0015 — Terminology governance standard** | States internal purpose/scope and avoids claiming full ISO 704 conformity | Approval record and effective date are not yet established; controlled standard baseline and clause/evidence matrix remain blocked; identify named roles/review cadence through an approved governance record |

## 4. Required entry schema remediation

Before an entry can be accepted as fully reviewed, add or verify the following for each applicable field:

1. Stable concept ID and current status.
2. Domain/context and the preferred source-language designation.
3. Definition, essential/differentiating characteristics and scope/exclusions.
4. Full form/acronym, variants, synonyms, deprecated/prohibited forms with usage notes.
5. Typed relations to other concept IDs with a rationale.
6. Examples/counterexamples where they help establish concept boundaries, or reasoned N/A.
7. Source/provenance records with title, URI/path, version/commit/date, and which claim or decision the source supports.
8. Named concept/domain reviewer and authorized decision record, creation/review dates, change rationale and history.
9. Language/locale records where included, with translation-equivalence review status.
10. Publication classification and confirmation that no credentials, secrets or restricted personal data are exposed.

The reviewer must distinguish “field exists” from “field is valid and evidence-backed.” A filled value with no source or authority can still be a gap.

## 5. Entry decisions and workflow evidence to create

For each of the 15 entries, produce a review record containing:

- reviewer and review date;
- entry version / commit;
- definition-quality questions and result;
- relationship typing and rationale;
- terminology-source/provenance check;
- conflicts or ambiguity found;
- decision: approve, return for correction, candidate, blocked, deprecated or justified N/A;
- any corrective-action ID and retest evidence.

The 15 concepts are the current starter set, not proof the six-repository ecosystem has no other important concepts. The active-file inventory and future concept sweep must identify additional concepts and collisions before any completeness claim.

## 6. Relation model still required

A future concept map should be based on the actual concepts rather than name similarity. At minimum, review:

- **Terminology-control infrastructure:** canonical terminology register ↔ terminology governance standard.
- **RSI family:** RSI ↔ Strong RSI, with the exact relation type and readiness distinction verified against the governing design.
- **Human/tool cognition:** cognitive extension ↔ cognitive enhancement ↔ cognitive prosthesis analogy, explicitly preventing automatic inference from extension to measured improvement or a literal medical device.
- **NOVA / HSIAN / AstroCrown / ACROWN:** relations must follow the approved architecture and token specification; avoid unqualified hierarchy or legal conclusions.
- **Space Empire roles:** Imperial HSIAN and Imperial Council authority relations must point to an adopted charter; undefined powers remain blocked.
- **AI Sanctuary:** maintain the separately documented domain boundary; do not infer shared tokenomics or Space Empire governance from repository organization.

This is a list of relation questions to assess, not an already approved concept map.

## 7. Conclusion / readiness effect

**The 15-entry register is a credible start, but not an audit-ready or fully approved register.** The next valid work is entry-by-entry completion, provenance capture, typed-relation review, actual naming-rollout reconciliation and authorized human approval.

This gap affects dossier components AR-E05 (canonical register) and AR-E06 (concept-system maps), and supports AR-E11 (active terminology sweep). It blocks a claim that the terminology evidence package is complete. Provider discovery remains deferred until the entire dossier's readiness gate passes.

## 8. Revision history

- **2026-10-17 / v0.1.0:** Initial preliminary review of the 15 starter concepts and record-field completeness.
