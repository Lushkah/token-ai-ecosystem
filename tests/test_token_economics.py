"""Token economics tests"""

import pytest
from src.token_system.economics import TokenEconomics


def test_calculate_task_reward_basic():
    """Test basic task reward calculation"""
    economics = TokenEconomics()
    
    reward = economics.calculate_task_reward(
        base_amount=100.0,
        quality_score=80.0,
        is_innovation=False,
        efficiency_gain=0.0,
    )
    
    assert "total_reward" in reward
    assert reward["base_reward"] == 100.0
    assert reward["quality_bonus"] > 0


def test_calculate_task_reward_with_innovation():
    """Test task reward with innovation bonus"""
    economics = TokenEconomics()
    
    reward = economics.calculate_task_reward(
        base_amount=100.0,
        quality_score=90.0,
        is_innovation=True,
        efficiency_gain=20.0,
    )
    
    assert reward["innovation_bonus"] > 0
    assert reward["efficiency_bonus"] > 0
    assert reward["total_reward"] > reward["base_reward"]


def test_calculate_governance_reward():
    """Test governance reward calculation"""
    economics = TokenEconomics()
    
    reward = economics.calculate_governance_reward(
        voting_power=1000.0,
        proposal_outcome="passed",
    )
    
    assert reward > 0


def test_calculate_stake_reward():
    """Test staking reward calculation"""
    economics = TokenEconomics()
    
    reward = economics.calculate_stake_reward(
        staked_amount=1000.0,
        staking_period_days=365,
    )
    
    assert reward > 0


def test_distribute_treasury():
    """Test treasury allocation distribution"""
    economics = TokenEconomics()
    
    allocation = economics.distribute_treasury_allocation(1_000_000.0)
    
    assert allocation["platform_treasury"] == 400_000.0
    assert allocation["agent_rewards"] == 300_000.0
    assert allocation["community"] == 200_000.0
    assert allocation["core_team"] == 100_000.0
