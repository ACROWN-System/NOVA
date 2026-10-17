# Semantic Review Batch 069 — AstroCrown Geometry, Typography and Background Terminology

**Document ID:** NOVA-ISO704-SEM-B069  
**Date:** 2026-10-18  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** The four index files and the active Background section file were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Review lens:** definitions and relations for dimensional terms, source traceability of extracted requirements, visual-vs-semantic terminology, and precise distinction between scientific concepts and artistic design motifs. This is ISO 704 preparation—not a formal clause-by-clause assessment or product approval.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B069-01 | `development/index-reference/SIZING-AND-DIMENSIONS.md` | `0ae87ccdb63a57f69acf5a875efdb519f70bb81e` | Extends SWEEP-F-0038 and SWEEP-F-0043 |
| B069-02 | `development/index-reference/SPACING-AND-DISTANCES.md` | `6cb6bfc3dde5865947d153cae2ebb6faeb960b91` | Extends SWEEP-F-0038 |
| B069-03 | `development/index-reference/TYPOGRAPHY.md` | `eba1b239bfc67afa4921aae8d9b3a456969ed1e3` | Extends SWEEP-F-0038; no unique typography finding |
| B069-04 | `development/index-reference/VISUAL-DESIGN-SYSTEM.md` | `1934ad03f81ecb6ab84f4dcd4e901678e5e24246` | Extends SWEEP-F-0038 and SWEEP-F-0043 |
| B069-05 | `development/index-section/BACKGROUND.md` | `9586b5b65da73c00b54b2151c8f571b0bafbed17` | Extends SWEEP-F-0038; opens SWEEP-F-0046 and SWEEP-F-0047 |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. The files were read only and remain unchanged.

## 2. Semantic review results

### B069-01 — Sizing and dimensions reference

The index consistently states that it is a navigation aid and preserves the candidate/TBD/undefined status of source items. It retains the approximately 59 px header and 53 px initial information-bar height as approximate design targets, and preserves the principle that the hero-card dimensions should respond to information density and task value rather than arbitrary viewport percentages.

It repeats the reversed Space Blue relative-lightness condition tracked in SWEEP-F-0043. It also quotes source ranges from `HOMEPAGE-REQUIREMENTS.md` but does not identify the source commit/blob hash or extraction date. Because the source is unavailable at the reviewed baseline, those ranges cannot be verified against one immutable version.

**Disposition:** extend SWEEP-F-0038 for source provenance and cross-reference SWEEP-F-0043 for the repeated color relation; no new unique sizing finding.

### B069-02 — Spacing and distances reference

The index keeps exact spacing and dimensions as open requirement work where appropriate and distinguishes initial/approximate layout targets from undecided responsive values. It explicitly says that spacing, minimum dimensions, alpha, radii, and other values should be evaluated before the relevant implementation rather than guessed during coding. This is a useful boundary between a candidate design target and an approved fixed value.

The file cites `HOMEPAGE-REQUIREMENTS.md` by filename and line ranges without immutable source revision, and the referenced source path is absent from the reviewed baseline. This extends SWEEP-F-0038 but does not justify inferring that the source never existed historically.

**Disposition:** no unique spacing-term finding; extend SWEEP-F-0038.

### B069-03 — Typography reference

The typography index usefully keeps exact typography choices, font-family selections, font delivery mechanisms, and related header decisions explicitly undefined until candidate evaluation. It says a new mechanism should not duplicate an existing approved one unless a demonstrated advantage justifies it. It therefore does not silently promote font candidates into approved requirements.

Like the other cross-section indexes, it references source ranges from `HOMEPAGE-REQUIREMENTS.md` without a pinned origin revision or extraction date. Exact typography is intentionally unresolved rather than a defect in this review.

**Disposition:** no unique typography finding; extend SWEEP-F-0038 for source provenance.

### B069-04 — Visual design system reference

The index preserves palette semantics, the distinct roles of brand Gold and Warning Yellow, the intended three-level blue hierarchy, and the requirement that Space Blue remain TBD until hierarchy and accessibility are evaluated. It explicitly rejects selecting a value solely by name, midpoint arithmetic, or visual preference.

The intermediate Space Blue relation is nevertheless repeated with the two directions reversed (“darker than `#16345A` and lighter than `#081426`”); this is cross-reference evidence for SWEEP-F-0043, not a separate issue. The index also lacks immutable provenance for its extracted lines.

**Disposition:** extend SWEEP-F-0038 and cross-reference SWEEP-F-0043.

### B069-05 — Homepage Background / Environment section

The background document explicitly identifies itself as a migrated active subsystem document, preserves the candidate/undefined status of requirements, explains how older R-012–R-018 material is carried forward, and assigns the newly added alpha-transparency requirement the new identifier R-036 to avoid collision with the established global baseline. The R-036 section carefully distinguishes intentionally opaque foundational backgrounds from foreground assets that need genuine alpha transparency; it also describes checks for alpha preservation, compositing, edge artifacts, delivery and rights provenance. Those are positive terminology and scope controls.

Two scientific/design vocabulary choices need more precise treatment:

1. R-016 describes debris as resulting from a “historical Earth–Moon collision event.” NASA's Moon-formation overview describes several theories while noting the widely supported/leading impact-based explanation and that researchers continue to test specific formation scenarios. The current phrase may be suitable as shorthand in an art brief, but it does not mark whether the event is a design premise, an illustration of the giant-impact hypothesis, or a claim intended as literal scientific fact. A careful label such as “visual depiction inspired by the giant-impact hypothesis” would preserve the imagery while keeping the epistemic status explicit. Reference checked 2026-10-18: [NASA Science — Moon Formation](https://science.nasa.gov/moon/formation/) and [NASA Astrobiology — Earth right after it formed](https://science.nasa.gov/astrobiology/learning-resources/alp/earth-right-after-it-formed/).

2. R-018 specifies “radial Hawking radiation rays” extending from the center of a spiral nebula. NASA's glossary defines Hawking radiation in terms of radiation theorized to be emitted by black holes near their event horizons. The current background description identifies a spiral-nebula-inspired composition and a central core, but does not identify a black hole or say the term is a visual metaphor. As design language, this risks conflating a named physical concept with generic decorative rays. Reference checked 2026-10-18: [NASA Science — Universe Glossary](https://science.nasa.gov/universe/glossary/).

**Disposition:** SWEEP-F-0046 records the fact-vs-artistic-premise distinction for the impact wording; SWEEP-F-0047 records the named-physics-term ambiguity for “Hawking radiation rays.” These findings do not challenge the desired artwork or require changing the visual concept; they require clarity about the concept being named.

## 3. Findings

### SWEEP-F-0046 — Background design language presents the Moon-forming impact as an unqualified historical event

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/index-section/BACKGROUND.md`, R-016 Primitive Earth System Layer.
- **Observed issue:** The specification says debris results from “a historical Earth–Moon collision event” without stating whether the wording is an artistic premise, a representation of the leading giant-impact hypothesis, or a fact claim about the scientific formation scenario.
- **Evidence and interpretation:** NASA's public Moon-formation material describes impact-based explanations as the leading/widely supported model while noting that the specific scenario remains an active subject of scientific study. Therefore, the source's categorical phrase risks hiding the difference between a visual depiction and a proposition about scientific knowledge. The NASA material was checked on 2026-10-18: https://science.nasa.gov/moon/formation/ and https://science.nasa.gov/astrobiology/learning-resources/alp/earth-right-after-it-formed/.
- **Required action:** Mark the wording as an artistic depiction inspired by the giant-impact hypothesis, or cite and qualify the intended scientific model if the requirement is meant to make a factual assertion. Keep the visual composition and debris requirement intact unless the design owner separately changes them.
- **Closure evidence:** Human-approved wording that identifies the concept's epistemic status and a traceable scientific reference if a factual interpretation is intended.

### SWEEP-F-0047 — “Hawking radiation rays” uses a named physical concept as an undefined visual motif

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/index-section/BACKGROUND.md`, R-018 Spiral Nebula Layer.
- **Observed issue:** The spec calls radial rays from the spiral nebula's center “Hawking radiation rays” but does not identify a black-hole/event-horizon context or say that the term is only an artistic analogy.
- **Evidence and interpretation:** NASA's Universe Glossary defines Hawking radiation as a theory under which black holes emit radiation near their event horizons. A decorative ray treatment may certainly be desired, but the unqualified designation risks conflating the scientific concept with a general visual effect. Reference checked 2026-10-18: https://science.nasa.gov/universe/glossary/.
- **Required action:** The design owner should either define the intended black-hole/Hawking-radiation concept and its role in the artwork, or use a neutral art-direction term such as “radial light rays”/“radial energy-like rays” and record the stylized intent. Do not infer that the artwork depicts actual Hawking radiation solely from the current label.
- **Closure evidence:** Human-approved definition/design label distinguishing scientific concept from visual metaphor, with an identified reference if the physical term is intentionally retained.

## 4. Existing findings extended

### SWEEP-F-0038 — Homepage requirement source identity and extracted-reference traceability

Batch 069 adds the Sizing and Dimensions, Spacing and Distances, Typography, and Visual Design System indexes to the affected set. Each gives source file/line-range references to `HOMEPAGE-REQUIREMENTS.md` without an immutable source revision or extraction date. The Background subsystem is also based partly on pre-migration source excerpts identified by old line ranges; it preserves historical material and points to backup snapshots for historical consultation but does not pin the originating content to a commit/blob hash in this file. Because the requirement source is unavailable at the reviewed baseline, a reader cannot confirm every extraction/source excerpt against one unique revision. This does not prove the historical source never existed, and no excluded backup was inspected.

Human closure should pin a retrievable historical source or approved retained replacement, identify its commit/blob and date, distinguish current approved requirements from migrated historical excerpts, and verify the related extracts without reconstructing missing wording from memory.

### SWEEP-F-0043 — AstroCrown Space Blue lightness relation is reversed

Batch 069 cross-references this existing finding because both `SIZING-AND-DIMENSIONS.md` and `VISUAL-DESIGN-SYSTEM.md` repeat the reverse relative-lightness instruction: the intermediate Space Blue is described as darker than the lightest endpoint and lighter than the darkest endpoint. No duplicate finding ID is opened.

## 5. Counts, limitations and safety boundary

- Row-derived post-batch counts: **261 preliminary full-file reviews + 5 partial targeted screens + 52 not reviewed = 318 active paths**.
- Human validation remains pending for all 261 preliminary full-file reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- All five target blob SHAs match the exact recorded baseline entries.
- External scientific references were used only to disambiguate the meaning/status of terms used in the artwork specification; they do not constitute an ISO 704 clause assessment.
- No AstroCrown-Web source/runtime file, backup/archive path, workflow, test, credential, provider call, billing or repository setting was changed. No visual, browser, image-generation, or test workflow was executed.
- Scope remains proposed and not human-approved; controlled lawful access to the full applicable ISO 704 standard remains a prerequisite for formal clause mapping.