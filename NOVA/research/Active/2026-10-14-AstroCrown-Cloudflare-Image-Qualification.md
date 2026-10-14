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
2. Check out AstroCrown-Web at the recorded adapter commit SHA, not a floating branch, and invoke `development/ai-media-generator/cloudflare_image.py`.
3. Restrict workflow permissions to the minimum required: repository contents read-only; no issue writes, repository writes, or credential changes.
4. Validate the PNG with the existing adapter and upload only the PNG and its provenance sidecar as a short-retention artifact.
5. Retire the duplicate direct-live workflow from AstroCrown-Web. Keep AstroCrown-Web's offline tests and code adapter; do not add its own token or account ID secrets.
6. Keep all existing NOVA LLM/GPU health workflows, credential names, provider states, billing configuration, and operational-state writers unchanged.

## External API contract

- Endpoint: Cloudflare Workers AI REST API, `POST https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/bytedance/stable-diffusion-xl-lightning`.
- Auth: bearer token supplied only as a process environment variable on the NOVA runner. Never print it, pass it in command-line arguments, or write it to the artifact.
- Expected output: binary `image/png`; the existing adapter validates PNG structure, CRCs, decompression, and requested dimensions. Fail closed on provider errors or unexpected response content.
- An offline-test pass is not proof of live endpoint success, no-card eligibility, remaining quota, output quality, alpha transparency, licensing, or commercial rights.
- Use a non-sensitive test prompt only. The first live request is a separate, manually authorized action and must not be auto-triggered by pushes or pull requests.

## Acceptance criteria

- New workflow syntax and review checks pass on a pull request.
- No Cloudflare image inference is executed as part of CI or pull-request validation.
- No Cloudflare secrets are added, renamed, copied, echoed, or committed.
- Adapter source is pinned to the reviewed commit SHA, and GitHub Actions are pinned to reviewed immutable action SHAs.
- The workflow confirms secret presence without displaying values, gates the inference job on `refs/heads/main` and explicit confirmation, validates the PNG, and publishes the PNG plus metadata for seven days.
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
- Current status: BLOCKED pending PR review/merge and one user-authorized manual dispatch. No live image-generation call has been made by this plan.
