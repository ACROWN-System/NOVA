# NOVA Provider Acquisition Readiness

## Purpose

This document defines what must be verified before adding any new AI/LLM or GPU credential to NOVA.

Credentials themselves must never be committed to Git. Only secret environment-variable names belong in repository configuration.

## Current development objective

The immediate objective is **$0 operational validation**:
1. Obtain free/no-cost credentials or credits where currently available.
2. Verify the provider's current API contract and model availability.
3. Add the provider only after verification.
4. Run NOVA health probes.
5. Run quality verification before treating a model/provider as operationally preferred.
6. Preserve measured evidence in NOVA health memory.
7. Keep fallback providers available.

"Free" means a documented free allocation, free credits, or shared free compute; it does not mean unlimited capacity.

## LLM acquisition queue

### Groq — high-priority verification

NOVA currently contains openai/gpt-oss-120b and openai/gpt-oss-20b.

Official rate-limit documentation currently lists both at 30 RPM, 1,000 requests/day, 8K TPM and 200K TPD on the free plan. Exact account limits must still be read from the provider account because limits apply at organization level.

Source: https://console.groq.com/docs/rate-limits
Credential slot: GROQ_API_KEY_01

### Google Gemini — high-priority verification

NOVA currently contains Gemini models, but model availability and free limits must be verified in the active AI Studio project before activation. Google states that limits vary by model/project and are visible in AI Studio.

Sources: https://ai.google.dev/gemini-api/docs/rate-limits ; https://ai.google.dev/gemini-api/docs/pricing
Credential slot: GEMINI_API_KEY_01

### Cloudflare Workers AI — high-priority verification

Workers AI currently provides a 10,000-Neuron/day free allocation. NOVA's roster was changed to the currently documented free-plan model candidate: @cf/zai-org/glm-4.7-flash.

Source: https://developers.cloudflare.com/workers-ai/platform/pricing/
Credential slots: CLOUDFLARE_API_KEY_01, CLOUDFLARE_ACCOUNT_ID

### Mistral — verify before activation

Keep the provider configuration only after current account access, model availability, and free-mode terms are verified.
Credential slot: MISTRAL_API_KEY_01

### Cerebras — verify before treating as a $0 dependency

The provider remains in the roster for compatibility/fallback architecture, but NOVA must not assume a perpetual free tier. Verify current signup, billing/credit requirements, model catalog, and quota before obtaining or depending on a credential.
Credential slot: CEREBRAS_API_KEY_01

### Additional candidates

OpenRouter, Hugging Face Inference, SambaNova, Cohere, NVIDIA and other providers may be evaluated later. Candidates remain candidates until current terms, model availability, commercial-use conditions, privacy/data-use terms, and measurable API behavior are verified.

## GPU acquisition queue

### Nosana — first GPU candidate

Nosana currently advertises free GPU credits for new builders and provides an API/SDK for GPU markets and workloads. Amount and eligibility must be verified in the actual account before NOVA treats the credit as available.

Sources: https://www.nosana.com/blog/the-new-nosana-experience-is-now-live/ ; https://learn.nosana.com/api/markets ; https://www.nosana.com/gpu-workloads/
Credential slot: NOSANA_GPU_API_KEY_01

Activation requires a provider-specific adapter. A generic GET health endpoint must not be treated as proof that a GPU workload can actually run.

### Hugging Face ZeroGPU — shared/free GPU candidate

Hugging Face currently documents ZeroGPU as shared GPU infrastructure for Spaces, with a free-account daily quota. This is not a generic GPU rental API and therefore requires a dedicated adapter.

Source: https://huggingface.co/docs/hub/main/spaces-zerogpu
Credential slot: HF_TOKEN_01 when authentication is required by the selected integration.

## Activation gates

A provider is not operational merely because a key exists.

NOVA should record:
- provider name
- credential environment name
- model/service name
- requested model
- actual model returned by the provider
- API status
- authentication result
- response-contract result
- latency
- baseline latency
- quality verification state
- quota/rate-limit evidence when exposed
- timestamp
- resulting action

## Quality gate

Availability and quality are separate dimensions.

A provider can be reachable but low quality, fast but low quality, high quality but unreliable, high quality but too slow, or available but outside the intended free-cost boundary.

NOVA must therefore never promote a provider solely because its API health probe succeeds.

Quality remains UNVERIFIED until an explicit benchmark has produced evidence.

## Future scaling

The same provider contract must remain usable when the project moves from free prototype -> free credits -> low-cost operation -> paid operation -> multi-provider production.

No architecture should require replacing the router when a provider, model, GPU class, or billing model changes.

## Security

Never store API keys, access tokens, wallet private keys, passwords, or provider secrets in roster.json, gpu_roster.json, health_state.json, source code, README files, or workflow YAML.

GitHub Actions secrets are the intended initial credential boundary.
