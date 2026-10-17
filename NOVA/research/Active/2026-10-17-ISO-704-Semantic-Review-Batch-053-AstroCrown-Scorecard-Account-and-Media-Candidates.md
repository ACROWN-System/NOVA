# Semantic Review Batch 053 — AstroCrown Scorecard, Account, and Media Candidates

**Document ID:** NOVA-ISO704-SEM-B053  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** Every target below was reviewed at its repository's recorded `main` baseline commit, not at the working PR branch.  
**Purpose:** Preliminary terminology/concept and claim-boundary review for the next five active files in the tracker. This is not a formal ISO 704 clause assessment, security audit, license opinion, or runtime qualification.

## 1. Target manifest and source identity

| Repository | Exact path | Source commit | Verified blob SHA | Result |
|---|---|---|---|---|
| AstroCrown-Web | `.github/workflows/ossf-scorecard.yml` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `b26c7cae8c9d0ce263bf04ab68b19c084c237eee` | Preliminary review; no unique finding |
| AstroCrown-Web | `development/account-continuity/ACCOUNT-CONTINUITY-AND-PRIVACY-PRESERVING-ACCESS-ROADMAP.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `79126d8941597a683941f447ee651c0c811cdb91` | Preliminary review; no unique finding |
| AstroCrown-Web | `development/ai-media-generator/CAPACITY-AWARE-ROLLOUT-PROPOSAL.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `64f973d020cad66231a76db6c4aab52eeb01bb85` | Preliminary review; no unique finding |
| AstroCrown-Web | `development/ai-media-generator/cloudflare_image.py` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `ed06fcaeff5a949602557637531c6269bdd4985a` | Preliminary review; SWEEP-F-0030 opened |
| AstroCrown-Web | `development/ai-media-generator/IMAGE-VIDEO-COMPONENT-CANDIDATE-REGISTER.md` | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | `322684f45c9cc829704a43dae0e04bad237e16ba` | Preliminary review; no unique finding |

The five fetched blob hashes match the tracker rows. The reviewed target count increases by five; no other active file is promoted by inference.

## 2. Semantic review results

### B053-01 — OpenSSF Scorecard workflow

The workflow is explicitly named for OpenSSF Scorecard, runs on pushes to `main` and a weekly schedule, limits the top-level token to repository contents read, grants `security-events: write` only to the analysis job, pins each action to a commit SHA, disables persisted checkout credentials, stores results in SARIF, and uploads the SARIF to GitHub code scanning. The action's `publish_results: false` is distinct from the explicit SARIF upload: the former disables Scorecard's own publication/badge pathway, whereas the latter submits the scan file to GitHub code scanning. The current official action documentation distinguishes those mechanisms ([official Scorecard action README](https://github.com/ossf/scorecard-action/blob/2d1146689b8cda280b9bc96326124645441f03bc/README.md)).

**Terminology result:** the trigger, permissions and upload steps describe configured workflow behavior; they do not prove the workflow has run successfully, the resulting findings are clean, or the repository has no vulnerabilities. No such result is claimed by this source.  
**Disposition:** no unique finding. Workflow execution was not triggered.

### B053-02 — Account continuity and privacy-preserving access roadmap

The document labels itself a development-only proposal and explicitly says no capability in it is `IMPLEMENTED / VERIFIED`. It distinguishes person/member eligibility, account or pseudonym, authenticator, recovery capability, resource node, benefit entitlement, payout destination and legal eligibility. It also separates authentication from unique-person eligibility and benefit entitlement; treats optional local biometrics as a way to unlock an authenticator rather than a mandatory remote identity test; and rejects IP address, device count, wallet count or account count as a standalone identity proxy.

Passkeys, privacy-preserving credentials, programme-scoped duplicate-claim controls, recovery-share arrangements, personal-memory boundaries and compute contribution remain candidate/proposed architecture. The 3-of-5 recovery arrangement is expressly illustrative, and the text acknowledges both recovery limits and metadata/linkability risks. It gives a staged requirements/threat-model, prototype, acceptance-test and promotion sequence instead of presenting a design as an operational system.

**Terminology result:** key neighbouring concepts are separated rather than collapsed into the single labels “identity”, “authentication” or “account”; implementation, provider and legal choices remain explicitly open.  
**Disposition:** no unique finding. Requirements, threat modelling, implementation, legal review and testing have not been performed by this document review.

### B053-03 — Capacity-aware media rollout proposal

The document is labelled `PROPOSAL / CANDIDATE`, not an implementation approval. It separates a feature-access waiting list (who may use a feature) from a generation-job queue (the lifecycle of an accepted request). It also distinguishes projected/qualified capacity, observed runnable capacity, completed-job usage, quota, measured latency, quality, cost and public availability. Proposed job states are expressly provisional; admission is not described as guaranteed immediate execution; and image acceptance does not confer a video PASS.

The proposal requires exact component/model/provider rights, end-to-end result retrieval, queue and failure behavior, measurable capacity, privacy and user communication to pass before public rollout. Its $0/no-payment-method constraint is preserved and paid fallback is not silently enabled.

**Terminology result:** “capacity”, “access”, “job”, “qualified”, and “available” are given separate operational meanings; the text avoids treating a wait-list position, a configured credential or a successful prototype as production readiness.  
**Disposition:** no unique finding. The proposal creates no public waiting list, job queue or runtime feature by itself.

### B053-04 — Cloudflare image adapter

The source is a bounded single-model development adapter. It validates the configured account ID and token input, constrains prompt and output parameters, rejects redirects, caps response size, inspects image signatures/structure and dimensions, records provider MIME mismatch, writes a checksum/provenance sidecar, refuses overwrites, and leaves commercial use and alpha transparency explicitly unqualified. It does not claim to perform a live generation here, and no provider request was made during this review.

A provenance-contract inconsistency remains: the `request_image` docstring says its result contains a request ID (line 375), but `_extract_image` always returns `None` in the request-ID tuple position (line 361); `write_artifact` then serializes that value as `provider_request_id` (line 480). Consequently, this path cannot currently preserve a provider request ID and its sidecar will report null even if the response were to offer a usable identifier.

**Disposition:** open preliminary finding SWEEP-F-0030. This review does not establish whether the provider exposes a stable request identifier in this exact endpoint/version.

### B053-05 — Image/video component candidate register

The register identifies itself as active research and says no complete workflow or backend is approved. It separates model weights, runtimes, adapters, hosted endpoints, video, workflow engines, commercial terms, compute eligibility, output-quality checks and true-alpha verification. Candidate statuses remain `BLOCKED` or `CANDIDATE, NOT APPROVED`; the observed Cloudflare SDXL-Lightning background samples are correctly described as technically handled but visually failing the named background acceptance criteria. It distinguishes image-request execution success from visual acceptance, usage-meter evidence, no-payment eligibility, output rights and transparent-layer suitability. Its later result section records the 512×288 experiment and the current next step is a no-provider-call procedural baseline rather than a near-identical repeat.

**Terminology result:** status and evidence categories remain mostly well-separated; a candidate's license, technical path or apparent “open” status is not treated as blanket permission or a qualified runnable route.  
**Disposition:** no unique finding. Upstream terms, current account state, hardware eligibility and output rights were not independently requalified in this file review.

## 3. New finding

### SWEEP-F-0030 — Cloudflare image provenance contract promises a request ID but always returns null

- **Status:** OPEN — preliminary, human validation required.
- **Affected path:** `development/ai-media-generator/cloudflare_image.py`.
- **Observed evidence:** `request_image` describes its return tuple as image bytes, request ID and declared MIME (line 375); `_extract_image` returns `(response_body, None, content_type)` (line 361); `write_artifact` writes the supplied value to `provider_request_id` (line 480).
- **Interpretation:** the interface and provenance field imply request-level traceability, but the implementation hardcodes the identifier to `None`. A generated artifact therefore cannot be correlated to a provider request through this field, weakening reproduction and troubleshooting evidence.
- **Required action:** inspect the exact supported endpoint response contract; if it exposes a request identifier, capture and propagate it safely. If no identifier is exposed, name/status the field as unavailable (for example, `NOT_EXPOSED`) rather than returning a claimed request ID. Add offline tests for present, absent and malformed identifier metadata without making live provider calls.
- **Closure evidence:** source-contract alignment, offline positive/negative tests, example metadata showing the actual state, and human review of any claim that the identifier is stable or provider-issued.
- **Safety boundary:** no API request, secret access, credential change or provider qualification was performed in this review.

## 4. Cross-file disposition and limits

- Four files were reviewed with no unique new finding; one implementation file produced SWEEP-F-0030.
- The workflow and documents were read at the repository's recorded baseline commit. No files under backup/archive paths were inspected or modified.
- No test suite, workflow, Scorecard run, security scan, image generation request, benchmark, deployment or external account-setting inspection was performed.
- This review is preliminary AI-assisted semantic screening; designated human validation remains pending.
- Formal ISO 704 clause-level assessments completed by this batch: **0**.
