# Active Plan — Separate ISO 704 Conformance Work from Certification and Full-Text Access

**Date:** 2026-10-18  
**Status:** ACTIVE — strategy correction and evidence-path revision  
**Repository:** ACROWN-System/NOVA  
**Branch:** docs/terminology-governance-iso704-2026-10-17  
**Objective:** Correct the current process so it does not conflate implementing ISO 704:2022, obtaining a full controlled copy, and acquiring external certification. Preserve the $0-only constraint while allowing evidence-backed work to proceed on content directly available through identifiable public previews.

## Process and sequencing note

The initial web checks for this correction began before this task-specific plan was written. This deviation is disclosed. A search of the review-branch tree did not locate the stated `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`; prior completed plans record the same lookup limitation. This plan therefore follows the existing completed ISO 704 plan structure and explicitly records the gap rather than claiming template compliance.

## Human intent and constraints

- Primary aim: improve NOVA's terminology practices in demonstrable alignment with ISO 704:2022 where applicable.
- This is not a request to purchase a certificate or assert that ISO, a certification body, or another external party has approved NOVA.
- Maintain the approved $0-only policy. No purchase, paid subscription/membership, billable enquiry, hired adviser/provider, or other cost is authorized.
- Keep external certification-provider discovery deferred unless the human maintainer separately authorizes it.
- Do not assume an inaccessible clause is absent, inapplicable, or passed.
- Do not stop all terminology improvement just because complete text access is unresolved.
- Do not reproduce protected standard text in NOVA records. Use concise, original paraphrases with precise citations/locations and access/source notes.

## Scope

1. Separate four states in project records:
   - implementation/conformance work;
   - source-text visibility/provenance;
   - completeness of the clause/topic inventory;
   - external certification (separate and not currently pursued).
2. Review the current access report, readiness dossier, matrix template, tracker status and PR summary for language that incorrectly makes full-text access a prerequisite for all work.
3. Verify public previews from ISO or identifiable national/regional standards bodies. Record exactly which text is exposed; a full table of contents or an indexed sample is not evidence that all clauses are visible.
4. Permit provisional mappings only for exact provisions whose wording and location can be directly inspected in a traceable source. Mark these partial, source-bounded and not a complete audit.
5. Preserve the gate against declaring the complete matrix, full conformance or readiness while material clauses remain unreviewed.
6. Check the public source and current ISO catalogue for evidence of a distinct ISO 704 certification scheme; absence of evidence must be reported as such, not as proof that none can exist.

## Method

- Distinguish the *standard's subject and methods* from the commercial model for distributing a copy and from third-party certification.
- Identify primary/official sources first, then national standards-body previews and other public sources. Treat an unverified mirror as discovery evidence only; do not use it to justify a broad legality assertion or as the sole source of normative wording.
- Create a source-visibility ledger: source URL/owner, edition, visible clauses/pages, date checked, source type (official catalogue / official preview / standards-body preview / secondary sample / unverified copy), permitted-use information if published, and limits.
- Use direct evidence for partial rows; do not infer clause requirements from an abstract, search snippet, heading, or memory.
- Record clause-level paraphrases in original wording and cite exact section IDs. Keep any source text quoted from protected standards to only what is necessary and authorized; never copy the complete standard into the repository.
- Keep outcomes distinct: PARTIAL SOURCE-BOUNDED REVIEW, NOT REVIEWED, BLOCKED BY SOURCE VISIBILITY, N/A WITH RATIONALE, and COMPLETE INVENTORY. Do not label the complete assessment blocked solely because a purchase was not made.
- Maintain the human-approved $0-only policy throughout.

## Impact Analysis

**IF corrected:** NOVA can advance verifiable, source-bounded improvements without allowing a commercial access barrier to become an assumed certification condition. Unseen requirements remain visible as an evidence gap, not silently passed or ignored.

**IF not corrected:** the project may unnecessarily suspend useful work, confuse conformance with external certification, and describe a no-cost-access limitation as a total prohibition on all assessment activity.

## Exit criteria

- Access research explicitly separates implementation, text access and certification.
- At least one public preview is inspected for exact scope and visible content, with the limits correctly stated.
- Readiness and matrix language permits partial evidence mapping while keeping full-matrix completeness/readiness gated.
- Any claim concerning certification is carefully bounded by evidence and source.
- PR #124 summary reflects the corrected process and unchanged no-cost boundary.
- All writes specify the intended branch explicitly and are immediately verified by fetching the exact path on that same ref.
- Move this plan to Completed only after updated records and the PR body have been re-fetched and verified.

## Initial research notes — 2026-10-18

- ISO's official catalogue lists ISO 704:2022, Edition 4, as a published standard and describes its subject as principles and methods for terminology work: https://www.iso.org/standard/79077.html
- ISO's help page explains that the Online Browsing Platform free preview exposes selected sections rather than the full standard: https://www.iso.org/contact-iso.html
- A public GSO/SIMS preview page exposes front matter, introduction, scope, normative references, terms and definitions, and a bibliography in its indexed text; the substantive body sections are listed in the contents but are not fully present in the extracted text inspected. Therefore it is **not** treated as proof of complete-text access: https://gso-sims-preview-doc-aws.s3-eu-west-1.amazonaws.com/iso-704-2022-en.html
- Estonia's standards-body preview and other sample pages are available for further source-bounded inspection: https://www.evs.ee/en/StandardDownload/DownloadPreview?language=EnglishLanguage&productId=146425
- ISO states it does not itself provide certification/conformity assessment: https://www.iso.org/contact-iso.html
- The current search found no evidence of a dedicated third-party certification scheme for ISO 704, but this is a bounded search result, not proof that none exists.
- No paid activity was authorized or undertaken. No runtime/source, credentials, provider operation, or backup/archive path was changed.
