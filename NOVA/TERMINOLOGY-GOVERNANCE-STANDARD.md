# NOVA Terminology Governance Standard

**Document ID:** NOVA-TERM-GOV-001  
**Version:** 0.1.0  
**Status:** PROPOSED INTERNAL STANDARD — controls are being established; conformity has not yet been demonstrated.  
**Owner:** NOVA governance / designated human maintainer  
**Scope:** Canonical terminology and concept management for the AstroCrown–NOVA–HSIAN ecosystem and related projects, systems, services, technical architecture, governance, public communications and localization.  
**Intended alignment:** ISO 704:2022, *Terminology work — Principles and methods*; terminology vocabulary reference ISO 1087:2019.

**Certification statement:** This is an internally authored practice standard. It is not published or endorsed by ISO, does not reproduce ISO 704, and is not a certificate or declaration of full ISO 704 conformity.

## 1. Purpose

Establish one evidence-led, auditable source of truth for concepts, names, definitions, terms, acronyms, relationships and language rules used across the ecosystem. The system must support internal engineering and governance, consistent public communication, cross-repository coordination, multilingual usage, AI-assisted work and future independent audit.

The canonical register is maintained in [CANONICAL-TERMINOLOGY-REGISTER.md](CANONICAL-TERMINOLOGY-REGISTER.md). The public-facing implementation and writing requirements belong in AstroCrown-Web's brand language and terminology governance document, linked from the register's cross-repository implementation plan.

## 2. Standards basis and honest conformity boundary

ISO's public description of ISO 704:2022 says it establishes principles and methods for preparing and compiling terminology; describes relations between objects, concepts, definitions and designations; and addresses formation of terms/proper names and writing definitions. It applies across technical, scientific, industrial, legal, administrative and other fields. ISO 1087:2019 provides terminology-work vocabulary.

This internal standard is designed around those published subject areas and established terminology-management principles. Because the complete licensed text of ISO 704:2022 has not been adopted as an available project audit baseline, a clause-by-clause conformity claim is **BLOCKED**. Do not state “ISO 704:2022 compliant,” “certified,” or “certifiable” as an already verified fact based only on this document. At the same time, do not present certification as impossible or remove it from consideration: **pursuing a credible route to independent certification is an explicit strategic objective, subject to confirming that an appropriate provider offers it and that the project satisfies its criteria.**

The accurate current description is:

> The project is establishing an internal terminology-governance system designed for alignment with the published scope of ISO 704:2022. Full clause-level conformity assessment is pending, and an appropriate independent certification route is being investigated.

Before making a formal clause-level conformity claim, obtain lawful access to the complete standard, build a controlled requirements/evidence matrix using the exact edition, record gaps and non-applicable requirements, remediate gaps and complete an independent review. Do not copy or distribute the standard's copyrighted text in project documentation. ISO itself does not issue certificates; external bodies perform certification. Current public-source research has not verified an ISO 704-specific certification offering for this project. This is an evidence gap, not proof that no suitable provider exists.

### 2.1 Certification feasibility and pursuit pathway

Certification feasibility is a **required research workstream**, not a guarantee of certification and not a reason to defer internal implementation. The project intends to investigate and pursue a credible independent certificate if an appropriate provider will certify this scope.

The following route must be completed before stating that such a certificate is available:

1. **Find candidate assessors:** identify independent certification bodies or other competent conformity-assessment providers with demonstrable terminology, language-service, information-quality or relevant standards expertise.
2. **Ask the decisive question in writing:** will the provider issue a certificate specifically attesting conformity to ISO 704:2022, and under what named scheme, defined scope, criteria and assessment method? If it offers only consulting, training, a maturity review, an internal-audit service or an audit report, record that accurately; do not call it certification.
3. **Verify accreditation and recognition:** establish whether the issuer is accredited for the exact certification activity/scope, by which accreditation body, and whether that body's published scope supports the claim. Do not infer accreditation from the word “certification body” or from unrelated accredited schemes.
4. **Establish the criteria:** obtain the provider's written requirements and confirm that it assesses the actual ISO 704:2022 edition rather than an unrelated proprietary checklist, a general quality-management certificate or a provider's training course.
5. **Build readiness evidence:** obtain lawful access to the complete ISO edition, map applicable clauses to internal controls and objective evidence, assess gaps, implement corrective actions, and complete a documented internal audit and management review.
6. **Independent pre-assessment:** where the provider offers it, use a clearly labelled gap assessment before formal application. A readiness assessment is not a certificate and must not be represented as one.
7. **Decision and public wording:** retain the provider's proposal, scheme details, assessment report, accreditation evidence, certificate scope/number/validity and any use-of-mark rules. Publish a certification claim only after a valid certificate has actually been issued and checked.

Use these research statuses:
- **CANDIDATE:** a potential provider or route has been identified but not confirmed.
- **BLOCKED:** no written evidence establishes that a provider offers a suitable ISO 704:2022 certificate, or a prerequisite needed to assess conformity is unavailable.
- **VERIFIED AVAILABLE:** a competent provider confirms in writing the exact certificate, scheme and scope it can issue; accreditation status is separately documented.
- **APPLIED / ASSESSED / CERTIFIED:** separate statuses requiring evidence of each actual event. Do not skip steps.

A non-accredited certificate, independent audit opinion and accredited certification are different outputs. If an accredited certification scheme is unavailable, the project may still seek an independent audit/conformity statement and may investigate whether a qualified provider can establish a defensible scheme. Such an alternative must be described precisely and must not be advertised as accredited certification without evidence.

The current status is **CANDIDATE / FEASIBILITY NOT YET VERIFIED**. The absence of a confirmed route in initial public searches is not a conclusion that certification is impossible. No fee, standards purchase, application or paid tool is authorized by this policy; the initial search should prioritize official directories and written inquiries that do not create financial commitments.

Normative source references:
- ISO 704:2022 — https://www.iso.org/standard/79077.html
- ISO 1087:2019 — https://www.iso.org/standard/62330.html
- ISO information on certification — https://www.iso.org/certification.html

## 3. Terminology data model

Terminology must model concepts, not merely collect strings. For each entry distinguish:

- **Object or referent:** the thing, activity, system, property, event, service, institution or idea being discussed.
- **Concept:** the unit of knowledge the entry intends to represent.
- **Definition:** a statement that identifies the concept by its meaning and distinguishing characteristics.
- **Designation:** the name, term, acronym, symbol, code or other representation assigned to the concept.
- **Domain and context:** the field and situation in which the concept is valid.
- **Concept relationship:** a documented relation to another concept, such as broader/narrower, whole/part or related-by-association.

Do not assume a word alone establishes a single concept. One term may be ambiguous across domains; one concept may have a preferred term and permitted variants; similar wording may denote different concepts. Record and resolve these cases rather than flattening them.

## 4. Required entry fields

Every approved canonical concept entry must have, as applicable:

1. Stable concept ID that is never reused after retirement.
2. Domain/subdomain and record status.
3. Preferred designation in the source language.
4. Full form and acronym, where applicable.
5. Definition that identifies the concept's class and distinguishing characteristics where that model fits.
6. Scope note, context and explicit exclusions where ambiguity or misuse is likely.
7. Essential characteristics or criteria that distinguish the concept.
8. Concept relations, with relationship type and linked concept IDs.
9. Accepted variants, synonyms, abbreviations and forbidden/deprecated designations, each with usage notes.
10. Examples and counterexamples where they clarify the concept boundary.
11. Evidence/source record, owner/decision authority, dates created/reviewed, revision history and rationale for material changes.
12. Language/localization records and their validation status when multilingual terms exist.
13. Publication classification: internal, public or restricted; never expose secrets or private personal information through a terminology entry.

Mark fields N/A only with a reason. Use BLOCKED when necessary evidence or authority is unavailable. An entry that lacks sufficient evidence to assert its intended meaning must be CANDIDATE or BLOCKED, not silently treated as approved.

## 5. Definition and designation rules

- Define one concept per canonical entry. Avoid combining distinct concepts merely because one word is used for both.
- Use precise, concise, comprehensible, non-circular definitions. Do not define a term by repeating it or using an unexplained synonym.
- Prefer essential and distinguishing characteristics over examples, slogans, aspirations, benefits or sales claims.
- Examples illustrate definitions; they do not replace them. Counterexamples and exclusions may prevent predictable misinterpretation.
- Keep descriptive definitions separate from recommendations, legal conclusions, promises and project policy.
- State domain and context when meaning changes by technical field, governance context, public communication or jurisdiction.
- Record the preferred term and explain why alternatives are not preferred. Do not silently replace historical terminology in immutable records.
- Keep acronym expansion, punctuation, capitalization, hyphenation, plural forms and symbol usage consistent. Acronyms with multiple plausible meanings must carry a domain label or be avoided in reader-facing text.
- Do not form an acronym solely to force a brand name if doing so materially distorts the underlying concept.
- A brand name or proper name can be a canonical designation, but its existence does not prove the accuracy of factual or capability claims associated with it.
- Distinguish a project's chosen term from a scientific, technical, regulatory or legally defined term. A project-specific definition must not masquerade as universal consensus.

## 6. Concept systems and relationships

Group related concepts into a documented concept system before deciding their wording. Identify the principle used to subdivide a domain and avoid mixing incompatible classification criteria within the same hierarchy.

Use explicit typed relations:
- **Broader/narrower:** one concept belongs within the extension of another.
- **Whole/part:** a component is part of a defined whole; this is not interchangeable with broader/narrower.
- **Associative:** related concepts that are neither hierarchical nor whole/part.
- **Dependency:** a concept or capability requires another concept or condition.
- **Governance authority:** a defined role or body may make a decision only within its stated scope.
- **Historical/terminological:** a previous term, renamed concept, former acronym or replaced definition remains linked to its successor without being presented as current preferred terminology.

Relations must be justified; do not create a hierarchy merely because names sound similar. Where a diagram improves understanding, link it to the same stable concept IDs and keep it consistent with the register.

## 7. Term status and decision lifecycle

Use controlled statuses:

- **PROPOSED:** suggested but not approved.
- **CANDIDATE:** under investigation; meaning or suitability remains unsettled.
- **APPROVED:** accepted by the authorized maintainer/governance route and sufficiently evidenced for its stated scope.
- **DEPRECATED:** no longer preferred; retain it with a replacement pointer and reason.
- **RETIRED:** no longer used for new work; preserve the record and links.
- **BLOCKED:** a required input, evidence, authority or assessment is unavailable.
- **N/A:** a control genuinely does not apply; record the reason.

Lifecycle:

Problem/new concept → domain and context analysis → concept distinction → relation mapping → designation candidates → definition drafting → source/evidence review → overlap/conflict check → authorized decision → publication/localization → use monitoring → scheduled or event-triggered review.

Do not treat frequency of use, a model's confident statement, branding preference, search ranking or repetition in a draft as approval evidence. Record who authorized important project decisions and when.

## 8. Global and multilingual governance

The canonical concept and definition are the semantic source of truth. A translation must preserve the concept, scope and intended relationships, not simply mirror each source-language word. For each localized designation, record target language/locale, preferred form, usage/context restrictions, reviewer and validation status.

Where a reliable equivalent is unavailable, keep the source term with an explanation or mark the translation BLOCKED; do not fabricate a fluent-looking equivalence. Preserve distinctions among literal translation, recognized industry term, transcreation/marketing phrase, transliteration and untranslated proper name.

Do not assume that legal, financial, privacy, safety, religious, cultural or regulatory language has the same effect in every jurisdiction. Legal conclusions require appropriate jurisdiction-specific review.

## 9. Brand voice and public-use controls

The lexicon is not a substitute for a visual brand guide or complete editorial style guide; it is their semantic source of truth. Before publishing a material name or claim:
- use the approved designation and current definition;
- verify capability, availability, performance, licence, pricing, governance and legal claims separately;
- distinguish current operation from proposal, roadmap, prototype or research hypothesis;
- link to the canonical definition where useful;
- avoid presenting a project's chosen term as an external scientific or regulatory determination;
- keep public-facing summaries accessible while linking to detailed technical/governance definitions;
- record any market/language exception and its approval.

Terminology approval never independently authorizes product behavior, asset rights, token claims, external access or governance powers.

## 10. Governance and change control

- The designated human maintainer is accountable for the terminology register unless a formally approved governance charter assigns a different role.
- Any collaborator or model may propose an entry, critique or revision. No model may approve its own proposed term or silently overwrite an approved definition.
- Material changes require written rationale, impact analysis, affected concept/link list, evidence review and an explicit reviewable repository change.
- Search dependent references across affected active repositories. Update active references and public summaries where needed. Preserve historical/audit records and immutable backups.
- Do not modify anything under backup/ or Backup/ directory paths, including case variants and archived mirrors, during routine terminology updates. A historical term in an immutable record is not a defect to correct.
- Keep the current record, prior revisions, decision source, reviewer and relevant audit evidence.
- Review terminology when a product, legal context, technical capability, project decision, localization or important external evidence changes, and periodically for high-impact terms.
- Do not create a second competing canonical glossary in a dependent repository. The dependent repository may add audience-specific usage notes and cross-links, but shared concepts resolve to the canonical register.

## 11. Internal audit controls

For each audit, identify exact repository branch/commit, scope, term domains, evidence sources, sample selection, auditor, date and result. Review:

- **Concept integrity:** Does each entry represent one distinguishable concept, with suitable context and evidence?
- **Definition quality:** Is the definition clear, non-circular, appropriately scoped and distinguishable from examples, opinion or promotion?
- **Concept-system integrity:** Are broader/narrower, part/whole, associative and dependency relations correctly distinguished?
- **Designation control:** Is there one preferred designation per defined language/domain/context, with variants and prohibited/deprecated forms explained?
- **Traceability:** Can each approval and material revision be traced to a source or decision record?
- **Conflict control:** Are duplicates, contradictions, ambiguous acronyms and stale active references identified?
- **Localization:** Are translations conceptually validated, and are unresolved equivalents visible?
- **Publication control:** Do public claims match approved scope/status and avoid overstating technical, legal or scientific certainty?
- **Change control:** Is the register versioned, reviewed and protected against silent edits or accidental archival/backup changes?
- **Use in practice:** Do representative repositories, public pages and documents actually use approved terms?

Record findings with criterion, evidence, impact, remediation, owner, next-review date and re-test. A checklist alone is not conformity evidence; the auditor must inspect actual entries and usage.

Use these results:
- **PASS:** tested evidence meets the defined internal criterion.
- **FAIL:** evidence demonstrates a requirement is unmet.
- **BLOCKED:** required access, full-standard clause, evidence or authority is unavailable.
- **N/A:** criterion does not apply, with rationale.
- **CANDIDATE:** proposed control or entry has not yet been verified.

Do not average away mandatory failures. A blocked clause-level standard mapping cannot be converted to PASS through a local checklist.

## 12. Preliminary ISO 704 alignment/evidence map

This is a project-owned thematic map of published subject matter, **not a clause-by-clause reproduction or full conformity matrix**.

| Published subject area | Internal control | Evidence needed | Current result |
|---|---|---|---|
| Preparing and compiling terminology | Canonical register, lifecycle and ownership are defined | Reviewed register and change history | PARTIALLY DEFINED |
| Objects, concepts, definitions and designations | Entries separate these dimensions and identify context | Sample-entry audit and duplicate/conflict analysis | IMPLEMENTATION TO VERIFY |
| Concept relations and systems | Typed relation model and concept-system review | Relation map and review evidence | IMPLEMENTATION TO VERIFY |
| Writing definitions | Definition rules and required entry fields | Independent sampling of definitions | IMPLEMENTATION TO VERIFY |
| Formation of terms and proper names | Preferred form, variants, acronyms and decision rationale | Designation decisions and active-usage sweep | IMPLEMENTATION TO VERIFY |
| Multilingual terminology | Locale-specific equivalent records and validation | Reviewed sample in every active locale | DEFERRED UNTIL LOCALES ARE DECLARED |
| Full edition's specific provisions | Exact edition checked clause by clause | Lawfully accessible full text, requirements matrix, evidence and review | BLOCKED — FULL TEXT NOT YET IN PROJECT AUDIT BASELINE |

When authorized access to the full text becomes available, replace this preliminary map with a controlled clause-by-clause matrix identifying exact clauses, applicable criteria, evidence paths, result, finding IDs and re-test status. Do not infer clause numbers or requirements from the standard's public abstract.

## 13. Implementation stages and exit criteria

**Stage 0 — Adopt governance draft**
- Review scope, owner, status vocabulary, preservation boundary and source-of-truth model.
- Exit: reviewers agree on ownership and no false certification/conformity claim is made.

**Stage 1 — Establish the initial canonical register**
- Review current terms in bounded active paths across NOVA and AstroCrown-Web.
- Add stable IDs, definitions, statuses, cross-links and decision provenance for high-impact concepts.
- Exit: each in-scope initial term has an owner, status and usable definition; known gaps remain visible.

**Stage 2 — Repository usage and conflict audit**
- Scan active non-backup files for divergent names, duplicate meanings, legacy references and unsupported claims.
- Remediate active paths selectively through reviewable changes.
- Exit: all discovered matches are resolved or explicitly tracked; backup/archive paths remain untouched.

**Stage 3 — Public and localization controls**
- Define public-facing usage notes and localize only languages/markets actually in scope.
- Exit: each published localization has a validated term record or an explicit BLOCKED state.

**Stage 4 — Full-edition review**
- Once lawful access to ISO 704:2022 is available, conduct the clause-level comparison and independent review.
- Exit: every applicable clause has evidence and a result; mandatory gaps are closed or disclosed; conformity claims are reviewed before publication.

**Stage 5 — Ongoing audit**
- Review high-impact terms after material decisions/evidence changes and periodically thereafter.
- Exit: audit sampling, corrective action, revision history and re-test function as repeatable practices.

## 14. Impact Analysis

**IF implemented:** the ecosystem gains a controlled semantic foundation for engineering, governance, public communication, AI prompting/retrieval, localization and future audits. Conflicting terms can be corrected without silently rewriting history, and unsupported definitions/claims remain distinguishable from approved decisions.

**IF not implemented:** repositories and collaborators may keep changing names or using the same word for different concepts, making technical requirements, public claims and governance records harder to reconcile or audit.

## 15. Revision and interpretation

This is an internal project control. Where the complete ISO 704:2022 text establishes an applicable requirement that differs from or goes beyond this draft, record the gap and update the control before asserting full alignment. Do not make the document's own wording authoritative evidence of its own conformity.
