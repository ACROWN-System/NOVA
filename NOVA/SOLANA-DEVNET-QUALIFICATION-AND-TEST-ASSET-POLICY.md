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

## 9. Acceptance gates

- [ ] Local/offline model passes before any Devnet integration work.
- [ ] Devnet test keypairs are disposable, separated from Mainnet and never committed.
- [ ] Devnet configuration is explicitly verified before every write/deployment command.
- [ ] Faucet airdrops are confirmed and balances checked; no paid service is used.
- [ ] Public RPC limits and faucet failures are handled without paid fallback or uncontrolled retry loops.
- [ ] All required program, PDA, authority and SPL-token invariants pass on local tests and are rechecked on Devnet.
- [ ] Solana atomic rollback is addressed by a separate durable incident and recovery path.
- [ ] Real assets, Mainnet credentials and production treasury remain out of scope until a separate approval and independent security review.
