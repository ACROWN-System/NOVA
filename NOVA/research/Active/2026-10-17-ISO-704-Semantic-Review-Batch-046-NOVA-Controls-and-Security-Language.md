# ISO 704:2022 Semantic Review — Batch 046 (NOVA Repository Controls and Security Language)

**Review ID:** NOVA-ISO704-SEM-B046  
**Date:** 2026-10-17  
**Status:** PRELIMINARY FULL-FILE CONTENT REVIEW — human validation required  
**Scope:** Five files from the NOVA repository's active-path inventory  
**Baseline:** `main` commit `2a1f5c496474aa099703432e99b3d3dfddfd3fd7`  
**Boundary:** Full-file source/content review only. No workflow was executed, no settings were changed, and no security or ISO clause assessment was performed.

## 1. Method and evidence

Each selected path was fetched at the exact inventory baseline commit. The returned blob SHA was checked against the active-path sweep tracker's recorded SHA. This review evaluates terminology, definitions, public/security claims, traceability and whether a reader could infer more assurance than the source evidence establishes.

External technical claims were checked against these primary technical references:

- MDN `Referrer-Policy`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy
- MDN `Strict-Transport-Security`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security
- MDN `Content-Security-Policy`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy
- GitHub protected branches and required checks: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Git `.gitignore` semantics: https://git-scm.com/docs/gitignore

This is still an AI-assisted preliminary review. A designated human reviewer must validate each observation and decide scope/applicability before the record is used as audit evidence.

## 2. File-by-file records

### B046-01 — `_headers`

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/_headers
- **Blob SHA:** `097939eb42fb487acc31b29d5202730621a61b74`
- **Preliminary result:** REVIEWED — security-policy comments overstate or blur control scope.
- **Finding:** SWEEP-F-0017.
- **Observed wording:** comments describe `Referrer-Policy: no-referrer` as preventing all URL-history leakage to external sites or ISPs; describe HSTS as forcing “strict end-to-end HTTPS encryption”; and describe the CSP as blocking unauthorized scripts/tracking pixels while the policy explicitly permits `'unsafe-inline'` for scripts and styles and broad HTTPS sources for several resource types.
- **Assessment:** These controls have narrower, distinct effects. `no-referrer` suppresses the HTTP Referer information sent with requests; it is not a universal guarantee against URL/metadata visibility to network providers. HSTS instructs a browser to use HTTPS for future access to the host under the configured policy; it is not a general end-to-end encryption mechanism. CSP can restrict resource loading, but permitting `'unsafe-inline'` materially weakens the protection that a script/style CSP can otherwise provide. The file's `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` are the relevant frame restrictions; the separate `X-Frame-Ancestors` line should not be presented as an established standard header.
- **Risk:** Comments can communicate absolute privacy/security guarantees not established by the configuration. In an audit, the actual deployed response headers and site/runtime behavior are separate evidence and have not been tested here.
- **Required action:** Rewrite comments to name the control and its bounded purpose without absolute guarantees. If policy-strength changes are proposed, route them through a separate security review with compatibility tests and explicit authorization; this content sweep does not change header values.
- **Closure evidence:** reviewed wording change; official documentation linked from the record; if runtime/security effectiveness is claimed, capture response headers and test them at the assessed deployment and commit/revision.

### B046-02 — `.github/pull_request_template.md`

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/.github/pull_request_template.md
- **Blob SHA:** `312460bbdc6bbee0b59f45416c8916043daa1f44`
- **Preliminary result:** REVIEWED — positive evidence-discipline control; no unique finding from this file alone.
- **Evidence ID:** `NOVA-ISO704-SEM-B046:B046-02`
- **Observation:** The template asks contributors to identify the exact external API/model contract, cite official source URLs and check dates, distinguish unsupported capabilities as BLOCKED, separate mock/static/unit/contract/live/promotion results, document failures and unknowns, and avoid treating a checklist as a substitute for review. It also asks for exact commit/test evidence and Impact Analysis.
- **Cross-reference validation:** The template's links to AstroCrown's Development & Audit Convention and NOVA's Root-Cause Prevention and Shared-Knowledge Governance document resolve on the assessed main branches. The linked NOVA document explicitly labels universal enforcement as proposed/not yet enforced.
- **Boundary:** This is a template and design control; the existence of a checklist does not demonstrate that contributors complete it, that all PRs use it, or that branch protection requires specific checks. The latter is tracked separately under SWEEP-F-0019.
- **Required action:** Retain the evidence distinctions; during operational audit, sample actual PRs to demonstrate use of the template and verify any claimed required-check settings independently.

### B046-03 — `.github/workflows/nova_cloudflare_smoke_test.yml`

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/.github/workflows/nova_cloudflare_smoke_test.yml
- **Blob SHA:** `c9e3dbf5509cd4dcbebee39a4bf97382e07cb4f1`
- **Preliminary result:** REVIEWED — external-contract evidence and local response-assertion gap.
- **Finding:** SWEEP-F-0018.
- **Observed wording/behavior:** The workflow comments state that the exact model and schema are documented by Cloudflare's JSON Mode supported-model list. The file does not itself retain the official documentation URL and date checked. The workflow requests a `json_schema` response format and, after parsing the content as JSON, checks that `nova_health` and `ack` have expected values; it does not locally reject additional object keys or record a full schema-validation result.
- **Assessment:** A one-request smoke-test result can support only the tested configuration and observed response at that run. The label `RESPONSE_CONTRACT=PASS` risks being read as complete validation of the requested schema even though the local assertions cover only two values. An inline comment is not a durable source record for current provider/model support.
- **Risk:** Test labels may overstate external compatibility or response-shape validation, making a single smoke test look like broader capability or readiness evidence.
- **Required action:** Add a dated official source link or a traceable linked audit record for the exact model, endpoint and response-format capability. Either validate the complete expected shape locally (including type, required keys, and whether extra keys are permitted) or narrow the result label to the specific assertions actually performed. Keep static/source-level review, a live HTTP response, schema validity and provider qualification as separate results.
- **Closure evidence:** a separate reviewed code/test change, documented official source and check date, targeted tests including wrong-type/missing/extra-key responses as appropriate, and an output showing what each PASS label actually validates. No workflow was run in this batch.

### B046-04 — `.github/workflows/nova_health_tests.yml`

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/.github/workflows/nova_health_tests.yml
- **Blob SHA:** `2f2fbfed66e4de0b719c000fd888cc874e3ab46c`
- **Preliminary result:** REVIEWED — CI execution and merge-enforcement claims need separation.
- **Finding:** SWEEP-F-0019.
- **Observed wording:** A workflow comment says the PR trigger makes this a “reliable required check.”
- **Assessment:** The YAML shows that the workflow is configured to run on pull requests and selected pushes. It does not establish that repository branch protection/rulesets require the check before merging. GitHub documents required status checks as a distinct protected-branch setting. An attempt to inspect the live branch-protection endpoint was not available through this connection, so the current setting is **UNKNOWN/BLOCKED**, not verified enabled or disabled.
- **Risk:** Readers may mistake “workflow runs on PRs” for “merge is technically prevented unless this check passes.”
- **Required action:** Change the comment to say that the workflow runs on pull requests and is intended to be required; state that enforcement must be verified in repository rules/settings. Record a separate settings-verification evidence item with date, branch/rule scope, required check name and applicable bypass rules before claiming enforcement.
- **Closure evidence:** reviewed wording and a separate authorized, dated readout of actual main-branch protection/ruleset configuration. No settings were changed in this batch.

### B046-05 — `.gitignore`

- **Exact source:** https://github.com/ACROWN-System/NOVA/blob/2a1f5c496474aa099703432e99b3d3dfddfd3fd7/.gitignore
- **Blob SHA:** `0c1b62a34f37505ae731e2a1f563d7f9da9b4013`
- **Preliminary result:** REVIEWED — descriptive labels overstate what ignore patterns enforce.
- **Finding:** SWEEP-F-0020.
- **Observed wording:** section headings include “Security & Secret Shield” and “Operating System & Metadata Scrubbing (Anti-Fingerprinting).” The actual rules cover a defined set of names/extensions, environment files, some secret-related locations, OS metadata and logs.
- **Assessment:** Git's own documentation says `.gitignore` applies to intentionally untracked files; files already tracked are not affected, and ignore patterns are not a complete repository secret-scanning or metadata-removal system. The current list is a useful contribution to hygiene, but cannot guarantee secret prevention, complete fingerprint removal, or that sensitive files never enter a commit.
- **Risk:** Strong headings can be mistaken for an enforced security boundary. Patterns may be incomplete, overridden or bypassed; existing tracked files need separate handling.
- **Required action:** Rename headings to describe the actual function (for example, common local-secret/build/OS-file ignore patterns) or add an explicit limitation beside them. Keep actual secret scanning, tracked-file checks, least-privilege credentials and history remediation as separate controls.
- **Closure evidence:** reviewed wording; a documented secret-handling policy and independently tested secret-scanning controls if the project makes stronger claims. No secret files or credential contents were inspected in this review.

## 3. Findings opened

### SWEEP-F-0017 — Security-control descriptions overstate effective header protections
- **Severity for readiness:** Material claim-accuracy finding.
- **Status:** OPEN.
- **Scope:** NOVA `_headers` source comments.
- **Closure:** precise control descriptions plus deployment-level evidence for any claims of actual runtime effectiveness.

### SWEEP-F-0018 — Cloudflare smoke-test result and model/schema source are insufficiently bounded
- **Severity for readiness:** Evidence traceability and test-claim scope.
- **Status:** OPEN.
- **Scope:** Cloudflare Workers AI smoke-test workflow.
- **Closure:** dated official source record for exact model/request combination and response assertions aligned with the precise meaning of each PASS label.

### SWEEP-F-0019 — Workflow trigger is described as a required merge check without verified ruleset evidence
- **Severity for readiness:** Governance-enforcement claim.
- **Status:** OPEN / ACTUAL SETTINGS UNKNOWN.
- **Scope:** NOVA health-test workflow comment and main-branch merge controls.
- **Closure:** corrected wording plus separately verified dated branch protection/ruleset evidence.

### SWEEP-F-0020 — `.gitignore` headings imply broader secret/privacy protection than ignore patterns provide
- **Severity for readiness:** Control-description and evidence-boundary finding.
- **Status:** OPEN.
- **Scope:** NOVA `.gitignore` comments.
- **Closure:** scoped wording and separate evidence for any claimed secret-detection or history-remediation control.

## 4. Counts and limitations

- Five active files received preliminary full-file reviews against the exact inventoried main-branch blob SHAs.
- Counts after Batch 046: **146 preliminary full-file reviews + 5 partial targeted screens + 167 not reviewed = 318 active paths**.
- Human validation remains pending for all 146 preliminary reviews.
- Formal ISO 704 clause-level assessments completed: **0**.
- The review does not establish runtime behavior, provider support, live security headers, branch protection settings or certification readiness.
- No source/runtime file, workflow, secret, repository setting or credential was changed.
- No backup/archive path was changed.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Preliminary five-file review of NOVA repository controls; recorded SWEEP-F-0017 through SWEEP-F-0020; no implementation changes made.
