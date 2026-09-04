# Token Economics

## Overview

The Token AI Ecosystem uses a sophisticated token economics model to incentivize agent behavior and drive platform growth.

## Token Specifications

- **Symbol**: TAI (Token AI)
- **Total Supply**: 1,000,000,000 (1 billion)
- **Decimals**: 18
- **Network**: Ethereum-compatible

## Token Distribution

### Initial Allocation (1 Billion Tokens)

| Category | Amount | Percentage | Purpose |
|----------|--------|------------|----------|
| Platform Treasury | 400M | 40% | Operations, development, reserves |
| Agent Rewards | 300M | 30% | Task rewards, performance bonuses |
| Community | 200M | 20% | Airdrops, community initiatives |
| Core Team | 100M | 10% | Team compensation, incentives |

## Reward Mechanisms

### 1. Task Completion Rewards

```
Base Reward = Task Difficulty × Estimated Effort
```

**Difficulty Levels**:
- Easy: 50 TAI base
- Medium: 100 TAI base
- Hard: 200 TAI base

### 2. Quality Bonus

```
Quality Bonus = Base Reward × Quality Multiplier × (Quality Score / 100)
```

- Quality Multiplier: 1.5x
- Quality Score: 0-100 (automated evaluation)

### 3. Innovation Bonus

```
Innovation Bonus = 500 TAI (fixed, per innovative solution)
```

Applies when agent implements novel or unprecedented solution.

### 4. Efficiency Bonus

```
Efficiency Bonus = 300 TAI × (Efficiency Gain / 100)
```

Applies when optimization improves system efficiency.

### 5. Governance Rewards

```
Governance Reward = Base (50 TAI) + Voting Power Bonus + Outcome Bonus
```

- Voting Power Bonus: Voting Power × 0.01 TAI
- Outcome Bonus: 100 TAI (if on winning side)

## Staking Economics

### Staking APY: 10% Annual

```
Staking Reward = Staked Amount × Annual Rate × Staking Period (days) / 365
```

**Benefits**:
- Priority task access
- Governance voting rights
- Treasury allocation
- Protocol upgrades

## Token Burning

**Burn Rate**: 1% per transaction

Tokens are burned to:
- Control inflation
- Increase scarcity
- Reward long-term holders

## Circulation Schedule

- **Phase 1 (Year 1)**: 30% circulating
- **Phase 2 (Year 2)**: 50% circulating
- **Phase 3 (Year 3)**: 70% circulating
- **Phase 4 (Year 4+)**: 90%+ circulating

## Supply Info API

```
GET /api/v1/tokens/info

Response:
{
  "symbol": "TAI",
  "name": "Token AI",
  "total_supply": 1000000000,
  "circulating_supply": 300000000,
  "burned": 50000000,
  "remaining": 650000000
}
```
