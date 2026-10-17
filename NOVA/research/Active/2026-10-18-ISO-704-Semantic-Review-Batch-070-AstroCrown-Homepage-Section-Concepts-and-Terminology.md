# ISO 704 Semantic Review Batch 070 — AstroCrown Homepage Section Concepts and Terminology

**Document ID:** NOVA-ISO704-SEM-B070  
**Review date:** 2026-10-18  
**Baseline repository:** `ACROWN-System/AstroCrown-Web`  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Scope:** Five active homepage-section documents, retrieved at the exact baseline and compared with the live sweep tracker before review.  
**Review status:** Preliminary full-file semantic review; human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. The applicable full-text standard remains unavailable in the current evidence package; this report does not claim conformity or nonconformity to any clause.

## Review method and limits

Each complete source document was read at the pinned baseline blob SHA recorded below. The review concentrated on concept identity and boundaries, definition/designation precision, classification criteria, relation types and direction, concept-system consistency, epistemic status (candidate versus approved), and traceability from migrated excerpts to their origin. It was a static content review only. No website code, runtime behavior, design rendering, source APIs, tests, workflows, provider settings, credentials, repository settings, or backup/archive paths were changed, executed, or inspected. The migration documents mention historic backup snapshots; those snapshots were not consulted.

## Source manifest and dispositions

| # | Source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B070-01 | `development/index-section/DIRECTORY-FILTER.md` | `0b4c65cc016b5870bdc4d3f139a1b4ccea2f7088` | Preliminary review; extend source-provenance finding SWEEP-F-0038 and record candidate filter-taxonomy risk SWEEP-F-0048. |
| B070-02 | `development/index-section/DIRECTORY.md` | `9ec72d6e30ee84cbb92ad880fd93495b9e86ef35` | Preliminary review; extend SWEEP-F-0038 and SWEEP-F-0048; open SWEEP-F-0049 on “reference device/currency” and percentage-basis ambiguity. |
| B070-03 | `development/index-section/DISCOVERY-INFORMATION-BAR.md` | `1aa678d5eb29defd1017c455ab82c1743d447752` | Preliminary review; extend SWEEP-F-0038 and SWEEP-F-0044 to the active subsystem source. |
| B070-04 | `development/index-section/FOOTER.md` | `ebc4098b7044f6c623183e195e521c8deb37bf36` | Preliminary review; extend SWEEP-F-0038; no separate semantic finding opened from this file. |
| B070-05 | `development/index-section/HERO-CARDS.md` | `a0410ff66f14d645fd7d516ea7625f71b808d8ff` | Preliminary review; extend SWEEP-F-0038 and open SWEEP-F-0050 on the typed concept dimensions and relations in the candidate Influence Map. |

## File-level review notes

### B070-01 — Directory Filter

The file explicitly labels the filter taxonomy as a **current candidate taxonomy** and says that filter intelligence needs a defined timeframe, universe, methodology, and source before implementation. Those statements preserve candidate state and appropriately prevent example percentages from being mistaken for verified market facts.

The candidate list “All; AI; Gaming; Meme; RWA; DePIN; Stable” requires a clearer concept model before it can serve as a controlled taxonomy: “All” is a selection/reset operation rather than a market-category concept, while the remaining labels appear to use differing classification criteria and can plausibly overlap. That is a design-stage semantic risk, not a claim that an implemented filter is wrong. SWEEP-F-0048 records the need to decide whether these are independent facets, multi-label tags, or one controlled classification; definitions and overlap rules should reflect the intended user task rather than forcing false exclusivity.

The stated filter-to-architecture flow and reuse opportunities are useful structural context, but they do not alone define the category relation model. The preserved candidate language is a positive control.

### B070-02 — Working Market Directory

The directory repeats the candidate filter taxonomy, so SWEEP-F-0048 covers this source as well. The row-field list includes “selected reference-device/currency value”; its separate subsection again says “reference device/currency” and states that it affects displayed price and percentage interpretation consistently. “Device” is not defined as a market reference concept here, and the wording does not settle whether the intended concept is a quote currency, reference currency, reference asset, or another unit/basis. It also does not specify how a change percentage is calculated when the selected basis changes. SWEEP-F-0049 records this ambiguity without assuming which intended concept the product owner meant.

The document appropriately labels many data fields and execution integrations as candidate/undefined and explicitly says execution data must not be presented as guaranteed executable pricing unless current availability is verified. It also declares exact layout, sorting, pagination, filtering, search, provider architecture, and other implementation choices undefined. Those are useful safeguards against mistaking an early domain sketch for a completed specification.

### B070-03 — Discovery Information Bar

The requirement itself contains the candidate information-type table assessed in SWEEP-F-0044. The three examples combine different semantic dimensions: priority/severity and negative security status; positive valence and general information; and warning/governance or subject-domain labels. Since this table is in the active subsystem requirement document, not only in an extracted design-reference index, SWEEP-F-0044 is extended to this affected path.

The document consistently calls its technology, icon, content-management, animation, and geometry choices candidates and explicitly states that the baseline is not an immutable implementation specification. It also identifies accessible interaction, reduced-motion behavior, contrast, focus, and dynamic content behavior as evaluation needs. These are positive controls. The type/color/icon mapping still needs an explicit classification model before the candidate examples can become controlled labels.

### B070-04 — Footer

The footer requirement uses a broad but bounded purpose: supporting navigation, identity, legal/trust information, and applicable ecosystem links without competing with discovery and the working market area. Its examples are candidate information, and the statement “Links shall only be presented when their destination and purpose are established” is an appropriate constraint on publishing unresolved designations or destinations. No distinct concept-definition or relation finding was opened from the available text.

The section is nevertheless another migrated requirement excerpt whose source range is named by line number without an immutable originating commit/blob reference in the active file. SWEEP-F-0038 is extended for provenance traceability; this does not imply that the historical source never existed.

### B070-05 — Hero Cards

The file preserves several useful concept boundaries:
- the consensus methodology is explicitly undefined, and provider values are not to be combined merely because they are numeric;
- source observations and derived consensus are to remain distinguishable;
- “Winners & Losers” ranking is not reduced to percentage movement alone;
- the Influence Map should express observed influence rather than unverified causation;
- missing evidence is not silently represented as zero, neutral, healthy, or positive;
- candidate status is explicitly separated from approved requirements.

These are strong positive controls for terminology and evidence governance.

One open model-design risk remains in R-021.5. The candidate list called “dimensions” combines concepts at different levels and of different kinds (for example, Trend, Capital Activity, Derivatives, Whale Activity, ETF Flow, News, Regulation, Technology, Macro, and Narrative). Those could be useful independent lenses, but the document does not yet define whether each item is an evidence source, event/activity class, subject domain, market condition, actor-related signal, or explanatory theme. The example arrows (such as “News → Gaming” and “Regulation → Payments”) also do not identify the relation being asserted: association, topic mapping, evidence-to-category mapping, or a stronger influence relation. SWEEP-F-0050 records this as a candidate concept-modeling risk, without asserting that the intended relationships must be causal or that the candidate dimensions should be discarded.

The file itself already says these are candidates and requires source, lookback, weighting, confidence, minimum-evidence, conflict, and staleness rules before implementation. The recommended next step is to type the dimensions and name each intended relation explicitly, while preserving the existing non-causation safeguard. Exact score formulas and data methods remain deliberately undefined.

## Findings and traceability updates

1. **SWEEP-F-0038 — Homepage requirement source identity and extracted-reference traceability:** Extend the affected-path scope to all five section files in this batch. Each identifies an excerpt from a pre-migration source by old line range, but does not pin that source to an immutable commit/blob identity within the active file. The documents state that historic source material is preserved in backup snapshots; this review does not inspect those excluded paths or infer historical non-existence.
2. **SWEEP-F-0044 — Information-bar type taxonomy mixes classification dimensions:** Extend the affected paths to `development/index-section/DISCOVERY-INFORMATION-BAR.md`, where the candidate type table appears in the active subsystem requirement.
3. **SWEEP-F-0048 — Candidate directory filter list mixes a selection operation and market-category criteria:** New. A controlled decision is needed on facets versus tags, category definitions, overlap/multiple-membership, and whether “All” is treated as filter behavior instead of a market category.
4. **SWEEP-F-0049 — “Reference device/currency” and percentage-change basis are underdefined:** New. Define the intended reference concept/term and specify how prices and percentage changes are expressed/calculated when the selected basis changes. Do not guess the product owner's intent.
5. **SWEEP-F-0050 — Influence Map candidate dimensions and example mappings have untyped concept kinds/relations:** New. Define the kind and scope of each candidate dimension and name the relation represented by each mapping, preserving the explicit boundary between observed signals and demonstrated causation.

All findings remain open and preliminary pending designated human validation. These are concept-system and wording risks, not claims of an implementation regression. The current active-source review cannot determine historical origin content that is not pinned in the reviewed baseline.

## Batch disposition and counts

After recording the five complete preliminary reviews, the row-derived sweep target is:

- Active files inventoried: **318**
- Preliminary full-file reviews: **266**
- Partial targeted screens: **5**
- Not yet reviewed: **47**
- Human validation of preliminary reviews: **pending**
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: **proposed; human approval pending**

Arithmetic check: 266 + 5 + 47 = 318.

No source/runtime files, backup/archive paths, tests, workflows, credentials, provider calls, billing, or repository settings were changed or used. This report is not a formal ISO 704 clause assessment or conformity statement.
