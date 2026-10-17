# Semantic Review Batch 068 — AstroCrown Design-Reference Terminology

**Document ID:** NOVA-ISO704-SEM-B068  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Review lens:** concept and designation consistency, classification-axis separation, semantic-versus-visual terms, candidate/approved status preservation, and provenance of cross-section extractions. This is ISO 704 preparation—not a clause-level assessment or an approval of the underlying homepage design.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B068-01 | `development/index-reference/ICONS-AND-INDICATORS.md` | `bea00c7a613298649805f8e33d734f826bc8c250` | SWEEP-F-0044; extends SWEEP-F-0038 |
| B068-02 | `development/index-reference/INTERACTION-CONVENTIONS.md` | `6dcd98ac8ca19f55a2171bc0ff2984537481db93` | SWEEP-F-0045; extends SWEEP-F-0038 |
| B068-03 | `development/index-reference/LAYOUT-AND-ALIGNMENT.md` | `d06850c148208a34a4d2999e1aa5a39cb3a05936` | Extends SWEEP-F-0038 |
| B068-04 | `development/index-reference/README.md` | `2cf350b722ed5a13b1093242341c8487cc3f90ee` | No unique finding; establishes intended index/reference hierarchy |
| B068-05 | `development/index-reference/RESPONSIVE-CONVENTIONS.md` | `765e0052a331a22c8c99d6c38476481f217ee70b` | Extends SWEEP-F-0038 |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. The files were read only and remain unchanged.

## 2. Semantic review results

### B068-01 — Icons and indicators

The index preserves the candidate state of icon choices and tells readers not to promote a candidate merely because it appears in the reference. It also keeps market filter intelligence conditional on a defined timeframe, universe, methodology and source, and explicitly leaves Winners & Losers ranking methodology undefined until evidence and tests exist. Those are useful safeguards against treating a symbol, number or visual style as self-defining evidence.

However, the information-bar candidate table places “High-priority negative / security”, “Positive / general information”, and “Warning / governance” in one `Candidate type` column. These labels combine different dimensions: priority/severity, sentiment valence, message domain/topic and possibly communication purpose. They are not mutually exclusive—for example, a governance item may be neutral, positive, or a high-priority warning—and “general information” does not inherently mean positive. The candidate colors and icons are still marked as candidates, so this is not evidence that a released UI currently miscommunicates; it is a taxonomy design ambiguity to resolve before promotion.

**Disposition:** SWEEP-F-0044 — information-type candidates mix classification dimensions. Define the axes first (for example topic/domain, priority/severity, polarity/valence, message/action type), then define permissible combinations and the mapping from each relevant combination to icon, color and wording.

### B068-02 — Interaction conventions

The index carefully distinguishes the required interaction result from a particular implementation mechanism for scroll handoff and scrollbar presentation. It preserves keyboard operation, focus, accessible state communication, reduced-motion considerations, and candidate status for sound effects. It also says wallet provider, integration protocol, authentication/account semantics and runtime state-management remain undefined; these boundaries are positive controls.

The wallet sentence says, “Wallet shall be an interactive H1-style header control.” The phrase `H1-style` does not clarify whether it means a visual/typographic hierarchy, an HTML level-one heading, or both. A wallet control's interactive role (for example, button or link according to actual behavior) is a different concept from a heading's document-structure role. This terminology may lead different implementers to create different semantics even when they intend the same look. The same wording is repeated in the Layout and Alignment index.

**Disposition:** SWEEP-F-0045 — visual hierarchy and semantic control role are conflated or left ambiguous in `H1-style`. The requirement owner should specify visual treatment separately from actual HTML/ARIA semantics and name the control role based on its behavior. Do not infer the absent originating requirement's exact intent from the extract.

### B068-03 — Layout and alignment

The index retains the candidate/TBD status of the palette and several dimensions, clearly states that the content structure should have an identified purpose, and preserves the rule that candidate technology listings are not implementation approval. This helps prevent a navigation index from becoming an accidental second approval layer.

The index repeats the reversed Space Blue relative-lightness language already recorded in SWEEP-F-0043 and also quotes source ranges from `HOMEPAGE-REQUIREMENTS.md` without a commit/blob identity. The content reinforces, rather than resolves, the two tracked issues: F-0043 for the color relation and F-0038 for source-revision traceability.

**Disposition:** extend SWEEP-F-0038 for provenance and cross-reference SWEEP-F-0043; no duplicate finding ID.

### B068-04 — Cross-section reference README

The README defines the files as extracted navigation aids, says they do not replace source documents, rejects a second independent approval layer, and tells maintainers to inspect the originating section and historical source when conflicts occur. It also says backup snapshots are historical consultation material, not an active requirements location.

These instructions define a sensible source-of-truth relationship. In the current reviewed baseline, however, the named `HOMEPAGE-REQUIREMENTS.md` source is unavailable, and individual indexes do not pin an exact source revision. The README alone cannot establish whether any excerpt has drifted, is stale, or was extracted accurately. This corroborates F-0038 rather than opening a separate finding.

**Disposition:** no unique finding. The source-of-truth hierarchy is a positive control, and it highlights why immutable provenance is necessary. Excluded backups were not inspected.

### B068-05 — Responsive conventions

The index preserves a desktop-first baseline while distinguishing later mobile refinement from the obligation to design for responsive behavior. It keeps exact breakpoint/contraction mechanisms and directory details undefined until evidence supports them, and retains accessibility, browser compatibility, graceful degradation and security constraints. Those are appropriate candidate-status boundaries.

Like other indexes, it quotes ranges from `HOMEPAGE-REQUIREMENTS.md` without a pinned origin revision and does not reproduce all the originating requirement definitions. Because the origin is absent from this reviewed baseline, the extracted ranges cannot be checked against one unique source version.

**Disposition:** extend SWEEP-F-0038. No separate responsive-specific terminology finding was supported by this review.

## 3. Findings

### SWEEP-F-0044 — Information-bar type taxonomy mixes classification dimensions

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/index-reference/ICONS-AND-INDICATORS.md`, R-020.3 candidate information-type table.
- **Observed issue:** The `Candidate type` values mix priority/severity (`High-priority`), sentiment valence (`negative`, `positive`), subject/security domain (`security`, `governance`), and communication class (`general information`, `warning`). These dimensions may overlap and do not form one mutually exclusive category set.
- **Interpretation:** Without separate classification axes, maintainers may assign different icons/colors or message wording to the same concept, or treat a topical label such as “governance” as inherently warning-level. Because the table is expressly a candidate list, this is a design-stage taxonomy risk, not a claim about released UI behavior.
- **Required action:** Define the intended dimensions and terms, state whether multiple labels may coexist, and specify a controlled mapping from the resulting classification to icons, colors and message wording. Preserve the candidate status until the definitions and mapping are evaluated.
- **Closure evidence:** Human-approved definitions and relation model; documented valid combinations; examples covering neutral/positive/negative and differing priorities within the same domain; and traceable mapping rules for icon/color/label choices.

### SWEEP-F-0045 — “H1-style header control” leaves visual style and semantic role ambiguous

- **Status:** OPEN — preliminary; human validation required.
- **Affected paths:** `AstroCrown-Web/development/index-reference/INTERACTION-CONVENTIONS.md` and `AstroCrown-Web/development/index-reference/LAYOUT-AND-ALIGNMENT.md`, Wallet Control section.
- **Observed issue:** The extracted requirement calls Wallet an “interactive H1-style header control” without saying whether `H1-style` refers only to visual/typographic prominence or requires level-one heading semantics. The same phrase combines a presentation style with an interactive control role.
- **Interpretation:** HTML heading hierarchy and the behavior/semantics of an interactive control are different concepts. Ambiguous wording can yield different document structure, accessibility behavior, or styling implementations. As the originating requirements file is unavailable at this baseline, its exact original intent is not inferred here.
- **Required action:** The requirement owner should specify visual appearance separately from semantic markup and control role; choose the control element according to its actual action and preserve appropriate heading hierarchy independently.
- **Closure evidence:** Human-approved wording in the authoritative requirement and synchronized indexes; explicit distinction between visual hierarchy and semantic role; implementation-independent acceptance criteria for the wallet interaction and accessible name/focus/activation.

## 4. Existing finding extended

### SWEEP-F-0038 — Homepage requirement source identity and extracted-reference traceability

Batch 068 adds `ICONS-AND-INDICATORS.md`, `INTERACTION-CONVENTIONS.md`, `LAYOUT-AND-ALIGNMENT.md`, and `RESPONSIVE-CONVENTIONS.md` as affected index files. All quote named line ranges from `HOMEPAGE-REQUIREMENTS.md`; none pins an originating commit/blob hash or extraction date. The reference README correctly says index files do not replace the source, but the source is unavailable at the reviewed baseline, so their exact source revision and drift cannot be independently determined. The absent source does not prove it never existed historically; this batch did not inspect backup/archive paths or reconstruct the source.

## 5. Counts, limitations and safety boundary

- Row-derived post-batch counts: **256 preliminary full-file reviews + 5 partial targeted screens + 57 not reviewed = 318 active paths**.
- Human validation remains pending for all 256 preliminary full-file reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- All five target blob SHAs match the exact recorded baseline entries.
- The review treated the information-type groupings and `H1-style` wording as candidate/design-language risks, not as proof of released-product defects.
- No AstroCrown-Web source/runtime file, backup/archive path, workflow, test, credential, provider call, billing or repository setting was changed. No test or workflow was run.
- Scope remains proposed and not human-approved. Controlled lawful access to the full applicable ISO 704 standard remains a prerequisite for formal clause mapping.