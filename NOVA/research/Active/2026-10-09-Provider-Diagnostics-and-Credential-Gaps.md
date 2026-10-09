# Provider Diagnostics and Credential-Gap Plan

**Date:** 2026-10-09  
**Status:** ACTIVE — implementation and verification in progress  
**Branch:** `fix/provider-error-diagnostics-and-readiness`

## Navigation-process limitation

The requested `NAVIGATION-PROTOCOL.md` and `NAVIGATION-PLAN-TEMPLATE.md` could not be found in the NOVA repository (including repository search). This plan records the blocker rather than pretending the prescribed protocol was reviewed. Re-establishing those repository-level navigation documents is a separate governance task and remains unresolved.

## Objective

Use the 2026-10-09 heartbeat evidence and public provider reports to improve diagnostics and correct free-provider readiness assumptions before acquiring more credentials.

## Evidence and questions

- NOVA run [37926549165](https://github.com/ACROWN-System/NOVA/actions/runs/37926549165): Mistral `mistral-small-latest` returned HTTP 429 / code 1300; current `diagnostic_headers={}` does not establish that Mistral sent no headers.
- Public Mistral reports show code 1300 accompanied by `x-ratelimit-limit-req-minute`, `x-ratelimit-remaining-req-minute`, `mistral-correlation-id`, and `x-kong-request-id`. Other reports show different request limits, so the code alone does not establish the underlying limit.
- The current allowlist omits those Mistral-specific names; the structured health-history path also drops the captured `response_headers`.
- NOVA run 37926549165 showed Groq 400 `json_validate_failed` with empty `failed_generation` on both GPT-OSS models. Current request config uses `max_tokens: 64`; official Groq docs specify reasoning controls and `max_completion_tokens` for GPT-OSS. Test a bounded provider-specific request update, but do not label it a verified live fix until a later manual run confirms.
- The run showed empty Cerebras and Cloudflare credentials in Actions; Cloudflare also requires an account ID. Current GPU resource documentation already names Nosana and Hugging Face ZeroGPU credential slots.
- Official Cerebras pricing states the $5 promotional credit requires a valid payment method and expires after 30 days; do not represent it as a perpetual no-card free tier.

## Scope

1. Extend safe diagnostic header allowlisting for evidenced Mistral headers and preserve the headers in durable probe history.
2. Parse Mistral-specific request/token windows distinctly from total account credits.
3. Add deterministic tests for header extraction/persistence and Groq GPT-OSS request budget configuration.
4. Correct provider acquisition/readiness records and add an evidence-labelled shortlist of potential additional providers, separating direct providers from aggregators and distinguishing confirmed terms from candidates.
5. Preserve the $0 / no-payment-method objective: no billing, payment method, provider secret, account setting, provider status or routing policy changes.

## Verification

- Inspect the patch.
- Run repository CI tests/compilation through the existing NOVA Health Tests workflow after the pull request is opened.
- No provider calls are performed by CI.
- Treat all proposed runtime request changes as candidate until a later live heartbeat proves the result.

## Impact analysis

**If modified:** Mistral response diagnostics become actionable when headers are present; durable history enables future correlation; Groq receives a more appropriate bounded GPT-OSS completion budget; readiness documentation reflects current provider terms and known credential gaps.

**If not modified:** Mistral 429 cause remains harder to isolate; captured headers are not durable; Groq JSON-validation failures remain unresolved; the documented Cerebras free-tier claim may mislead credential acquisition.

## Completion criteria

All intended changes reviewed; automated tests pass; PR opened; remaining live-only questions explicitly classified UNKNOWN/BLOCKED. Move this plan to Completed after the implementation stage is verified, not merely because code was committed.
