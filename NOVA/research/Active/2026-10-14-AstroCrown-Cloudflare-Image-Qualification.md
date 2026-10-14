# Active Navigation Plan — NOVA-Owned AstroCrown Cloudflare Image Qualification

**Date:** 2026-10-14  
**Status:** ACTIVE — establish the first live image test without duplicating credentials  
**Objective:** Execute AstroCrown-Web's existing Cloudflare image adapter from NOVA, where the existing Cloudflare credentials already reside, and preserve the generated PNG and provenance as a bounded workflow artifact.

## Navigation and source of truth

**Credential-owning repository:** https://github.com/ACROWN-System/NOVA  
**Adapter repository:** https://github.com/ACROWN-System/AstroCrown-Web  
**NOVA base commit:** `713741ae8f3c2f1d99780d89e13dfde0d2bd9ac6`  
**AstroCrown adapter source commit:** `d211dc5460941d60b9f1729791079cb9974d554a`  
**NOVA branch:** `work/astrocrown-cloudflare-image-runner-2026-10-14`  
**Mode:** Additive, manually triggered, read-only source checkout, no secret changes, no generation until a human manually dispatches the workflow on `main` with explicit confirmation.

The inspected current repository trees do not contain `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This record follows the existing AstroCrown-Web active image MVP plan and development/audit convention as the available fallback; it does not claim to have followed missing files.

## Decision

GitHub repository Actions secrets are scoped to workflows in their owning repository. Renaming the expected environment variable in AstroCrown-Web would not grant that workflow access to secrets stored only in NOVA. To avoid another token and avoid copying a credential between repositories, the image qualification workflow must run in NOVA and use NOVA's existing repository secrets.

The workflow maps:
- `secrets.CLOUDFLARE_API_KEY_01` to the adapter's process environment variable `ASTROCROWN_CLOUDFLARE_AI_TOKEN`;
- `secrets.CLOUDFLARE_ACCOUNT_ID` to `CLOUDFLARE_ACCOUNT_ID`.

The existing NOVA secrets and the adapter's stable internal variable contract remain unchanged.

## Scope

1. Add a new NOVA workflow that can only contact Cloudflare after explicit manual dispatch from `main` and a required no-payment confirmation.
2. Check out AstroCrown-Web at a reviewed immutable adapter commit SHA, not a floating branch, and invoke `development/ai-media-generator/cloudflare_image.py`.
3. Restrict workflow permissions to the minimum required: repository contents read-only; no issue writes, repository writes, or credential changes.
4. Validate PNG or JPEG container structure and requested dimensions, then upload only the detected-format image and its matching provenance sidecar as a short-retention artifact.
5. Retire the duplicate direct-live workflow from AstroCrown-Web. Keep AstroCrown-Web's offline tests and code adapter; do not add its own token or account ID secrets.
6. Keep all existing NOVA LLM/GPU health workflows, credential names, provider states, billing configuration, and operational-state writers unchanged.

## External API contract

- Endpoint: Cloudflare Workers AI REST API, `POST https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/bytedance/stable-diffusion-xl-lightning`.
- Auth: bearer token supplied only as a process environment variable on the NOVA runner. Never print it, pass it in command-line arguments, or write it to the artifact.
- Output contract uncertainty: Cloudflare's model schema specifies PNG, while its usage example uses `image/jpg`; a public provider documentation issue also reports JPEG from REST despite the schema. The failed live run logged `Provider output is not a valid PNG image` after accepting an `image/png` response header, but the response bytes were not preserved, so the returned format is unconfirmed. The remediated adapter detects actual PNG/JPEG bytes, validates container structure and dimensions, records declared versus detected MIME, and chooses a truthful filename extension. Unknown/JSON/HTML bodies fail closed.
- An offline-test pass is not proof of live endpoint success, no-card eligibility, remaining quota, output quality, alpha transparency, licensing, or commercial rights. JPEG structure validation is not a full pixel decode; manual viewability inspection is required.
- Use a non-sensitive test prompt only. Live requests remain separately manually authorized and must not be auto-triggered by pushes or pull requests.

## Acceptance criteria

- New workflow syntax and review checks pass on a pull request.
- No Cloudflare image inference is executed as part of CI or pull-request validation.
- No Cloudflare secrets are added, renamed, copied, echoed, or committed.
- Adapter source is pinned to the reviewed commit SHA, and GitHub Actions are pinned to reviewed immutable action SHAs.
- The workflow confirms secret presence without displaying values, gates the inference job on `refs/heads/main` and explicit no-payment confirmation, pins the remediated adapter by immutable SHA, validates PNG/JPEG bytes and dimensions, and publishes the detected-format image plus matching metadata for seven days.
- The old direct-live AstroCrown-Web workflow is removed so there is one clear manual qualification entry point.
- No live generation result or provider eligibility is claimed until the user manually runs the workflow and its evidence is inspected.

## Impact Analysis

**IF modified:** the existing credentials remain in NOVA, AstroCrown's reviewed adapter is reused without a second token, repository secret boundaries are respected, and one controlled image test becomes possible with a traceable artifact.

**IF not modified:** AstroCrown-Web's direct workflow will remain blocked by absent repository secrets, encouraging unnecessary token duplication or secret copying; no first image can be qualified via the existing adapter with the current credential placement.

## Explicit non-goals

- Do not change any Cloudflare, GitHub, NOVA or AstroCrown-Web secret values.
- Do not trigger a live workflow during implementation, tests, or pull-request checks.
- Do not enable paid billing or use a paid fallback.
- Do not modify the website homepage or publish the generated image into production.
- Do not qualify transparency, video, licensing, commercial rights, or the aggregate 86,400 GPU-minute/month target in this step.

## Impact and review evidence

- Existing adapter: `development/ai-media-generator/cloudflare_image.py` at AstroCrown-Web commit `d211dc5460941d60b9f1729791079cb9974d554a`.
- Existing offline tests remain in AstroCrown-Web and are not replaced.
- Existing NOVA Cloudflare smoke test targets LLM chat completions; it remains unchanged and is not evidence of image endpoint health.
- Initial live test: run https://github.com/ACROWN-System/NOVA/actions/runs/38573541271 failed during response validation and uploaded no artifact. The workflow has not yet been rerun against the remediated adapter. Provider qualification remains BLOCKED until a successful artifact is manually inspected and usage/account eligibility/rights evidence is recorded.


## Failure evidence, cause analysis and recurrence prevention — 2026-10-14

### Observed result

- The manually authorized run at https://github.com/ACROWN-System/NOVA/actions/runs/38573541271 passed the adapter checkout, Python setup, and required-secret presence check.
- The image request reached the adapter but failed with exit code 2: \`Provider output is not a valid PNG image.\`
- Artifact upload was skipped. No image was accepted or promoted. No secret value or provider response body was printed or preserved.
- This run alone does not prove the response was JPEG. The response body and signature were not preserved, so the underlying bytes could have been JPEG, an unexpected error response, or another malformed payload.

### Root cause

- **Direct technical cause:** PNG-only validation did not accept the returned body.
- **Process cause:** implementation treated the model's declared output schema as the complete provider contract, although the same provider documentation's usage example used \`image/jpg\`. Offline test fixtures modelled only PNG, so the test suite verified the chosen assumption rather than resolving the discrepancy against published usage and known provider issue evidence.
- **External reference:** Cloudflare model documentation https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-lightning/ and public documentation issue https://github.com/cloudflare/cloudflare-docs/issues/21022 record conflicting JPEG/PNG response conventions. This supports JPEG as a hypothesis, not a confirmed signature from the failed run.

### Remediation and anti-recurrence controls

- AstroCrown-Web PR #121 merged as \`72a7eaa70231653fb5baee5b6993464cca3c0656\`. It adds bounded PNG/JPEG recognition, separate declared and detected MIME provenance, truthful file extension, rejection of unknown/JSON/HTML payloads, offline format-drift tests, and updated audit records. It introduces no dependency and changes no credentials.
- This NOVA follow-up pins the immutable AstroCrown-Web merge SHA above and allows the upload step to collect either \`astrocrown-first-image.png\` plus its sidecar or \`astrocrown-first-image.jpg\` plus its sidecar. It remains manual-only and performs no inference during implementation or CI.
- For future external provider integrations, compare the API schema, official usage example, and relevant issue/changelog history before encoding a strict response contract; document conflicts as uncertainty; add deterministic tests for each relevant response variant; separate offline CI from manually authorized live qualification; and preserve only non-sensitive diagnostics (status, declared content type, byte count, recognized signature class), never response bodies or credentials.
- Residual limitation: JPEG marker/frame/scan validation is structural and not a full entropy decode. A successful workflow is not proof of visually usable pixels, alpha transparency, commercial rights, no-card eligibility, quota longevity, or production suitability. Inspect the actual image artifact before declaring the image pipeline operational.

## Updated Impact Analysis

**IF modified:** NOVA retains the sole secret/execution boundary, the adapter is pinned to the reviewed post-remediation revision, both supported file outcomes can be retained with truthful provenance, and the first integration failure becomes evidence for preventing the same assumption-driven defect in future provider work.

**IF not modified:** a valid JPEG response may continue to fail PNG-only validation; alternatively, if the adapter is updated without the NOVA artifact paths, a generated JPEG would fail at artifact upload. Future provider integrations would remain vulnerable to tests that encode an unverified interpretation of a conflicting external schema.
