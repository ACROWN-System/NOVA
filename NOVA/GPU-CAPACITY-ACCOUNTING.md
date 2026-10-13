# Aggregate GPU-Capacity Accounting

**Status:** Initial evidence register and deterministic accounting implementation  
**Last reviewed:** 2026-10-13  
**Current intended use:** **Non-commercial research and development in the GitHub development environment**  
**Monthly target:** **86,400 GPU-minutes across all eligible providers combined**

## Objective and accounting unit

One GPU-minute means one GPU allocated for one minute. Two GPUs allocated concurrently for one minute contribute two GPU-minutes. Under this convention, 86,400 GPU-minutes over a 30-day period equal two continuously allocated GPU equivalents. The target is aggregate; no single provider must supply it alone.

The evidence register is **NOVA/gpu_capacity_evidence.json**. The deterministic report engine is **NOVA/gpu_capacity.py**. The GPU heartbeat adds the report to **last_gpu_heartbeat.aggregate_capacity**. The capacity code performs no provider requests and cannot activate an account or spend credits.

## What counts

A recurring contribution counts only when all of the following are evidenced and current:

1. The account and its eligibility for the specific free allocation are verified.
2. The allocation is available without a payment method and has no cash cost under the agreed policy.
3. The provider's terms permit the current non-commercial R&D activity, including personal/internal-use, research, third-party-benefit, acceptable-use and workload restrictions. Commercial-use rights are **not required now**.
4. Automated access is supported for the intended system operation.
5. GPU type, VRAM, concurrency/queue behavior and workload compatibility have been tested sufficiently for the intended use.
6. Handling of the specific input/output data has been approved; community-hosted volunteer inference is not implicitly authorized.
7. A real allocation test passed and its evidence identifies the tested configuration.
8. Usable recurring GPU-minutes/month, the observation time, an expiry/validity time, and HTTPS evidence links are recorded.
9. The provider is activated in the current **NOVA/gpu_roster.json** before its amount counts as operationally available.

A missing field, unknown state, stale timestamp, invalid number, or unsupported claim blocks that contribution. Explicitly disallowed current R&D use or a required payment method excludes a candidate. Absence of commercial-use rights alone does not exclude a provider during this research phase.

## Separate quantities; never double-count

| Quantity | Meaning | Counts toward recurring monthly target? |
|---|---|---:|
| Advertised monthly GPU allowance | Public quota or normalized estimate | No |
| Verified eligible recurring GPU-minutes/month | Current account-level recurring allocation passing every gate | Not until active in the GPU roster |
| Verified active recurring GPU-minutes/month | Eligible recurring allocation integrated and active | Yes |
| Verified one-time GPU-minutes available | Current unused credits translated into measured GPU-minutes with evidence and expiry | Only for the current period; tracked separately from recurring capacity |
| Reserved GPU-minutes | Capacity reserved for running or scheduled work, according to explicit metering | Tracked separately |
| Idle allocated GPU-minutes | GPU time allocated but not completing useful work | Tracked separately |
| Completed useful GPU-minutes | Instrumented GPU allocation used to complete useful work | Tracked separately |
| Unknown or unmetered usage | Insufficient trustworthy usage measurements | Remains unknown, never silently converted to zero |

Recurring capacity values must exclude one-time credits. The aggregate engine will not convert a dollar balance, provider credit unit, CPU-hour or API call allowance to GPU-minutes without a sourced price/allocation measurement. An authenticated credential is not proof of allocation.

## Intended-use boundary

The current phase is research and development in GitHub and related development infrastructure; this is not yet a commercial service. Commercial-use rights are therefore not a qualification gate for current use. The gate is whether the provider's terms permit this specific non-commercial R&D activity, including restrictions on personal/internal use, benefit to third parties, acceptable use, data handling, automation and the intended workload.

This does not permit bypassing provider terms. If a term's application to AstroCrown R&D is ambiguous, mark the candidate BLOCKED until clarified. When the intended use changes to commercial production, every provider must be requalified. The accounting engine compares each provider's `qualification_use_mode` against the code policy's current intended-use mode; old R&D evidence cannot qualify a provider for commercial production without a new assessment.

## Initial provider assessment — official-source review on 13 October 2026

| Candidate | Evidence found | Accounting treatment now |
|---|---|---|
| Hugging Face ZeroGPU | Official documentation specifies 5 GPU-minutes/day for a free account and shared/queued Space access. Five minutes/day multiplied by 30 days gives a theoretical 150-minute allowance, not reserved capacity. [Official ZeroGPU documentation](https://huggingface.co/docs/hub/main/en/spaces-zerogpu) | Advertised estimate recorded as 150; **0 verified minutes counted** until account eligibility, no-card terms, commercial permissions, approved data handling, workload path and real allocation are proven. |
| Nosana | The official Credits API documents balance and free-credit eligibility/request endpoints; requests are subject to eligibility. [Credits API](https://learn.nosana.com/api/credits.html) · [Terms](https://www.nosana.com/terms-and-conditions/) | Candidate retained; account credit balance, no-card eligibility, workload pricing, recurring allowance and a real qualifying allocation remain unverified. |
| Lightning AI | The current official pricing page advertises up to 80 free GPU hours to start, no card, and GPU-hour values that vary by GPU; phone verification is required for the free GPU-hour allocation. [Official pricing](https://lightning.ai/pricing) · [AI Studio guide](https://lightning.ai/docs/overview/ai-studio/) | Prioritize a bounded R&D allocation test after eligibility and terms review. The public headline is not an account-observed balance, a guaranteed monthly allowance, or a verified GPU-minute contribution. |
| Modal Starter | The official page advertises $30 of included compute each month; that is a dollar balance across resource types, not a fixed GPU-minute allowance. The official startup page exposes a payment-method FAQ, but the retrieved evidence does not settle this account's no-card eligibility. [Pricing](https://modal.com/pricing) · [Startup program](https://frontend.modal.com/startups) | Candidate research only; no amount counted until no-card eligibility, terms, GPU rate/resource mix and tested usable capacity are documented. |
| Google Colab free | Official FAQ states that free GPU access is dynamically limited, not guaranteed, and hardware/runtime limits vary. [Official FAQ](https://research.google.com/colaboratory/faq.html) | Not counted as unattended production capacity. It may still be a manual development/test tool. |
| Kaggle notebooks | The [Terms of Use](https://www.kaggle.com/terms) restrict usage to personal, internal, non-commercial use and prohibit use on behalf of or for the benefit of a third party. | Not excluded merely for lacking commercial rights. **BLOCKED** until we determine whether this R&D activity fits the personal/internal-use and no-third-party-benefit restrictions. |
| Vast.ai | The [official FAQ](https://console.vast.ai/faq/) states that a verified credit card is required to receive test credit. | Excluded from the current no-payment-method path unless a qualifying no-card allocation is evidenced independently. |

This is an ecosystem shortlist, not a claim that every candidate is commercially eligible or currently available. Account-specific observations are still required.

## Current verified result

At the latest checked operational-state observation, no GPU provider was active in **NOVA/gpu_roster.json**; Nosana and Hugging Face credentials were unconfigured. Consequently, the verified operational contribution is **0 GPU-minutes/month** and the target gap **after verified active capacity** remains 86,400. This is a verified-evidence accounting result, **not a claim that no other GPU capacity could exist**. See the [dedicated operational-state record](https://github.com/ACROWN-System/NOVA/blob/nova-operational-state/NOVA/health_state.json).

The actual useful GPU work completed month-to-date remains **UNKNOWN / NOT METERED**. It is not reported as zero, because no complete usage-metering source has yet been connected.

## Discoveries, decisions, unresolved items

### Discoveries

- The aggregate target requires contributions from multiple eligible providers.
- Hugging Face ZeroGPU's free tier has a useful but small documented daily allowance; shared/queued behavior prevents treating its theoretical allowance as reserved minutes.
- Nosana's credits API exposes a balance shape and separate eligibility path; neither establishes this account's available credits by itself.
- Lightning AI has a no-card free tier and an advertised initial credit amount; GPU-minutes need account and workload measurement.
- Modal's included amount is dollar-denominated compute, not GPU time.
- The free-provider policy is scoped to non-commercial R&D. Kaggle's personal/internal-use and no-third-party-benefit restrictions require a use-specific check; they must not be converted into a blanket commercial-rights gate.

### Decisions

- Retain a fixed target of 86,400 GPU-minutes/month.
- Keep advertised allowances, verified recurring capacity, one-time credit capacity, reserved/idle time and completed useful work separate.
- Never promote candidate credentials, an HTTP 200, an advertised quota, account credits or an unmeasured GPU price into verified usable GPU-minutes.
- Keep providers inactive until the external contract for the current R&D use, account eligibility, free/no-card condition, data boundary, workload path and allocation evidence pass.
- Do not send sensitive or private prompts to unapproved community-operated providers.

### Unresolved / blocked

- Nosana's account credits, no-card eligibility, current GPU-minute cost and usable recurring allocation.
- Hugging Face account eligibility, commercial/data terms for the proposed Space, the actual app's compatibility, and tested daily/monthly usable allocation.
- Lightning account credit balance and GPU conversion for a chosen model, plus commercial/data and automation qualification.
- Modal's no-card eligibility for this account, current selected-GPU costs and tested monthly capacity.
- An approved instrumented route for completed/idle/reserved GPU-minute measurements.
- The required navigation protocol/template are unavailable in the active repository tree; this limitation must not be replaced by a claim that the canonical plan workflow was followed.

## Next actions

1. Verify a candidate's exact account eligibility and terms before adding credentials or activating it.
2. Run a bounded, approved allocation test for a selected workload and capture GPU type, VRAM, runtime, queue time, limits, cost, result and expiry.
3. Enter a recurring capacity observation only with a trustworthy monthly-minute amount, observation timestamp, expiry and evidence URLs. Enter one-time credits separately.
4. Re-test current capacity when evidence expires; do not count stale values.
5. Connect provider-specific usage meters before claiming completed useful GPU-minutes.
6. Update this register additively, run the full NOVA health suite, review the resulting PR, then inspect post-merge heartbeat state.

## Impact Analysis

**IF merged:** NOVA can present a consistent, auditable total over the combined provider portfolio while preventing advertised, unknown, expired, card-dependent, non-commercial or untested allocations from inflating the target.

**IF not merged:** Capacity will remain scattered across provider-specific observations, making it easier to confuse public allowances, credentials, dollar credits and actual usable GPU time; the 86,400-minute target will have no deterministic aggregate evidence report.

- Do not require commercial-use rights during the current R&D phase; requalify providers if the intended use changes to commercial production.
- Optimize for reliability through eligible provider diversity, bounded allocation tests, observed success/failure rates, queue/runtime evidence and preserved fallbacks; advertised quota alone is not a reliability signal.