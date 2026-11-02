# NOVA Administrative Smart-Account Security Architecture

**Document ID:** NOVA-SEC-ADM-001  
**Date:** 2026-11-02  
**Status:** OWNER-ACCEPTED ARCHITECTURE DIRECTION — DOCUMENTATION ONLY; NOT A RUNTIME CAPABILITY CLAIM  
**System ownership:** NOVA  
**Initial application context:** AstroCrown administrator operations  
**Related implementation record:** [AstroCrown-Web PR #141](https://github.com/ACROWN-System/AstroCrown-Web/pull/141)  
**Application requirements:** [AstroCrown User and Administrator Account Requirements](https://github.com/ACROWN-System/AstroCrown-Web/blob/docs/provider-independent-wallet-auth-plan-2026-10-20/development/account-continuity/USER-AND-ADMIN-ACCOUNT-REQUIREMENTS.md)  
**Detailed security requirements:** [NOVA Administrative Smart-Account and Transaction-Enforcement Specification](https://github.com/ACROWN-System/AstroCrown-Web/blob/docs/provider-independent-wallet-auth-plan-2026-10-20/development/account-continuity/NOVA-ADMINISTRATIVE-SMART-ACCOUNT-SECURITY-SPEC.md)

## 1. Governing decision: the enforcement account is NOVA

The programmable administrative smart account and its transaction-validation mechanism are components of NOVA itself. They are not an external wallet-security service sitting beside NOVA.

NOVA therefore includes both:
- the off-chain intelligence, governance, policy, orchestration, monitoring, audit and incident-response capabilities; and
- the on-chain programmable accounts, mandatory transaction validators, enforcement guards and constrained recovery mechanisms that make approved policies enforceable before execution.

NOVA must not merely observe prohibited activity and react after assets have moved. It must reject prohibited administrative operations before execution. On-chain enforcement is part of NOVA's security boundary and remains mandatory even if an off-chain NOVA service is unavailable, compromised or bypassed.

This document establishes the architecture direction and security invariants. It does not claim that these smart accounts, contracts or runtime capabilities have already been implemented.

## 2. Asset and wallet separation

Three separate wallet functions must remain distinct.

### 2.1 Administrator-owned external identity and compensation wallet

For the AstroCrown administrator workflow, the administrator's external wallet remains under the administrator's control.

Its allowed purposes are:
- proving control of a registered wallet during administrative sign-in or step-up;
- signing a reviewed, domain- and session-bound authentication challenge; and
- receiving that administrator's salary, service payments, bonuses or other compensation through a separate payout workflow.

It is not a wallet for AstroCrown organizational funds or NOVA operational funds. It is not the treasury key, does not own the NOVA operations smart account and does not provide unrestricted authority over organizational assets. NOVA/AstroCrown must never request or store its private key or seed phrase.

The authentication-wallet association and compensation-destination record are separate account purposes, even if the same external address is registered for both. A compensation payment is not an administrative transaction and does not prove administrative authorization. A change to the payout destination requires heightened verification and an auditable record.

When administrator privileges are revoked, the external address loses its association as an administrator authenticator. Its owner retains control of the external wallet and any funds already held there. Earned compensation is not confiscated. Further payouts may be held only where that destination is independently suspected to be compromised or a separate approved payment hold applies.

### 2.2 NOVA administrative operations smart account

Each administrator receives a separately identifiable programmable administrative operations smart account. A per-administrator account is the default because it limits the blast radius, provides clear attribution and prevents one compromised administrator account from directly affecting every other administrator's operational account.

This account:
- is created and registered through NOVA's governed administrator lifecycle;
- is a first-class component of NOVA;
- is enforced by mandatory NOVA transaction-validation logic before execution;
- holds only the minimum organizational operational assets needed for explicitly assigned duties;
- can perform only policy-approved administrative operations;
- cannot be used for an administrator's personal transactions or compensation;
- cannot directly control or drain the AstroCrown treasury; and
- can be frozen, suspended, revoked and recovered through its pre-authorized constrained emergency path.

The administrator's external identity wallet must not become an unrestricted owner key for the operations account. Any signature relationship must be narrowly scoped and validated by the mandatory smart-account rules. The signer and account-abstraction implementation must be selected during the later technical design; it must not weaken the invariants in this document.

### 2.3 Treasury and protected recovery vault

The AstroCrown treasury is a separate organizational asset domain. Routine administrator permissions and ordinary operations-account authority must not provide unrestricted treasury ownership, withdrawal or upgrade rights.

The recovery vault is another separately controlled destination. Its address and authorization rules must be established before an operations account receives assets. Recovery may send funds only to that predetermined destination through constrained logic; an administrator or an incident-time NOVA service must not be able to replace it with an arbitrary address.

## 3. NOVA architecture and transaction path

### 3.1 Off-chain policy and governance

Before creating an administrative operation, NOVA must:
1. authenticate the ordinary AstroCrown account;
2. confirm the server-owned administrator role and exact permission;
3. verify a fresh external-wallet step-up when required;
4. canonicalize the requested operation, including chain, account, destination, asset, amount, contract/function, payload, nonce and validity period;
5. evaluate the operation against the current policy, administrator scope, approved destinations/contracts, operational limits and policy version; and
6. approve, reject or escalate the request with a durable decision record.

The off-chain layer may prepare and relay approved transactions. It must not possess an unrestricted private key capable of bypassing NOVA's on-chain guard or freely transferring organizational assets.

### 3.2 On-chain validation and enforcement

The NOVA administrative operations account must be designed for Solana's program/account execution model rather than assumed to be an Ethereum-style ERC-4337 account. A NOVA program will hold policy state in explicit data accounts and control per-administrator operational vault authorities through program-derived addresses (PDAs) where the reviewed design supports that pattern. A PDA has no private key; only its deriving program can authorize it through the runtime's PDA-signing/CPI mechanism. The NOVA program independently validates each exact operation before it invokes a transfer or other state-changing CPI. The validation path is mandatory and must not be removable by an ordinary administrator.

It must reject:
- destinations, contracts, assets, networks and functions outside the approved policy;
- values, spending rates or operation frequencies above assigned limits;
- requests without the required role, permission and authorization evidence;
- stale, expired, replayed or incorrectly bound authorizations;
- malformed, unknown or unverifiable operations;
- operations evaluated against an obsolete, missing or inconsistent policy version; and
- any attempt to disable, replace or bypass the guard through an unapproved program upgrade, alternate instruction, cross-program invocation (CPI), authority account, token-account owner/delegate, signer or PDA-control route.

Unknown or ambiguous conditions fail closed. A lack of NOVA policy data, inability to verify an authorization, or unavailability of a required validation dependency must never turn into permission to execute.

### 3.3 Monitoring and reconciliation

NOVA must continuously monitor supported networks and periodically reconcile on-chain state against the expected policy and account configuration.

Monitoring should include, when supported:
- native-asset and token balances/transfers;
- approvals, allowances and permit authorizations;
- contract calls and function selectors;
- program IDs and upgrade authorities, owner/signer/guardian state and recovery configuration;
- PDA derivations and control relationships, program-owned state accounts, token-account authorities/delegates and CPI routes;
- session/delegated authorities and spending limits;
- policy and contract upgrades;
- rejected, pending, replaced and executed operations; and
- emergency freezes and recovery actions.

NOVA must declare which chains, account implementations and asset types are actually covered. Monitoring or recovery must not be claimed for unsupported chains, tokens or contracts. Each network needs defined confirmation depth, RPC/provider failure handling, reconciliation cadence and incident evidence requirements.

## 4. One-violation rule and automatic response

### 4.1 Qualifying attempt

A deliberate prohibited operation submitted or approved by a currently authenticated and wallet-step-up-verified administrator is a qualifying violation, even when NOVA blocks it before execution. The policy is one violation: that attempt triggers the same administrative security response as a confirmed compromise.

A qualifying event must be attributable to an authenticated administrator action or valid authorization from that administrator's approved administrative context. An unauthenticated third-party probe, forged request, ordinary transport failure or benign interface/network error is not by itself proof of administrator misconduct. Such events still require logging, security evaluation and appropriate protection.

The administrative policy must be disclosed to administrators before they receive the corresponding access and must explain the prohibited operations clearly.

### 4.2 Automatic response

Once NOVA establishes a qualifying violation, the response must be automatic and must not wait for discretionary manual approval or an informal operator decision.

NOVA must:
1. **Reject the operation.** The prohibited operation does not execute.
2. **Contain the account.** Suspend the affected administrative operations smart account and prevent new administrative operations from using it.
3. **Revoke authority.** Remove the administrator role and all associated permissions; expire active administrator sessions and delegated authorities; invalidate outstanding operation authorizations.
4. **Unregister the operations account.** Mark its address as revoked in the authoritative NOVA registry and retain its incident history. It cannot be silently re-enrolled.
5. **Protect remaining assets.** Automatically invoke the pre-authorized emergency freeze/recovery path for the affected operations account and transfer remaining recoverable operational assets to the predetermined protected recovery vault.
6. **Remove privileged wallet association.** Remove the administrator's external wallet from the administrator-authenticator registry without seizing, taking control of or confiscating that external wallet.
7. **Notify the account holder.** Persist the incident and show the standard notice in the ordinary AstroCrown User dashboard. The Administrator access button disappears because the backend no longer reports active administrator authority.
8. **Require formal reinstatement.** Restoration requires security review and new authorization. Reconnecting the external wallet alone does not restore the role or reactivate the revoked operations account.

### 4.3 Constrained emergency authority

Automatic recovery must be possible because the recovery power was deliberately and narrowly authorized when the smart account was created—not because NOVA acquired an unrestricted private key after an incident.

The NOVA emergency controller may only:
- freeze or disable the exact registered operations account;
- invalidate its administrative operation authorizations;
- move its remaining supported operational assets to the predetermined recovery-vault address; and
- emit a permanent recovery/audit record.

It may not transfer to an arbitrary destination, withdraw treasury assets, expand its own powers, install a bypass, alter the recovery destination or perform general-purpose transactions. Any cryptographic threshold or independent attestation requirement must be established in advance and be available to the automated incident path; it must not become an ad hoc manual approval that defeats the required response.

If a supported network is temporarily unavailable, NOVA must immediately revoke the off-chain administrative role and sessions, keep the on-chain guard fail-closed, persist the recovery instruction, and retry the pre-authorized on-chain recovery path when the network is available. The incident must not be reported as fully recovered until the chain confirms the recovery outcome.

### 4.4 Dashboard message

The ordinary User dashboard remains accessible. The Administrator access entry is absent and the same incident notice applies whether the prohibited attempt was blocked before execution or the event was a confirmed compromise:

> **Administrative privileges revoked**  
> Your NOVA administrative operations account attempted an operation that violates AstroCrown's Administrative Wallet Security Policy. The operation was blocked. Your administrative operations account has been disabled, your administrator privileges have been revoked, and the security incident has been recorded by NOVA.  
>
> Your ordinary AstroCrown account remains accessible, but you no longer have access to the Administrator dashboard.  
>
> Incident reference: [Generated incident ID]

The message must be driven by authoritative NOVA/backend incident state, not a client-side condition. The incident reference, event time, policy version, rejected operation summary and recovery status must be available in the security audit history without exposing private credentials.

## 5. Financial and personal-property boundary

- An administrator's external wallet is not an organizational funds wallet. It may receive personal compensation through a separate payout workflow.
- The NOVA operations smart account holds only organizational operational funds allocated to administrative duties.
- The AstroCrown treasury remains separately controlled.
- Recovery applies to the affected NOVA operations account's remaining supported operational assets, not to assets in the administrator's external wallet.
- Revocation does not confiscate salary or bonuses already earned. Compensation disputes and lawful payment holds are managed through separate finance/governance procedures.
- If an external payout destination is itself suspected compromised, further payments to that destination are held pending independent verification; this does not give NOVA custody of the external wallet.

Recovery cannot guarantee retrieval of assets already transferred to another address, irreversibly consumed, or locked in a contract without an applicable recovery mechanism. “Recover remaining assets” means assets still controlled by the NOVA operations account and supported by the pre-authorized recovery implementation.

## 6. Governance and resilience requirements

- The transaction guard, validator, recovery controller and upgrade mechanism are security-critical NOVA components.
- No routine administrator or single NOVA service credential may silently disable the mandatory guard or grant itself unrestricted recovery/treasury authority.
- Policy updates, contract upgrades, signer/guardian changes, recovery-vault changes and emergency permissions require separately governed authorization, independent review, auditable rationale and tested procedures.
- The on-chain enforcement layer must remain restrictive if off-chain policy services fail.
- An off-chain compromise must not make the smart account permissive.
- A compromise of the enforcement root or upgrade authority is a system-level incident; NOVA must not claim that monitoring alone guarantees recovery from it.
- Emergency freeze/recovery authority must be narrow enough to protect assets without creating an alternative unrestricted asset-transfer path.
- Every account creation, policy change, suspension, recovery, revocation and reinstatement must be auditable.
- Reinstatement requires formal review and fresh authorization; the revoked account is not simply switched back to active.

## 7. Required implementation stages

1. **Threat model and policy schema:** formalize operation types, prohibited actions, allowed destinations, limits, identity binding, attribution rules and incident thresholds.
2. **Offline reference model:** implement the policy evaluator and incident state machine with synthetic data. No private keys, live network transactions or real assets.
3. **Smart-account selection:** compare maintained account-abstraction implementations and supported standards; review their code, maintenance, license, audit history, compatibility, upgrade paths and cost. Do not select a framework merely because it is popular.
4. **Test-chain prototype:** implement the smart account, validation guard, restricted emergency controller and fixed recovery destination on a zero-cost test network where practical.
5. **Adversarial and invariant testing:** test direct-call, module, fallback, upgrade and guard bypass; replay; stale policy; malicious delegation; compromised off-chain service; false attribution; recovery destination substitution; partial recovery; and network failure.
6. **Independent review:** obtain independent smart-contract and system security review before any production asset is deposited.
7. **Production authorization:** separately approve deployment, monitoring, key/authority operations, upgrade process, emergency procedure, recovery drills, custody and treasury boundaries.

Do not use production assets or credentials during stages 1–6. Prefer local/offline tests and $0 test environments; do not consume paid provider quotas for deterministic policy tests.

## 8. Acceptance criteria

- [ ] NOVA owns the architecture and governance of the on-chain administrative validation mechanism as a NOVA component.
- [ ] The external administrator wallet is used for identity/step-up and may receive compensation, but is not the source or custodian of organizational operational funds.
- [ ] Each administrator has a separately identifiable NOVA operations smart account.
- [ ] The operations smart account's mandatory validation cannot be bypassed by an administrator, alternate module, fallback, delegate or ordinary NOVA service.
- [ ] The off-chain policy evaluator and on-chain validator independently check the exact operation and fail closed.
- [ ] A qualifying prohibited attempt by an authenticated, stepped-up administrator is blocked and automatically triggers the full one-violation response, even without an on-chain transaction hash.
- [ ] An unauthenticated third-party probe or benign system error cannot, by itself, be misattributed as an administrator's deliberate attempt.
- [ ] The role, permissions, sessions, delegates and operations account are revoked; the external wallet loses its admin-authenticator association but is not seized.
- [ ] Remaining supported operations-account assets are automatically protected and moved only to the predetermined recovery vault through constrained authority.
- [ ] The User dashboard remains available, the Administrator entry disappears and the standard incident message is displayed.
- [ ] Recovery limitations, unsupported assets and assets already transferred away are handled honestly.
- [ ] Compensation and treasury controls remain separate from administrator role and operations-account authority.
- [ ] Local/offline tests, test-chain adversarial tests, invariants and independent review pass before real assets are deposited.

## 9. Provisional Solana-first architecture and zero-cost test path

Solana is the **preferred provisional blockchain candidate** for AstroCrown, and Solana Devnet is the **preferred first public integration/test network** for the NOVA administrative operations prototype. This is not yet a final production-chain commitment. Mainnet adoption remains blocked pending technical, security, governance, operational, ecosystem, cost and independent-review qualification.

The implementation must use Solana-native concepts. Do not transplant Ethereum ERC-4337 account-abstraction assumptions, EVM module/guard architectures or EVM-specific transaction hooks into the Solana design without a separately justified compatibility layer.

### 9.1 Solana-native account design direction

- Model NOVA enforcement as one or more Solana programs with explicit, separately stored policy/configuration state accounts.
- Use per-administrator program-derived addresses (PDAs) and associated program-controlled vault/state accounts where the reviewed asset model supports them. A PDA is off-curve and has no private key; only the deriving program can authorize it using the runtime's PDA-signing mechanism in a cross-program invocation.
- Give each administrator a separate operations state/vault identity. The external administrator wallet is an explicit transaction signer/authenticator for narrowly scoped NOVA instructions; it is not the direct authority over the organizational assets in the PDA-controlled operations vault.
- Route supported native SOL and SPL-token operations through NOVA instructions. Token-account authority, delegate and close authority, mint/freeze authority, program ID and upgrade authority must be checked against the approved policy.
- Do not claim that NOVA can intercept or block arbitrary transactions from an administrator's ordinary external wallet. The enforceable boundary is NOVA-controlled assets and operations routed through the NOVA program. The owner of an external self-custody wallet retains control of that wallet. AstroCrown cannot technically prevent the person from using that external wallet for unrelated personal activity unless it stops being an ordinary user-controlled wallet; that would be a different custody model.
- Keep administrator identity authentication, payout destination, NOVA operational vault, treasury and recovery vault as distinct purposes and authorization domains, even when an external address is reused for both authentication and compensation receipt.
- Define the program upgrade authority and emergency authority before deployment. Do not leave a single routine administrator or ordinary external wallet with an unrestricted upgrade or treasury key.

### 9.2 Solana transaction atomicity and the one-violation state machine

Solana transactions are atomic: if any instruction fails, all state changes in that transaction are rolled back, although the transaction fee is still charged. Therefore, a NOVA program must **not** rely on writing a revocation/audit record and then returning an error from the same instruction; that record would roll back too.

The incident state machine must provide a separate durable path:
1. The off-chain NOVA gateway records and acts on a prohibited authenticated request rejected before submission; or
2. If a prohibited NOVA instruction is submitted directly and fails on-chain, an independent NOVA monitor observes the confirmed failed transaction and its authenticated signer/program logs, verifies attribution, and submits a separate pre-authorized incident/revocation/recovery transaction; or
3. The program uses a specifically designed successful “violation report/lock” instruction that performs no prohibited asset operation but commits the violation state, after which a separate constrained recovery instruction executes.

The chosen path must be adversarially tested for direct submission, simulation-only/preflight rejection, dropped or unconfirmed transactions, replay, race conditions, monitor downtime and ambiguous attribution. A failed transaction with no attributable authenticated administrator intent is not sufficient to revoke an administrator. Recovery must not be reported as complete until the relevant chain confirms it.

### 9.3 Local and Devnet test sequence

Use a strict $0-first progression:

1. **Offline/local model:** deterministic policy evaluation, state-machine tests and synthetic transaction construction; no RPC and no real credentials.
2. **Local Solana validator or lightweight local execution harness:** repeatable program/account tests with locally funded test accounts. This is the primary place for regression and adversarial cases; do not spend Devnet faucet allocation on tests that can run locally.
3. **Solana Devnet:** public integration checks, program deployment and wallet/transaction testing using disposable Devnet-only keypairs and faucet SOL. Devnet tokens are valueless test assets and the ledger may reset.
4. **Separate test-asset scenarios:** create controlled test mints and accounts for SPL-token/Token-2022 coverage as appropriate. A native SOL faucet does not automatically provision arbitrary SPL tokens.
5. **Mainnet decision gate:** no mainnet deployment, real treasury asset, real salary/bonus payment or real operational funds until program invariants, adversarial tests, independent review, monitoring and recovery drills all pass and the separate chain-selection decision is approved.

### 9.4 Testnet and asset-compatibility qualification

Solana Testnet is a supplemental environment, not a replacement for Devnet. Devnet is the primary public application-development/integration environment. Testnet is primarily used to stress-test Solana releases, network upgrades, validator behavior, performance and stability, and may run a newer software release branch. Use Testnet selectively for runtime/version compatibility and controlled end-to-end smoke/stress tests; do not treat a Testnet pass as proof of Mainnet equivalence.

Different asset compatibility must be tested by program and mint configuration, not by collecting arbitrary faucet tokens. Build a controlled asset matrix for supported classes:
- native SOL;
- classic SPL Token;
- Token-2022 base mints;
- Token-2022 transfer fees, transfer hooks, permanent delegate, default account state/pausable, metadata and confidential transfer (explicitly unsupported until designed and qualified);
- only those NFT/asset standards AstroCrown chooses to support, such as Metaplex Token Metadata, programmable NFTs, compressed NFTs or Metaplex Core.

A token mint and its balances are cluster-specific. A Devnet mint is not automatically present on Testnet. Create a matching controlled test mint and associated accounts separately on each cluster where the corresponding test is required. Maintain a fixture manifest with cluster, mint, owning program, decimals, extensions, authorities and test scenario. Token name, logo, symbol or metadata URI is not proof of identity. NOVA identifies test assets by cluster, owning program, mint address and verified configuration.

Token-2022 extensions can have incompatible combinations, and extension selection must be planned when mint/account state is initialized. The NOVA supported-asset registry must explicitly state accepted programs/extensions and fail closed for unknown mints, programs, extensions, hooks and standards. Review the [official Token Extensions documentation](https://solana.com/docs/tokens/extensions) and [Token Programs guide](https://solana.com/docs/tokens).

Testnet has valueless test tokens, may reset and has a public faucet, but faucet availability, quotas and eligibility may change. Confirm the official live service before requesting assets. Use local controlled fixtures for deterministic tests, Devnet for application integration, and Testnet only for the specific network/version compatibility scenarios that benefit from it. Do not pay for tokens or services to complete this initial test plan.

### 9.5 Faucet and RPC controls

- Primary official sources: [Solana Devnet faucet](https://faucet.solana.com/), [Solana Devnet SOL guide](https://solana.com/developers/cookbook/development/airdrops-and-faucets), [Solana cluster documentation](https://solana.com/docs/references/clusters) and [Solana CLI basics](https://solana.com/docs/intro/installation/solana-cli-basics).
- The CLI can request an airdrop to a disposable Devnet test wallet, for example: `solana airdrop 2 <DEVNET_TEST_ADDRESS> --url devnet`. The currently documented CLI limit is up to 5 SOL per request, subject to RPC/faucet rate limits. Web-faucet limits and verification requirements can change; check the live faucet rather than encoding a permanent quota.
- Confirm the configured cluster and signer before any operation that creates, transfers, authorizes or deploys: inspect `solana config get`, verify the endpoint is Devnet or localhost, and use a separate Devnet-only keypair/configuration. Never reuse or import a mainnet keypair into test scripts.
- The public Devnet RPC is shared and rate-limited; HTTP 429/403, downtime and faucet scarcity must be expected. No production reliability or SLA is implied.
- Do not use paid RPCs, paid relayers, paid faucet upgrades, subscriptions or provider credits for the initial qualification. If public Devnet limits block a test, defer it, use a permitted alternate free faucet or return to local validation; do not incur costs silently.
- Do not store test keypairs, recovery phrases or private keys in Git, PRs, issues, CI logs or screenshots. Create them locally or ephemerally and label them unambiguously as test-only.
- The faucet supplies test SOL, not Mainnet SOL. Testnet/Devnet balances have no monetary value and must never be included in treasury, provider-budget, compensation or revenue calculations.

### 9.6 Solana-specific acceptance additions

- [ ] The first public integration target is Solana Devnet; local/offline tests precede Devnet usage, and Testnet is used selectively for cluster/runtime compatibility.
- [ ] A controlled asset compatibility matrix covers every asset program and extension AstroCrown intends to support; cluster-specific test mints are created separately and unknown assets fail closed.
- [ ] NOVA uses Solana programs, explicit account state, PDAs and CPI authorization as appropriate, rather than an assumed EVM account-abstraction design.
- [ ] All supported operational assets are held under program-controlled authorities; no external administrator wallet can bypass NOVA to move those vault assets.
- [ ] The program validates signer, authority, policy version, account relationships, destination, mint/program, amount and instruction scope before CPI.
- [ ] SPL token owner/delegate/close authority and relevant Token-2022 extensions are explicitly reviewed before support is claimed.
- [ ] A transaction failure cannot be the only incident-recording mechanism because atomic rollback removes state changes; incident recording/revocation/recovery is a separately verified durable path.
- [ ] Test coverage includes Devnet/localhost separation, no accidental Mainnet requests, faucet exhaustion, RPC rate limits, ledger reset and no-cost fallback.
- [ ] No private key, seed phrase, funded Mainnet wallet or production asset is used in Devnet/CI.

## 10. Current status and application boundary

This document is an architecture and governance requirement. It does not claim that NOVA currently performs on-chain transaction validation, creates administrative smart accounts, monitors administrator wallets, automatically freezes accounts or recovers assets.

The related AstroCrown-Web PR #141 currently provides a development-only account foundation: server-owned user/admin roles, permissioned appointment/revocation, external wallet proof-of-control and short-lived step-up. That prototype does not implement this NOVA smart-account subsystem. The application and NOVA runtime must not expose controls or claim that asset protection is active until the implementation stages and acceptance criteria above have actually passed.

No contract deployment, production wallet, organizational asset movement, treasury change or live network operation is authorized by this document.
