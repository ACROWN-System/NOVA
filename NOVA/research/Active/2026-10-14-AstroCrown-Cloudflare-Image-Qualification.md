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


## First successful live image — 2026-10-14 — run #38577103848

**Result:** REQUEST AND ARTIFACT DELIVERY PASS; JPEG/MIME MISMATCH CONFIRMED; PROMPT FIDELITY PARTIAL; COMMERCIAL/ALPHA QUALIFICATION BLOCKED.

- Run: https://github.com/ACROWN-System/NOVA/actions/runs/38577103848
- Job log: https://github.com/ACROWN-System/NOVA/actions/runs/38577103848/job/115897000012
- The job fetched and verified AstroCrown-Web merge SHA 72a7eaa70231653fb5baee5b6993464cca3c0656, checked existing secret presence without printing values, executed one image request, and uploaded the artifact successfully.
- Artifact: astrocrown-cloudflare-image-38577103848, artifact ID 11901575526, expiration 2026-10-21T14:03:32Z. The archived ZIP is 72,164 bytes; SHA-256 8e2184d464b345567d1270c81e2f60561f0fc9b4e4f2c1b4deab10463aa889fa.
- Files included: astrocrown-first-image.jpg (72,727 bytes) and astrocrown-first-image.jpg.metadata.json.
- Independent post-download inspection successfully opened and fully decoded the JPEG: 1024×1024 pixels, RGB mode, SHA-256 639221c57e74e2289e72946b158464474c837e1921767ce089dbf6b718f206ae.
- **Provider response contract confirmed:** the response declared Content-Type: image/png, but the payload was a valid, fully decodable JPEG. Sidecar records the mismatch and that the known Cloudflare PNG/JPEG inconsistency was tolerated. This is direct evidence on this successful run; the earlier failed run remains inconclusive because its response body was not preserved.
- Timing: adapter wall-clock measurement 3556 ms; includes network request, validation and local file writes, and is not provider-only latency. This single observation is insufficient to establish an ongoing service-level target.
- Visual result: a starfield with strong violet/magenta nebula clouds and a prominent planet left-of-center. No obvious text or watermark. It did not satisfy the intended small planet near the lower-right edge or the restrained/subtle cloud direction. **Prompt fidelity: PARTIAL.** Keep the result as an internal reference, not a selected/promoted homepage asset.
- JPEG is RGB and does not preserve alpha transparency. Do not use this output as a transparent compositing layer.
- Sidecar rights status remains NOT_YET_QUALIFIED_FOR_COMMERCIAL_PROMOTION. Successful execution does not establish licensing, commercial-use permission, account entitlement stability, or ongoing no-cost usage.
- AstroCrown-Web PR #122 was merged as `a73b96863eb37d33c2d9cee43cc7c83e2dccade6`; its offline tests and CodeQL checks passed. It corrects JPEG alpha-status metadata without requiring another live image call. This NOVA follow-up updates the immutable adapter pin so a future manual run includes that correction.

## Cost/usage evidence boundary

The user explicitly confirmed the current no-payment configuration before dispatch. The current model page displays SDXL-Lightning at $0.00 per step (https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-lightning/). The general Workers AI pricing page separately documents a 10,000-Neuron/day Workers Free allocation and overage billing under Workers Paid (https://developers.cloudflare.com/workers-ai/platform/pricing/). Neither the successful job log nor the artifact proves dashboard consumption, subscription/billing state, remaining daily allocation, or invoice status. Before another request or batch, inspect account usage/billing evidence if the no-payment boundary is uncertain; do not infer a billing amount from a successful response.

## Updated operational conclusion and Impact Analysis

The image adapter is now **functionally demonstrated for a single live generation request**, including its ability to accept the model's JPEG bytes despite the image/png declaration. The wider provider remains **partially qualified only**: prompt fidelity is partial; alpha transparency is unsupported by this JPEG; commercial rights and sustainable account/usage eligibility remain unverified.

**IF updated:** both NOVA and AstroCrown audit records reflect the actual successful run, preserve the artifact checksum and response contract evidence, prevent overclaiming visual/license/alpha readiness, and document the next bounded checks.

**IF not updated:** the earlier failure would remain the latest documented outcome; operators could overlook the confirmed JPEG/MIME discrepancy, misuse an RGB JPEG for transparency layers, or mistake one successful request for evidence of rights, sustainable capacity or known billing status.

## Next decision gate

Do not dispatch another live request just to validate the metadata correction. The AstroCrown-Web correction is merged; this NOVA PR pins that immutable revision for any future dispatch. Then decide whether the next manually authorized image request should target stronger prompt adherence (small planet placed deliberately at lower-right) or whether the current result should be kept solely as a rough background candidate. Any further public/commercial promotion remains behind independent license, usage, visual-quality and alpha/transparency gates.

## Second successful live image request — 2026-10-15 — run #38714064899

**Result:** LIVE REQUEST / IMAGE-CONTAINER VALIDATION / ARTIFACT DELIVERY PASS; DESIRED LOW-DISTRACTION VISUAL STYLE NOT MET BY THIS SAMPLE; COST/RIGHTS/ALPHA STILL UNQUALIFIED.

- Run: https://github.com/ACROWN-System/NOVA/actions/runs/38714064899
- Workflow commit: https://github.com/ACROWN-System/NOVA/commit/9c3cf01cdda53336c465050aafd0552f79160443
- The manual workflow completed successfully in 21 seconds. Its generation/validation step recorded `CLIENT_TOTAL_ELAPSED_MS=8392`; this covers request, validation, and local artifact writing rather than provider-only latency.
- Request: `@cf/bytedance/stable-diffusion-xl-lightning`, 1024×1024, four steps. The positive prompt explicitly requested nearly black/deep navy, sparse tiny dim stars, a subtle desaturated blue-violet nebula and no bright flares, text, logos or UI. No seed was supplied, so sampling was stochastic.
- Artifact: `astrocrown-cloudflare-image-38714064899` (ID `11961394496`, 7-day retention). It contains `astrocrown-first-image.jpg` and `astrocrown-first-image.jpg.metadata.json`; image file length 61,018 bytes. SHA-256: `d3c05c8c5949dca27f1dad609fd8a0a220076aa647afd386b58022cb67bc67ed`.
- The sidecar confirms Cloudflare declared `image/png` while the validated payload was JPEG. The adapter wrote the truthful `.jpg` extension and recorded the declared/detected mismatch. Request ID was not exposed.
- Preliminary visual inspection: the sample has a useful dark central region, but its nebula remains intensely magenta/violet, multiple stars have prominent bright flares, and distracting streak-like marks appear. It therefore does **not** pass the desired restrained homepage-background style check. This is a review of this specific sample, not proof that all stochastic outputs from the model will fail.
- JPEG does not preserve alpha transparency. Do not use this as a transparent layer or promote it as a selected homepage asset. The artifact is diagnostic evidence only.
- The workflow ran only after its operator-selected `no_payment_confirmed=yes` gate was satisfied. That is an operator assertion, not billing telemetry. The run and artifact provide no provider billing-meter data, quota-burn amount, invoice evidence, or remaining free allocation; cost and quota remain **NOT MEASURED**.
- The `actions/upload-artifact` Node.js 20 deprecation warning did not fail this run. Track action-runtime modernization separately rather than misclassifying it as an inference failure.

## Recurrence-prevention update — negative-prompt traceability

The sample exposed one actionable workflow limitation: the AstroCrown adapter already supported Cloudflare's documented `negative_prompt` request parameter, but the NOVA manual workflow did not expose or pass that parameter. Further, the adapter previously did not copy a supplied negative prompt into the provenance sidecar. A prompt-refinement experiment would therefore have been less controlled and less auditable than necessary.

- AstroCrown-Web PR #127 was merged as [`cdde2a8a3a008da91b88111b3fa6fac1b5ae4937`](https://github.com/ACROWN-System/AstroCrown-Web/commit/cdde2a8a3a008da91b88111b3fa6fac1b5ae4937). It records negative prompts in sidecar metadata and adds an offline test confirming the value reaches both the request payload and metadata. Its AI Media Generator Offline Tests, External Review Pipeline CI, NOVA RSI Engine CI and NOVA RSI CodeQL checks all passed before merge.
- This NOVA branch adds an optional `negative_prompt` input (pre-filled to suppress neon/magenta saturation, bright starbursts, lens flares, overexposed highlights, streaks, oversized stars and baked-in text/UI), forwards it through the environment to the adapter CLI without shell interpolation, and pins the reviewed AstroCrown-Web merge SHA above. It does not trigger generation.
- The repository's recursive tree at main commit `9c3cf01cdda53336c465050aafd0552f79160443` contains the existing active plan but no `NAVIGATION-PROTOCOL.md` or `NAVIGATION-PLAN-TEMPLATE.md`. This existing active record is being continued transparently rather than claiming those absent files were reviewed.

## Updated next decision gate — second prompt-quality sample

After this NOVA workflow change passes review and merges, manually dispatch one more request using the same positive prompt, 1024×1024 dimensions and four steps as run #38714064899, leaving the new negative-prompt default unchanged. This makes the negative-prompt input the only deliberate request-setting change; because the previous request did not specify a seed, do not claim deterministic A/B equivalence. Inspect the new image and its sidecar before any follow-up request. If the visual direction still fails, research a materially different model/route or a bounded deterministic post-processing/composition approach instead of repeating near-identical requests. Continue to keep the result blocked for commercial promotion, genuine alpha, and verified cost/account eligibility until independent evidence passes those gates.
