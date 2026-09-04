# LUSHKA Puzzle Mining

LUSHKA can include a permissionless puzzle-mining layer without secretly increasing the token supply.

## Design

- The Lushka ERC-20 remains fixed at 1,000,000,000 tokens.
- A separate `LushkaPuzzleMining` contract holds a pre-funded mining allocation.
- Each round publishes a cryptographic challenge and difficulty.
- Participants search a large word space (for example, a one-million-word candidate set) plus a nonce.
- The contract verifies the final proof with `keccak256` and pays the fixed reward to the first valid solution from each wallet per round.
- Mining rewards are transfers from the funded pool; the mining contract cannot mint new LUSHKA.

## Fairness and anti-whale protection

The system should protect participants with objective, published rules rather than judging people by wealth or identity. Recommended ecosystem protections include:

1. Fixed mining allocation and fixed reward schedule.
2. Public round challenges and on-chain verification.
3. One successful solution per address per round.
4. Transparent maximum wallet/transaction limits only if governance later adopts them, with documented exceptions for liquidity and protocol contracts.
5. AI monitoring for abnormal claim patterns, Sybil clusters, exploit attempts, wash activity, and contract anomalies.
6. AI may recommend pausing a round or changing parameters, but it must not secretly confiscate funds or discriminate against users.
7. Any emergency pause or parameter change should be controlled by explicit, auditable governance or a narrowly scoped security role.

## Important limitation

A one-million-word dictionary should not be stored directly in Ethereum contract storage; that would be unnecessarily expensive. The client/miner can hold the candidate list, while the chain verifies the cryptographic result. For stronger censorship resistance, publish the exact word-list version and a Merkle root/IPFS CID for each puzzle epoch.

## Launch sequence

1. Deploy `LushkaToken` on Sepolia.
2. Deploy `LushkaPuzzleMining` with the token address.
3. Transfer a defined mining allocation from the treasury to the mining contract.
4. Start a test round and publish the challenge, difficulty, word-list version, and reward.
5. Test independent miners and verify that invalid proofs fail.
6. Audit both contracts before mainnet deployment.
7. Only then deploy on Ethereum mainnet and fund the mining pool with a publicly documented allocation.
