# Semantic Review Batch 078 — AstroCrown Evidence Sources, Snapshots, Changelog and Schema

**Document ID:** NOVA-ISO704-SEM-B078  
**Review date:** 2026-10-18  
**Baseline repository:** ACROWN-System/AstroCrown-Web  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Review status:** Preliminary full-file semantic review; designated human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report makes no conformity or nonconformity claim.

## Method and limits

Five active documents were fetched from the pinned baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`; every returned blob SHA matched its tracker record. The external source index was examined for the distinction between source discovery, claim-level provenance and currentness. A small number of official current links were checked as spot checks only, not as a full link-by-link audit. No source snapshot contents, runtime code, tests, workflows, credentials, provider calls, billing, repository settings or immutable backup/archive contents were executed, changed or inspected.

## Source manifest and dispositions

| ID | Exact source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B078-01 | `development/verification/evidence/README.md` | `7605cbbc73a9008620c11b2cd27a773f6e65d389` | Positive control for evidence-layer roles; cross-reference SWEEP-F-0060 for provenance granularity. |
| B078-02 | `development/verification/evidence/snapshots/README.md` | `c22cf38def0b63b54c9caca5f6f31b5ca4a987dd` | Positive control for dated, non-overwritten snapshots. |
| B078-03 | `development/verification/evidence/sources/EXTERNAL-SOURCE-INDEX-2026-10-02.md` | `2689196106a101b0428e032f534a24a262345ecd` | Opens SWEEP-F-0060 — source discovery index is not yet sufficient as item-level claim provenance. |
| B078-04 | `development/verification/operations/CHANGELOG.md` | `9bb7c407a076f113ef34cc63655713c7ad7e4195` | Positive control for dated history and append-not-overwrite intention; no unique finding. |
| B078-05 | `development/verification/operations/SCHEMA.md` | `6668f112eb8f1888a65c0ba020c3c673ee482b87` | Opens SWEEP-F-0061 — field inventory is not, by itself, a complete normative data schema. |

## Semantic review results

### B078-01 — Verification Evidence README

The README identifies three different kinds of evidence artifact: sources, snapshots and extracts. It says evidence should be referenced instead of unnecessarily duplicated and that preserved artifacts should retain acquisition date and source identity where material. This helps separate a source, an immutable historical capture and a derivative extract.

The phrase “where material” leaves an applicability judgment, which should be made explicit when the layer is operationalized. The document is a short layer guide, however, and does not itself claim to define all fields for each evidence record. Its concept boundaries are useful. No unique finding was opened for this README alone.

### B078-02 — Evidence Snapshots README

The snapshots guide defines the intended items as dated external-source captures needed for historical preservation. It explicitly prohibits overwriting a historical snapshot when the source changes and instructs that a new dated artifact be created with provenance linked. This protects temporal distinctions between a source as it existed at one point and a later version of that source.

The file is a brief storage rule, not a complete snapshot metadata specification. It does not define checksums, capture format, source revision or all possible provenance fields; those may be specified in a related record policy. No snapshot contents were inspected and no unique finding was opened.

### B078-03 — External Source Index (2026-10-02)

The file groups references by useful domains: standards/security, web quality, security providers/programs, regulation, market/data, exchange/listing, and research/governance/security evidence. The dated index is useful as a discovery catalogue and the list includes recognizable source owners and several version-specific references—for example NIST SP 800-218 SSDF v1.1 and WCAG 2.2.

Entries nevertheless vary considerably in granularity. Some identify a named/versioned publication or methodology page, while others point only to a general institutional or company homepage. The single index date does not establish that each individual destination was checked on that date, remains current, or supports any particular assertion in a later assessment. Entries do not provide a claim/requirement relationship, relevant section, exact publication/version or effective date where applicable, source type/authority level, individual last-checked date, known scope/limitations or refresh trigger.

This is not evidence that the cited sources are false or that every discovery-index row must carry every possible metadata field. The conceptual issue is the unresolved boundary between (a) a source-discovery index and (b) a provenance record used to support a specific claim or decision. The parent evidence README refers to source index and provenance records, but this index does not identify itself as discovery-only or define when a richer source record becomes mandatory.

A sample spot check confirmed the External Source Index's White House Executive Order URL resolves to the official Executive Order 14434 page, dated September 29, 2026. The order's Section 2 concerns executive-branch terminology use subject to law; Section 3 maps terminology for purposes of the Order to existing 15 U.S.C. § 9401(3) and requests proposed legislative language. The official code page contains the referenced statutory definition. Sources checked on 2026-10-18:
- White House, Executive Order 14434: https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/
- U.S. Code, 15 U.S.C. § 9401: https://uscode.house.gov/us/usc/119-118/t15/s9401/

These spot checks validate only those links and claims; they do not demonstrate that every index entry or every linked source was audited.

**Disposition:** open preliminary SWEEP-F-0060.

### B078-04 — Verification Intelligence Changelog

The changelog provides a dated entry for the initial ecosystem-preservation work, identifies the broad verification-intelligence layers created, records that repository governance required branch/PR preparation rather than writing directly to main, and instructs that future refreshes append evidence instead of overwriting historical records. These are useful chronological and preservation controls.

The entry is a narrative summary rather than a complete per-artifact provenance log. Commit- and changed-path-level history should be sourced from Git, while evidence records should identify the external source versions they support. Given the brief descriptive purpose and available version-control history, no unique terminology finding was opened.

### B078-05 — Verification Entity Schema

The file identifies a broad field set for a structured verification entity. It distinguishes evidence-related fields (such as source_records, evidence_required, evidence_state, last_verified and next_review), operational/context fields (such as status, necessity_status, opportunity_readiness and blocking_requirements), and impact/replication fields (such as nova_replicability, replication_equivalence, visibility, credibility_impact, trust_impact and operability_impact). The breadth indicates that the proposed record is intended to connect entity identity, methodology, evidence, lifecycle and decisions.

However, despite the title “Verification Entity Schema,” the file supplies only a list of field names. It does not define the semantics, data types, cardinalities, required/optional status, permitted values, relationship rules, null/unknown/N/A handling, date formats, or validation constraints for the fields. Similar or potentially overlapping concepts, including `status` and `evidence_state`, need typed definitions so a record consumer cannot conflate evidence confidence with operational progress. Some of those dimensions may be defined in related documents; this review does not presume their absence from the whole repository. The reviewed file alone is not a self-contained validation schema.

The required resolution depends on intent: if this file is only a conceptual field inventory, say so explicitly and link to the normative schema; if it is intended to be the normative schema, define the structural and semantic constraints and the relationship to controlled status vocabularies.

**Disposition:** open preliminary SWEEP-F-0061.

## Findings and traceability

### SWEEP-F-0060 — External Source Index does not distinguish discovery links from claim-level provenance

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/verification/evidence/sources/EXTERNAL-SOURCE-INDEX-2026-10-02.md`.
- **Observed issue:** Entries mix version-specific publications, methodology pages, service/program pages and broad homepages, and generally include only a label and URL. The index-level date does not establish per-entry last verification, current version, relevant section, claim relationship, authority/source type, scope/limitation or refresh trigger.
- **Interpretation:** A discovery index can help locate potentially relevant material but is not automatically evidence that a specific claim is supported by a particular source version. Without an explicit distinction, a source’s presence in the index may be over-interpreted as claim validation or currentness.
- **Required action:** Define the index as discovery-only or enrich it with explicit source-record identifiers. For each consequential claim, connect to an appropriate provenance record containing applicable fields such as issuing organization, source title/type, exact URL/section, publication/version/effective date, actual access/check date, relevant claim/requirement, scope/limitations, evidence status and refresh trigger. Mark unavailable or unchecked attributes as unknown rather than inferred. Do not assume every field applies to every source.
- **Closure evidence:** Human-approved discovery-index/provenance distinction; a representative sample tracing claim → source record → specific source passage/version; explicit dates and state meanings; and a full URL/source validation if required by the evidence policy. The small spot check in this batch is not sufficient for whole-index closure.

### SWEEP-F-0061 — Verification Entity Schema is a field list without normative structural and semantic constraints

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/verification/operations/SCHEMA.md`.
- **Observed issue:** The document is titled a schema and calls its contents a “Minimum structured record,” but provides field names only. It defines no data types, cardinality, required/optional rules, allowed-value binding, relation constraints or validation rules.
- **Interpretation:** The field inventory indicates the concepts intended to be recorded but does not establish an interoperable or machine-validatable record structure. Distinctions among fields such as `status` and `evidence_state` can be lost unless their definitions and value domains are explicit.
- **Required action:** Clarify whether the document is a conceptual field inventory or normative schema. If it is an inventory, label it non-normative and link to the authoritative schema and field definitions. If normative, provide a versioned structural definition with field type, meaning, cardinality, requiredness, allowed values or external enum link, null/unknown/N/A behavior, cross-field constraints and examples.
- **Closure evidence:** Human-approved schema role/version; an authoritative field-definition set; valid and invalid example records; validation results covering missing, malformed, unknown and conflicting values; and alignment with the approved status/evidence enum and lifecycle rules.

## Batch disposition and counts

- Active paths in proposed scope: **318**
- Preliminary full-file reviews after Batch 078: **306**
- Partial targeted screens: **5**
- Not yet reviewed: **7**
- Human validation of preliminary reviews: pending
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: proposed; human approval pending

Arithmetic: 306 + 5 + 7 = 318.

This is a preliminary semantic review, not a formal ISO 704 clause assessment, conformity statement or certification claim.
