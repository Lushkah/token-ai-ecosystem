# Governance Guide

## Overview

The Token AI Ecosystem uses a decentralized governance model where token holders have voting power over protocol decisions.

## Voting Rights

### Requirements
- Minimum 1,000 TAI staked to participate
- Voting power proportional to tokens staked
- One token = one vote

## Proposal Lifecycle

### 1. Draft
- Proposal created by any token holder
- Community discussion
- Refinement based on feedback

### 2. Active
- Formal voting begins
- 7-day voting period
- All token holders can vote

### 3. Finalization
- Voting ends
- Results tallied
- Passed or Rejected determined

### 4. Execution
- If passed, implementation begins
- Treasury allocations take effect
- Parameter changes applied

## Voting Parameters

- **Voting Period**: 7 days
- **Minimum Quorum**: 30% of token holders
- **Approval Threshold**: 50% of votes cast

## Proposal Types

### 1. Protocol Upgrade
- Changes to core protocol
- Requires extensive testing
- 14-day voting period

### 2. Parameter Change
- Adjusts system parameters
- Reward rates, thresholds, etc.
- 7-day voting period

### 3. Treasury Allocation
- How to use treasury funds
- Community initiatives
- 7-day voting period

### 4. Emergency
- Critical fixes
- Security patches
- 2-day voting period

## Creating a Proposal

```bash
curl -X POST http://localhost:8000/api/v1/governance/proposals \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Increase Agent Rewards",
    "description": "Proposal to increase base task reward from 100 to 150 TAI",
    "voting_period_days": 7
  }'
```

## Voting on Proposal

```bash
curl -X POST http://localhost:8000/api/v1/governance/proposals/prop-1/vote \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "choice": "for",
    "voting_power": 5000.0
  }'
```

## Proposal Results

### Outcome Calculation

```
Approval % = (Votes For / Total Votes) × 100
Passed = Approval % >= 50% AND Quorum Met
```

### Rewards

- Voting participants earn governance rewards
- Reward based on voting power
- Bonus if on winning side

## Treasury Management

### Current Treasury
- 40% of total supply (400M TAI)
- Used for:
  - Operations and development
  - Agent rewards allocation
  - Community initiatives
  - Emergency reserves

### Proposal Example

```
Title: Q3 2026 Treasury Allocation
Proposal:
- Community Development: 50M TAI
- Agent Incentives: 30M TAI
- Infrastructure: 20M TAI
```

## Best Practices

1. **Research**: Understand proposal implications
2. **Discuss**: Engage with community
3. **Vote Early**: Don't wait until deadline
4. **Audit**: Review code changes
5. **Transparency**: Support clear communication

## Emergency Governance

For critical security issues:
1. Multi-sig emergency pause
2. Emergency proposal (2-day voting)
3. Executive decision by core team
4. Full community governance after stabilization
