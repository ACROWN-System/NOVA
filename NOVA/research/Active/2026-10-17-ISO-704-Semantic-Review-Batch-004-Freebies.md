# ISO 704:2022 Preliminary Semantic Review — Batch 004 (Freebies Licence and Token Example)

**Review ID:** NOVA-ISO704-SEM-B004  
**Date:** 2026-10-17  
**Status:** AI-ASSISTED PRELIMINARY CONTENT REVIEW COMPLETE FOR TWO FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** `ACROWN-System/Freebies-` main snapshot dated 2026-10-17  
**Boundary:** This is a terminology/public-claim review, not a smart-contract security audit, legal opinion, or ISO clause-conformity result.

## 1. File dispositions

| Batch item | Path | Baseline blob SHA | Result |
|---|---|---|---|
| B004-01 | `LICENSE` | `ece2b4b8bdc31602fa252f5aa726849c03d909b7` | REVIEWED — MIT licence wording present; scope of licence is not by itself proof that every repository asset is covered |
| B004-02 | `SimpleToken.sol` | `a92117c650a0a8f9929ec9a8479a198d10a3c3a0` | REVIEWED — example contract terminology/public claims need qualification and separate technical verification |

## 2. Findings

### B004-F01 — “Open-source/free forever” does not follow from the MIT file alone

The MIT licence file provides a standard permission and warranty disclaimer for the defined “Software”. That text alone does not establish that every asset, dependency, trademark/brand identifier, hosted service or future resource is covered by the same licence. This supports the distinction already recorded in the Freebies README and the AstroCrown-Web README: per-file rights and third-party material must be checked separately.

**Disposition:** No licence text is changed by this terminology review. The broader README statement that resources are open-source and free forever remains a public-claim finding from B001-F02; keep its scope and evidence decision open.

### B004-F02 — “ERC-20” and “BSC ready” label an example, not demonstrated conformity

The source is titled “Minimal ERC-20 Token (BSC ready)” and includes public name/symbol/supply fields, transfer/approve/transferFrom functions and corresponding events. The contract source alone does not demonstrate full interface/behavioral compatibility testing, chain deployment, compiler/build verification, third-party dependency review or production suitability. The constructor and transfer logic are illustrative; this review does not establish that the contract is insecure, nor does it perform a security audit.

**Required action:** keep the artifact described as a minimal/tutorial example unless a separate engineering verification proves the intended standard/chain compatibility. If “ERC-20 compliant” or “BSC-ready” is used as a factual claim, attach the test/build evidence and exact scope, and distinguish a code example from a deployed/verified contract. Do not infer audit or certification status from the filename or SPDX tag.

## 3. Source-of-truth boundaries

- The `SPDX-License-Identifier: MIT` marker and the repository MIT licence are consistent at the level inspected, subject to third-party rights and file-specific notices.
- “Token”, “ERC-20”, “BSC ready”, “open-source”, “free” and “free forever” are not interchangeable labels. The latter three are publication/availability claims; the first two are technical design/interface terms.
- No specific ISO 704 clause is assessed here. The complete standard baseline remains blocked.
- No Solidity tests, static analysis, deployment tests or external audit were run as part of this terminology review.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Preliminary semantic/public-claim review of the Freebies repository's licence and single token example.
