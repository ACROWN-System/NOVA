# ISO 704:2022 Audit-Readiness Dossier and Evidence Register

**Document ID:** NOVA-ISO704-AR-001  
**Version:** 0.1.3  
**Date opened:** 2026-10-17  
**Status:** ACTIVE — readiness package construction; NOT READY FOR AN ISO 704 AUDIT  
**Owner:** Designated human maintainer  
**Canonical project records:** `NOVA/TERMINOLOGY-GOVERNANCE-STANDARD.md` and `NOVA/CANONICAL-TERMINOLOGY-REGISTER.md`  
**Related application:** AstroCrown-Web terminology / brand-language governance  
**Provider outreach:** DEFERRED until the evidence-package readiness gate passes  
**Paid activity:** Not authorized by this dossier  
**Backup boundary:** Any file beneath a backup/archive directory is immutable: do not create, update, rename, move or delete it, regardless of capitalization or naming (including dated system mirrors and `index-archive/`). The active path inventory excludes these locations; no backup/archive path is changed.

## 1. Purpose and decision

Build the complete project-controlled evidence package needed to assess whether the declared terminology-work scope is ready for an independent assessment against ISO 704:2022. Provider discovery and accreditation checks are deliberately sequenced after internal evidence readiness, so a future discussion can be based on an evidence-backed scope rather than promises or assumptions.

This dossier is a controlled work plan and evidence index. It is not itself proof of conformity, a completed internal audit, a certification decision, or proof that an ISO 704:2022-specific certificate is available.

### Readiness language

Until every gate in section 8 is supported by recorded evidence, use only:

> The project is constructing a controlled terminology-governance and audit-evidence package intended to support a future assessment against ISO 704:2022. Full clause-level assessment and readiness have not yet been established.

Do not say “ISO 704 certified,” “ISO 704 compliant,” “passed an ISO 704 audit,” or “ready for a successful ISO 704 audit” before the relevant evidence supports that exact statement.

## 2. Important standards boundary

The public ISO record identifies ISO 704:2022 as Edition 4, published in July 2022, and describes terminology-work principles and methods: relations among objects, concepts, definitions and designations; terminology preparation/compilation; term and proper-name formation; and definition writing. This public description is useful for scoping but is not a substitute for the complete edition. At the controlled-baseline freeze, re-check the official ISO record for status and any newer published edition or formally active revision project. A preliminary work item or proposal is not itself a replacement published edition and must not silently change the planned assessment baseline.

A lawful, controlled copy of the complete edition is required before claiming a complete clause-by-clause assessment. The project must not reproduce copyrighted standard text in its repository. The controlled matrix should capture clause identifiers, a concise project-authored paraphrase, the statement's force (for example: requirement, principle, recommendation, description or definition), applicability, internal control, objective evidence, result and finding reference.

ISO does not itself certify or issue certificates. Certification and accreditation are distinct: an accreditation body may accredit a conformity-assessment provider for a defined scope; the word “ISO” does not mean ISO approved that provider. Provider and scheme discovery is intentionally outside the current phase and must not begin until the readiness gate passes.

**Public references**
- ISO 704:2022 record and lifecycle: https://www.iso.org/standard/79077.html
- Preliminary lifecycle lead surfaced from a national standards-body project listing; verify against primary ISO project information at baseline freeze: https://dps.gov.al/en/project/show/iso%3Aproj%3A94618
- ISO 1087:2019 terminology-work vocabulary reference: https://www.iso.org/standard/62330.html
- ISO explanation of certification/accreditation: https://www.iso.org/certification.html
- Bureau of Indian Standards (BIS) Know Your Standard: https://www.bis.gov.in/know-your-standard/?lang=en (potential access lead only; specific ISO 704:2022 availability is unverified)
- BIS standards portal instructions: https://standards.bis.gov.in/website/how-to-use (potential access lead only; not proof of free access to this ISO edition)

## 3. Scope to freeze before detailed assessment

The current proposed repository coverage and baseline tree SHAs are recorded in [Scope Proposal and Repository Inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md) and its [machine-readable active-path inventory](2026-10-17-ISO-704-Active-Path-Inventory.json). These establish an initial path baseline only; human scope approval and content review remain open. The scope statement must identify:

- The organizational/project entity whose terminology work is being assessed, without implying a separate legal entity unless established.
- The repositories, projects, technical domains, governance terms, service/product material and public communication included.
- The authoritative source of shared concepts (NOVA canonical register) and the dependent AstroCrown-Web rules for public-language use.
- The terminology-work activities actually performed: concept analysis, register maintenance, definition drafting/review, designation selection, relation modelling, approval, publication, use checking, change control and corrective action.
- The languages/locales in scope. English is the initial authoring language in the current design; a human decision must state whether translation/localization is excluded from the first audit or included. Do not silently imply multilingual evidence exists.
- Explicit exclusions and rationale, including any external repositories, third-party systems, archived histories and immutable backup paths.
- The assessment period and configuration baseline (repository refs/commit SHAs, document versions, register snapshot dates).
- Roles, approval authority, auditor identity and conflict-of-interest / independence limitations.

No scope can be represented as exhaustive until the included paths, document classes, date range and exclusions have been recorded and verified.

## 4. Evidence handling rules

1. Give each evidence item a stable ID. Record title, exact path or URI, repository, branch/commit or version, owner, creation/review date, evidence type, scope, status, and the control/clause rows it supports.
2. Preserve original evidence and its context. If a record is superseded, retain a traceable version history; do not overwrite historical evidence to make a result appear cleaner.
3. Distinguish policy/design evidence from proof of actual use. A procedure proves that a rule was written; it does not prove that people followed it.
4. Distinguish a successful sample from complete coverage. A spot check is not proof that every active path was reviewed.
5. Mark a control **BLOCKED** where the applicable standard text, authority, source evidence or test is missing. Missing evidence is not PASS.
6. Mark **N/A** only with a scope-based written rationale approved by the human maintainer and, once known, compatible with the assessment criteria.
7. Keep confidential, personal, credential and secret material out of the public evidence pack. Redact only in a way that preserves audit meaning and record that redaction.
8. Record all review findings, even where inconvenient. No author or model may silently downgrade a finding or approve its own unreviewed change.
9. Keep immutable backup/archive paths excluded from all edits. If historical evidence is needed, document that the path was excluded; do not edit the artifact.
10. Store the eventual assessment copy as a dated snapshot or release/commit reference, with a manifest/hash list where practical.

## 5. Evidence register

Status meanings: **EXISTS—DRAFT** = an artifact exists but has not been accepted as evidence; **NOT STARTED** = required work not yet demonstrated; **BLOCKED** = a prerequisite prevents valid assessment; **PASS** = tested evidence meets the declared criterion; **FAIL** = evidence shows a gap; **N/A** = justified exclusion.

| Evidence ID | Evidence package component | What acceptable evidence must demonstrate | Current status | Next action |
|---|---|---|---|---|
| AR-E01 | Scope and boundaries | Approved scope statement; included domains, repos/paths, activity, languages, period, exclusions and rationale | DRAFT / NOT APPROVED | Review the [scope proposal and repository inventory](2026-10-17-ISO-704-Scope-and-Repository-Inventory.md); approve the six-repository scope, languages, assessment period and exclusions, or document changes before claiming coverage |
| AR-E02 | Controlled standard baseline and lifecycle freeze | Lawful access to the complete ISO 704:2022 edition; edition/version, source, access/licence record, controlled-copy identifier, lifecycle/revision status checked at baseline date | BLOCKED | Investigate lawful no-cost routes first (BIS standards/library services, an existing institutional/consortium library or an already licensed copy); verify exact edition and permitted use. Also check the ISO record/lifecycle for newer published editions or active revision work; these are separate checks. Routes are leads, not confirmed availability. No purchase or paid subscription without separate authorization |
| AR-E03 | Clause/topic-to-evidence matrix | Every applicable section/clause captured from the controlled edition; statement force, project interpretation, applicability, control, evidence, result, gaps and rationale | BLOCKED — template available | Use the [controlled matrix template](2026-10-17-ISO-704-Clause-Evidence-Matrix.md) only after AR-E02; no guessed or invented clause mappings |
| AR-E04 | Terminology governance procedure | Approved roles, workflow, criteria, decision gates, status lifecycle and audit controls | EXISTS—DRAFT | Review, approve and establish an effective date |
| AR-E05 | Canonical terminology register | Versioned concept entries with stable IDs, domain/context, preferred designations, definitions, characteristics, relations, variants, sources, owner, status and history where applicable | EXISTS—DRAFT | Review each entry; record unresolved fields as candidate/blocked; approve a controlled snapshot |
| AR-E06 | Concept-system maps | Project-owned concept maps with justified relationship types and links to register IDs | NOT STARTED | Create maps for included domains; validate against entries and document unresolved relations |
| AR-E07 | Definition quality review | Recorded evaluation of entry definitions for concept identity, distinguishing characteristics, clarity, scope, non-circularity, and ambiguity; findings and retests | NOT STARTED | Define review form, sample or full-population method, reviewer, and acceptance criteria |
| AR-E08 | Designation and naming decisions | Evidence for preferred terms, acronyms, variants, spelling/form, rationale, ambiguity/collision review, deprecated names and decision authority | PARTIAL / NOT VERIFIED | Build decision log and link each in-scope entry to its approval/evidence |
| AR-E09 | Source and provenance index | Sources, project decisions, supporting evidence, versions and dates traceable to entries; clear separation of project definitions and external facts | PARTIAL / NOT VERIFIED | Add source IDs and provenance to the register; assess every entry |
| AR-E10 | Governance/approval records | Who approved the scope, standard, register entries and material changes; decisions, dates, rationale and review trail | PARTIAL / NOT VERIFIED | Capture explicit approvals; draft status is not equivalent to adoption |
| AR-E11 | Active repository terminology sweep | Reproducible inventory of every included active path; search terms, path list, tooling/method, timestamp/ref, exceptions, conflicts and resolution status | PATH BASELINE CREATED; CONTENT SWEEP NOT STARTED | Use the [active-path inventory](2026-10-17-ISO-704-Active-Path-Inventory.json); classify all listed files, update the scope at the intended assessment refs, then perform and evidence the content sweep |
| AR-E12 | Actual public-use audit | Representative or full audit of pages, UI labels, README/docs, announcements, metadata/accessibility strings in declared scope against canonical terms | NOT STARTED | Freeze scope and sample; record exact paths/URLs and results |
| AR-E13 | Localization decision and evidence | Explicit language scope; for any included locale, term records, equivalence decisions, reviewer and unresolved translations | NOT STARTED | Approve English-only first-audit scope or create real locale evidence; do not imply translations were tested |
| AR-E14 | Change control and record integrity | PR/commit trails, review approvals, versioning, impact analysis, deprecation/successor handling and protected backup boundary | EXISTS—DRAFT / PARTIAL | Inspect actual history and sample completed changes; verify backup/archive paths were not changed |
| AR-E15 | Operational-use records | Dated evidence that the procedure is actually followed: new-entry workflow, change review, conflict handling, publication check and scheduled/event-triggered review | NOT STARTED | Run and document controlled pilot cycles before readiness claim |
| AR-E16 | Internal audit plan and report | Auditor, independence/conflict declaration, scope, criteria, methods, sample, objective evidence, findings, conclusion and limitations | NOT STARTED | Create after baseline and supporting records exist; author checklist alone is not an audit |
| AR-E17 | Findings and corrective-action log | Every finding, severity/rationale, owner, due date, correction/root cause, corrective action, objective closure evidence and re-test | NOT STARTED | Establish log; all nonconformities must be addressed or transparently retained as open |
| AR-E18 | Management review/readiness decision | Dated human review of scope, audit results, unresolved risks, resources, corrective actions, evidence completeness and go/no-go decision | NOT STARTED | Conduct only after internal audit and corrective-action review |
| AR-E19 | Final package manifest | Index of included artifacts, versions/commits, evidence IDs, matrix coverage, open findings, exclusions and integrity checks | NOT STARTED | Produce a reproducible final snapshot after AR-E01–AR-E18 are evaluated |
| AR-E20 | Provider outreach / scheme confirmation | Only after readiness gate: written statement of exact offering, criteria, assessment method, certificate scope and issuer; independent accreditation-scope verification where claimed | DEFERRED BY DESIGN | Do not start until all readiness gates pass; this is not required to construct the internal evidence pack |

The statuses above reflect the present documentation review, not successful audit testing. Do not convert “exists” into “pass” without review and objective evidence.

## 6. Clause/topic-to-evidence matrix — controlled schema

Use the [controlled matrix template](2026-10-17-ISO-704-Clause-Evidence-Matrix.md) to create the separate controlled matrix after AR-E02 is available. At minimum, each row must contain:

- Matrix row ID and exact section/clause identifier from the licensed edition.
- Project-authored, concise description of the point being assessed (do not reproduce copyrighted paragraphs).
- Nature/force of the statement, recorded accurately rather than treating every explanatory passage as a mandatory “shall”.
- Applicability decision, rationale, scope/domain/language affected, and approving reviewer.
- Related internal procedure/control ID.
- Evidence IDs and exact source versions, plus what the evidence demonstrates.
- Verification method: document inspection, entry review, trace, interview, observation, sample/test, or other justified method.
- Result: PASS, FAIL, BLOCKED or N/A.
- Gap/finding ID, owner, target date, corrective action, closure evidence, retest and reviewer.
- Assessor question / uncertainty that must be resolved without guessing.

**Completeness rule:** every section/clause in the full controlled edition must appear in the matrix or be accounted for through a justified documented grouping. If a clause is informational, definitional or not applicable, capture that decision; do not omit it silently. The matrix itself must not claim ISO approval.

## 7. Working method and phases

### Phase A — Freeze scope and governance

1. Complete AR-E01 with included projects, active paths, domains, activities, languages, period, sources and exclusions.
2. Confirm terminology steward, human approver, domain reviewers and who can perform an independent internal audit.
3. Approve the internal procedure and entry-record format.
4. Declare that provider discovery is held until readiness; no fees, applications or standards purchase are authorized here.

### Phase B — Establish the normative baseline

1. Obtain lawful, controlled access to the complete ISO 704:2022 text through a separately authorized route.
2. Record edition, version, source, licence/access conditions and who is permitted to consult it.
3. Build AR-E03 using the exact text and its actual structure. Do not fill unknown clauses from memory, search excerpts or guesses.
4. Keep the full standard and copied passages out of public repository unless the licence explicitly permits it.

### Phase C — Create project-controlled evidence

1. Review every canonical entry in the frozen scope for completeness, consistency and justified status.
2. Build concept maps and validate typed relations.
3. Record designation/definition decisions, their sources and approvals.
4. Sweep the declared active repository/path set and document coverage and exclusions.
5. Audit actual public use and record conflicting/legacy terms; do not edit immutable backups.
6. Operate the workflow for controlled pilot changes and keep objective records.

### Phase D — Conduct internal evaluation

1. Complete the clause/topic-to-evidence matrix.
2. Inspect objective evidence instead of merely checking that a policy exists.
3. Independently audit entries and actual use; record sampling limitations and conflicts of interest.
4. Log every finding; apply correction/root-cause/corrective action as appropriate; retest closure.
5. Record unresolved matters explicitly. A major/open blocker prevents a “ready” conclusion.

### Phase E — Management readiness decision

1. Review completeness of scope, matrix, register, repository sweep, operational records, internal audit and corrections.
2. Approve the final package manifest and freeze a reproducible evidence snapshot.
3. Record GO / NO-GO with reasons, remaining exceptions, approver and date.
4. Only after a GO decision, begin provider/scheme discovery and ask whether an appropriately accredited independent body can assess the declared scope. A successful internal readiness review does not prove a certificate exists or guarantee a successful external assessment.

## 8. Readiness gate — every condition is mandatory

The package may be labelled **INTERNAL AUDIT-READY FOR PROVIDER DISCUSSION** only when all of the following are recorded PASS:

- [ ] Scope and exclusions are approved and detailed enough to judge completeness.
- [ ] Complete ISO 704:2022 edition is lawfully available as a controlled audit baseline.
- [ ] Every clause/section has been accounted for in the controlled matrix without fabricated mappings.
- [ ] Each applicable principle/requirement/topic is mapped to implemented controls and objective evidence.
- [ ] All included register entries are reviewed and have an evidence-backed status.
- [ ] Concept relationships and designation/definition decisions are documented and reviewed.
- [ ] Active-path inventory and terminology sweep are completed with explicit coverage and exceptions.
- [ ] Actual published/public-facing usage in scope has been audited and findings are resolved or assessed against the agreed go/no-go criteria.
- [ ] Procedures have evidence of operation, not just a written policy.
- [ ] Internal audit report records method, evidence, finding severity, limitations and reviewer.
- [ ] Every finding is closed with objective retest evidence, or the human readiness decision transparently establishes why a remaining item does not block readiness; no mandatory issue is concealed.
- [ ] Human management review signs the decision and accepts the residual risk.
- [ ] Final evidence manifest identifies each artifact/version and the snapshot can be reproduced.
- [ ] Changed-path comparison confirms no backup/archive path was modified.

If any item is BLOCKED, FAIL or unverified, the overall readiness decision is NO-GO or NOT YET DETERMINED. Do not average scores to hide a mandatory gap.

## 9. Current status and immediate next steps

**Overall status: NOT READY FOR AN ISO 704 AUDIT.**

The governance standard, initial register, and AstroCrown-Web application guide are draft artifacts. The complete edition has not been established as a controlled baseline; no complete clause/evidence matrix, exhaustive active-path sweep, operational pilot record, completed internal audit, corrective-action closure package, or management readiness decision has been demonstrated.

Next actions, in sequence:

1. Freeze the practical assessment scope and language boundaries (AR-E01).
2. Review and approve the internal terminology procedure and register-entry controls.
3. Investigate lawful no-cost access via official BIS standards/library services, existing institutional/consortium access or an already licensed copy; verify the exact edition and usage rights. If no lawful no-cost route is confirmed, pause for a separate human decision. No purchase is authorized by this dossier.
4. Populate the [matrix template](2026-10-17-ISO-704-Clause-Evidence-Matrix.md) only from that controlled edition; no clause-level mapping is valid before that prerequisite.
5. Produce, inspect and test each remaining evidence item through documented changes and reviews.
6. Complete internal audit, corrective-action closure/retesting, management review and the final package manifest.
7. Keep certification-provider discovery deferred until the readiness gate is fully passed.

## 10. Impact Analysis

**IF this dossier and sequence are applied:** project readiness is measured against traceable evidence and a controlled version of the actual standard; gaps remain visible; later external discussions can be precise about scope and maturity; unsupported certification claims are prevented.

**IF this dossier and sequence are not applied:** the project could mistake policy wording for operational evidence, overlook active terminology conflicts, claim completeness based on partial public summaries, or begin provider discussions with an undefined scope and unverified readiness.

## 11. Change log

- **2026-10-17 / v0.1.0:** Initial controlled evidence register and staged readiness gate created. Provider outreach deferred until the package is internally complete. No provider availability claim is made.
- **2026-10-17 / v0.1.1:** Added a controlled clause/topic matrix template, clarified that no clause mapping may be guessed, prioritized lawful no-cost access routes, and corrected the sequential work plan. Full-standard access and all audit-readiness evidence remain open.
- **2026-10-17 / v0.1.2:** Added a standard-lifecycle freshness check so the baseline records any newer published edition or active revision work rather than assuming the 2022 edition will remain the relevant target indefinitely.
- **2026-10-17 / v0.1.3:** Added an initial inventory of six accessible repositories and 318 active file paths, with 843 backup/archive files excluded from the active path list. Scope approval and all content-level checks remain pending.
