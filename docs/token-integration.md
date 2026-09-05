# Lushka Token Integration — v0.9

The supplied `LushkaToken(1).sol` is integrated as the current deployment template.

## Contract
- Solidity: `^0.8.24`
- Token: `Lushka (LUSHKA)`
- Standard: OpenZeppelin ERC20
- Permissions: OpenZeppelin AccessControl
- `MINTER_ROLE` controls minting.
- Constructor takes `admin` and `initialSupply`, grants admin/minter roles to `admin`, and mints the initial supply to that address.

## Integrity boundary
This contract remains a deployment template. It is **not deployed to mainnet** by this package. Before any real-money deployment, review tokenomics, supply/mint policy, administrative key security, and obtain an independent smart-contract security audit and legal review.

Use the published OpenZeppelin package rather than copying/modifying OpenZeppelin library internals.
