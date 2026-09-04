"""Token economics engine"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

from src.config import settings

logger = logging.getLogger(__name__)


class TokenEconomics:
    """Token economics engine for reward distribution and incentives"""
    
    def __init__(self):
        self.total_supply = settings.TOKEN_TOTAL_SUPPLY
        self.circulating_supply = 0.0
        self.burned = 0.0
        self.base_reward = settings.REWARD_BASE_AMOUNT
        self.quality_multiplier = settings.REWARD_QUALITY_MULTIPLIER
        self.innovation_bonus = settings.REWARD_INNOVATION_BONUS
        self.efficiency_bonus = settings.REWARD_EFFICIENCY_BONUS
    
    def calculate_task_reward(
        self,
        base_amount: Optional[float] = None,
        quality_score: float = 50.0,
        is_innovation: bool = False,
        efficiency_gain: float = 0.0,
    ) -> Dict[str, float]:
        """Calculate reward for completed task"""
        if base_amount is None:
            base_amount = self.base_reward
        
        # Calculate components
        base_reward = base_amount
        quality_bonus = 0.0
        innovation_bonus = 0.0
        efficiency_bonus = 0.0
        
        # Quality bonus (scales with quality score)
        if quality_score >= 50:
            quality_bonus = base_reward * self.quality_multiplier * (quality_score / 100.0)
        
        # Innovation bonus
        if is_innovation:
            innovation_bonus = self.innovation_bonus
        
        # Efficiency bonus (scales with efficiency gain)
        if efficiency_gain > 0:
            efficiency_bonus = self.efficiency_bonus * (efficiency_gain / 100.0)
        
        # Total reward
        total_reward = base_reward + quality_bonus + innovation_bonus + efficiency_bonus
        
        return {
            "base_reward": base_reward,
            "quality_bonus": quality_bonus,
            "innovation_bonus": innovation_bonus,
            "efficiency_bonus": efficiency_bonus,
            "total_reward": total_reward,
        }
    
    def calculate_governance_reward(
        self,
        voting_power: float,
        proposal_outcome: str,  # "passed", "rejected", "abstained"
    ) -> float:
        """Calculate reward for governance participation"""
        base_reward = 50.0  # Base governance reward
        
        # Reward for voting with significant power
        power_bonus = voting_power * 0.01
        
        # Bonus if on winning side
        outcome_bonus = 0.0
        if proposal_outcome == "passed":
            outcome_bonus = 100.0
        elif proposal_outcome == "rejected":
            outcome_bonus = 50.0
        
        total_reward = base_reward + power_bonus + outcome_bonus
        return total_reward
    
    def calculate_stake_reward(
        self,
        staked_amount: float,
        staking_period_days: int,
    ) -> float:
        """Calculate reward for token staking"""
        # Annual percentage yield (APY) of 10%
        annual_rate = 0.10
        daily_rate = annual_rate / 365.0
        
        staking_reward = staked_amount * daily_rate * staking_period_days
        return staking_reward
    
    def distribute_treasury_allocation(
        self,
        total_tokens: float,
    ) -> Dict[str, float]:
        """Distribute treasury allocation"""
        return {
            "platform_treasury": total_tokens * 0.40,
            "agent_rewards": total_tokens * 0.30,
            "community": total_tokens * 0.20,
            "core_team": total_tokens * 0.10,
        }
    
    def calculate_burn_amount(
        self,
        transaction_amount: float,
        burn_rate: float = 0.01,  # 1%
    ) -> float:
        """Calculate token burn amount"""
        return transaction_amount * burn_rate
    
    def get_supply_info(self) -> Dict[str, Any]:
        """Get token supply information"""
        return {
            "total_supply": self.total_supply,
            "circulating_supply": self.circulating_supply,
            "burned": self.burned,
            "remaining": self.total_supply - self.circulating_supply - self.burned,
            "timestamp": datetime.utcnow().isoformat(),
        }
