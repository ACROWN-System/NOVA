# Solana Devnet Qualification and Test-Asset Policy

**Document ID:** NOVA-DEV-SOL-001  
**Date:** 2026-11-02  
**Status:** PROVISIONAL DEVELOPMENT DIRECTION — $0-FIRST / DOCUMENTATION ONLY  
**Initial application:** AstroCrown and the NOVA administrative operations subsystem  
**Related architecture:** [NOVA Administrative Smart-Account Security Architecture](ADMINISTRATIVE-SMART-ACCOUNT-SECURITY-ARCHITECTURE.md)

## 1. Decision and scope

Solana is the preferred provisional blockchain candidate for AstroCrown. Solana Devnet is the preferred first public integration network for NOVA and AstroCrown program development. This does not yet authorize a final Mainnet selection, token deployment, production contract or real asset operation.

The objective is to qualify the Solana account/program model and the NOVA administrative security controls without spending money on blockchain test tokens, paid RPC services, paid faucets, paid relayers or provider credits.

The word **zero-cost** applies to the test SOL supplied by faucets and to the initial use of free/local development facilities. It does not mean that engineering labor, local compute, connectivity, or every future production service has no cost. Any later non-zero expenditure requires a separate explicit decision.

## 2. Network order

### Stage A — Offline deterministic model

Start with tests that require no blockchain network:
- policy evaluation and canonical operation encoding;
- administrator role/permission and session binding;
- transaction allow/deny decision cases;
- one-violation incident state transitions;
- recovery-vault destination invariants;
- replay, stale policy, unknown operation and false-attribution tests;
- audit event creation and consistency.

Use synthetic accounts, generated test data and fake transaction descriptions. Do not use secrets, funded real wallets or paid AI/provider calls.

### Stage B — Local Solana execution

Run a local validator or an appropriate lightweight Solana program test harness to test the program and account model repeatedly. Create locally funded test accounts, controlled native/token assets, PDAs and vaults. Local execution is the default for deterministic regression and adversarial tests.

Local test balances are artificial and have no value. Local tests must verify that the application never confuses localhost with Devnet or Mainnet.

### Stage C — Solana Devnet integration

Use Devnet only for integration tests that genuinely require the shared public cluster:
- deploy a test version of the NOVA program;
- verify program/account derivation and PDA authority;
- exercise signed instructions using disposable wallets;
- request test SOL from the free faucet or CLI airdrop;
- test native SOL and controlled SPL-token test mints;
- inspect transactions and events in a Devnet-aware explorer;
- test policy rejection, account lock, revocation and constrained recovery;
- verify how the separate incident-response path behaves after a failed transaction; and
- record RPC errors, faucet rate limits, transaction signatures and confirmation outcomes.

Devnet is not a durability environment. Its ledger can be reset; Devnet balances and test accounts must be treated as disposable.

### Stage D — Separate production-chain decision

Only after implementation and independent security review should AstroCrown decide whether Solana is the production chain. The final decision must consider security model, program/account design, upgrades and authority management, ecosystem dependencies, supported assets, interoperability, RPC costs/reliability, monitoring, recovery, audit evidence, legal obligations and long-term maintenance.

No production asset, treasury funds, real compensation payment or Mainnet deployment is authorized by this plan.

## 3. Devnet SOL acquisition

Use official Solana sources first:

- [Solana Devnet faucet](https://faucet.solana.com/)
- [Solana guide to Devnet SOL, airdrops and faucets](https://solana.com/developers/cookbook/development/airdrops-and-faucets)
- [Solana clusters and public RPC endpoints](https://solana.com/docs/references/clusters)
- [Solana CLI basics](https://solana.com/docs/intro/installation/solana-cli-basics)
- [Solana Devnet Explorer](https://explorer.solana.com/?cluster=devnet)

Example CLI sequence for requesting Devnet SOL to a disposable test address:

    solana config set --url devnet
    solana config get
    solana airdrop 2 DEVNET_TEST_ADDRESS --url devnet
    solana balance DEVNET_TEST_ADDRESS --url devnet

The Solana CLI documentation currently describes a maximum of 5 SOL per Devnet airdrop request. Requests may be rate-limited by the RPC/faucet. The public web faucet currently displays a limit of two requests every eight hours, with additional access potentially subject to GitHub account verification. These are operational snapshots, not permanent guarantees; always check the live official faucet and CLI output.

The Devnet faucet/CLI delivers **test SOL**, not Mainnet SOL. It has no market value, cannot pay Mainnet fees and must never appear as revenue, treasury balance, compensation, collateral or an AstroCrown token reserve.

The native SOL faucet does not automatically provide arbitrary SPL tokens. For token-program tests, prefer creating controlled test mints and test token accounts under the project test procedure. Any third-party faucet for a particular token must be independently checked for authenticity, availability and asset identity; never assume a Devnet token represents the corresponding Mainnet asset.

## 4. Key and network separation

- Generate a disposable Devnet-only test keypair in a protected local environment or isolated CI test context.
- Do not use an administrator's personal wallet, compensation wallet, production wallet or Mainnet keypair for Devnet testing.
- Never upload or commit keypair files, seed phrases, private keys or signing secrets to GitHub, issue comments, PRs, CI logs, artifacts, screenshots or chat.
- Keep Devnet key material separate from any Mainnet key material at the filesystem, configuration and process level.
- Before every operation that creates, deploys, transfers, authorizes or changes accounts/programs, inspect the effective CLI configuration and confirm the cluster and signer. Use explicit Devnet or localhost options rather than relying on remembered defaults.
- Do not use a web wallet connected to Mainnet for an operation intended for Devnet. Verify the selected cluster and receiving address in the wallet UI before approving any signature or transaction.
- Keep test signers minimally funded. Do not accumulate or reuse a faucet wallet as a production credential.

## 5. $0-first RPC and faucet rules

- Use local validation before requesting Devnet SOL. Do not spend faucet requests on deterministic tests that need no public chain.
- Use the official public Devnet RPC only for modest integration workloads. It is shared and rate-limited; 429, 403, intermittent availability and congestion are expected possibilities.
- Do not set up a paid RPC account, paid faucet tier, paid relayer, paid transaction service, paid deployment platform or subscription for this first qualification.
- If the public faucet or RPC is exhausted/unavailable, pause Devnet-only tests, use a permitted alternative free faucet if independently qualified, or return to local execution. Do not silently switch to Mainnet or an unapproved paid service.
- Record only the amount actually received and transaction signature. Do not assume an airdrop succeeded until the transaction is confirmed and the balance is verified.
- Avoid loops that repeatedly request airdrops or retry RPC requests without bounded backoff. Respect current public service limits.
- Keep the test asset ledger isolated from NOVA's provider-budget accounting; test SOL is not an external model/provider quota.

## 6. Solana-native NOVA implementation constraints

- Use Solana programs, instructions, transactions, explicit state accounts, PDAs and CPIs as appropriate. Do not assume EVM contracts, ERC-4337, EVM fallback handlers, generic EVM modules or EVM transaction hooks are available.
- A PDA has no private key. The program that derives it may authorize it through the runtime's PDA-signing mechanism in a CPI.
- Keep mutable policy/account state in explicitly defined accounts and validate program IDs, owners, signers, PDAs, account relationships, token mints, token-account owner/delegate/close-authority fields, amounts and operation scope.
- The NOVA program must be the mandatory authority path for assets in NOVA-controlled operational vaults. An administrator's external identity wallet must not independently control those assets.
- Do not claim NOVA can block arbitrary personal transactions signed directly by the owner of an ordinary external wallet. NOVA can enforce rules over NOVA-controlled assets and transactions routed through the NOVA program. The external wallet owner retains control of that wallet.
- SPL Token and Token-2022 support must be scoped by mint and extension; do not accept arbitrary token programs or token account configurations without review.
- Program upgrade authority is a critical security boundary. Decide its governance, threshold, key isolation, recovery and revocation model before any Devnet program is treated as a meaningful security prototype.

## 7. Solana atomicity and incident evidence

A Solana transaction is atomic: if one instruction fails, all state changes in the transaction are rolled back, although the transaction fee is still charged. NOVA must therefore not attempt to store a permanent incident/revocation record in an instruction and then return an error in that same transaction, expecting the record to survive.

The one-violation response needs a separately committed path:
- the off-chain NOVA gateway records and responds to an authenticated prohibited request before submitting it; or
- an independently operating NOVA monitor observes a confirmed failed program invocation, checks signer and logs, validates attribution and submits a separate pre-authorized incident/revocation/recovery transaction; or
- NOVA implements a deliberately designed successful violation-report/lock instruction which records the violation without performing the prohibited asset operation, followed by a separate constrained recovery operation.

Tests must cover direct program submission, off-chain simulation/preflight rejection, transactions that never land, dropped/expired transactions, failed instruction rollback, replay, races, monitor/RPC outage and ambiguous attribution. A transaction failure alone is not evidence of administrator misconduct. NOVA must not revoke a person based only on an unauthenticated probe, transport error or unrelated program failure.

## 8. Required evidence and status reporting

The qualification record must identify:
- local tool versions and exact program build/revision;
- cluster and RPC endpoint (localhost vs Devnet);
- test-wallet public addresses only;
- faucet request outcome and confirmed amount;
- program IDs and PDA derivation inputs where safe to disclose;
- transaction signatures and confirmation commitments;
- test cases and results;
- policy decisions and incident attribution evidence;
- failure modes and unresolved findings; and
- whether each finding is local-only, Devnet-confirmed or independently reviewed.

Do not include private keys, seed phrases, passwords, secret RPC URLs, access tokens or sensitive incident data.


## 10. Testnet: supplemental network and release-compatibility stage

Solana Testnet should be included as a **supplemental, targeted qualification environment**, not as the primary application-development environment.

Solana's documented cluster purposes are different:
- **Devnet** is the recommended public environment for application developers, token holders and program integration.
- **Testnet** is primarily where Solana core contributors stress-test release candidates, network upgrades, performance, stability and validator behavior. It may run a newer software release branch than Devnet and Mainnet.
- **Local validator** remains the best place for repeatable application and adversarial regression tests.
- **Mainnet** remains production and is not part of the $0 test workflow.

Accordingly, use Testnet later in the qualification sequence to catch cluster/runtime/version-specific compatibility issues and to run controlled end-to-end smoke/stress tests where the test depends on the shared Testnet environment. Do not duplicate every Devnet test on Testnet by default, and do not interpret a Testnet pass as proof of Mainnet equivalence.

The official Testnet RPC is shared and may experience intermittent downtime. A Testnet faucet is documented, but its current limits, availability and eligibility must be checked live. Do not assume that every Testnet test asset is available from a faucet or that its limits match Devnet. If the faucet is unavailable, create controlled test mints where permitted or defer that test; do not use a paid source or Mainnet asset.

Official cluster-purpose reference: [Solana clusters and public RPC endpoints](https://solana.com/docs/references/clusters). Official Testnet endpoint: `https://api.testnet.solana.com`.

## 11. Asset compatibility matrix — create controlled mints rather than chase faucets

The main asset-compatibility objective is to test how NOVA parses, validates, monitors and authorizes **different asset programs and mint configurations**. Acquiring random faucet tokens is not a substitute for this testing.

A token mint created on Devnet does not automatically exist on Testnet or Mainnet. Each cluster has a separate ledger. For reproducible tests, create a controlled fixture mint and token accounts separately on Localnet, Devnet and (only for selected tests) Testnet. Record a fixture manifest that identifies cluster, token program, mint address, decimals, extension set, authorities, test scenario and build/version. Never assume the same symbol/name or mint address implies the same asset on another cluster.

At minimum, qualify the following asset classes where the project plans to support them:

| Asset class | Required test cases |
|---|---|
| Native SOL | Balance/transfer, account funding, rent/required account allocation, insufficient funds, fee-payer separation |
| Classic SPL Token | Mint and token-account identification, transfer, decimals, freeze/mint authority, owner/delegate, close authority and rejection of unsupported instructions |
| Token-2022 basic mint | Program-ID identification, mint/account parsing and transfer with no optional extensions |
| Token-2022 transfer fee | Fee calculation/withheld amounts, fee authority and gross-versus-net transfer accounting |
| Token-2022 transfer hook | Required extra accounts, CPI invocation, hook program allowlisting, hook failure and malicious/unapproved hook rejection |
| Token-2022 permanent delegate | Detection and policy treatment of authority that may transfer/burn tokens beyond ordinary owner/delegate expectations |
| Token-2022 default account state / pausable | Frozen/paused behavior, authority changes and fail-closed handling |
| Token-2022 metadata / metadata pointer | Correct mint binding and treating names/symbols/URIs as untrusted descriptive metadata rather than asset identity |
| Token-2022 confidential transfer | Explicit support decision; reject by default until confidentiality-aware balance, validation, monitoring and compliance behavior is independently designed and tested |
| NFTs and other asset standards | Test only standards that AstroCrown explicitly chooses to support (for example, Metaplex Token Metadata, programmable NFTs, compressed NFTs or Metaplex Core); validate their owning program, authority and transfer path separately |

This matrix is a scope proposal, not a claim that all listed types are supported. The supported asset policy must be explicit. An unrecognized program ID, mint, extension, hook or asset standard must be rejected by default until it has an approved test profile.

Token-2022 extensions are optional features and some extension combinations are incompatible. Extension selection often has to be made at mint/account initialization; it cannot safely be assumed that missing capabilities can be added later. Consult the [official Token Extensions documentation](https://solana.com/docs/tokens/extensions) and [official Token Programs guide](https://solana.com/docs/tokens) when building fixture profiles.

For each supported asset profile, test:
- correct parsing of mint and token-account data;
- owner, delegate, close authority, freeze authority, mint authority, permanent delegate, transfer-fee authority, transfer-hook program and other relevant authorities;
- exact amount/decimal handling without floating-point loss;
- transfer simulation and execution, including fee/gross/net effects;
- program/extension compatibility and required accounts;
- allowlisted and denied destinations;
- unsupported extension and malicious hook behavior;
- monitoring and incident attribution; and
- recovery/asset accounting limitations.

Do not treat a token ticker, displayed name, logo, metadata URI or faucet label as proof of authenticity. Identify an asset by its cluster, owning program and mint/asset address, plus the exact configuration and authorities that NOVA has qualified.

### Asset-fixture funding rules

- Local validator: use controlled local airdrops and mint fixtures; no public faucet is required for deterministic tests.
- Devnet: use faucet SOL for transaction fees and native-SOL cases; create controlled SPL/Token-2022 test mints for token cases. Use third-party asset faucets only after verifying the exact mint and test purpose.
- Testnet: use its current official faucet only for test SOL when it is available. Create controlled token fixtures on Testnet if the test requires that cluster; do not assume Devnet mints or tokens are replicated there.
- All faucet assets are valueless, cluster-specific test data. They are never reserves, collateral, compensation, project revenue or live token holdings.

## 12. Acceptance gates

- [ ] Local/offline model passes before any Devnet integration work.
- [ ] Devnet and Testnet keypairs are disposable, separated from Mainnet and never committed.
- [ ] Devnet is used for application integration; Testnet is used selectively for network/release compatibility, not as a substitute for Devnet.
- [ ] Controlled test mints are created separately on each cluster for the asset profiles being qualified; no cross-cluster mint equivalence is assumed.
- [ ] Unknown token programs, mints, Token-2022 extensions, hooks and asset standards fail closed unless an explicit support profile has passed tests.
- [ ] Devnet configuration is explicitly verified before every write/deployment command.
- [ ] Faucet airdrops are confirmed and balances checked; no paid service is used.
- [ ] Public RPC limits and faucet failures are handled without paid fallback or uncontrolled retry loops.
- [ ] All required program, PDA, authority and SPL-token invariants pass on local tests and are rechecked on Devnet.
- [ ] Solana atomic rollback is addressed by a separate durable incident and recovery path.
- [ ] Real assets, Mainnet credentials and production treasury remain out of scope until a separate approval and independent security review.
