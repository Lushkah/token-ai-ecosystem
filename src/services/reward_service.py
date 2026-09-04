"""Reward service"""

import logging
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.reward import Reward, RewardType
from src.config import settings

logger = logging.getLogger(__name__)


class RewardService:
    """Service for reward operations"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_reward(
        self,
        agent_id: str,
        reward_type: RewardType,
        base_amount: Optional[float] = None,
        multiplier: float = 1.0,
        task_id: Optional[str] = None,
        proposal_id: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> Reward:
        """Create reward for agent"""
        if base_amount is None:
            base_amount = settings.REWARD_BASE_AMOUNT
        
        final_amount = base_amount * multiplier
        
        reward = Reward(
            id=f"reward-{int(__import__('time').time() * 1000)}",
            agent_id=agent_id,
            reward_type=reward_type,
            base_amount=base_amount,
            multiplier=multiplier,
            final_amount=final_amount,
            task_id=task_id,
            proposal_id=proposal_id,
            reason=reason,
        )
        self.db.add(reward)
        await self.db.commit()
        return reward
    
    async def claim_reward(self, reward_id: str) -> Reward:
        """Claim reward"""
        from datetime import datetime
        result = await self.db.execute(
            select(Reward).where(Reward.id == reward_id)
        )
        reward = result.scalar_one_or_none()
        
        if reward:
            reward.is_claimed = 1
            reward.claimed_at = datetime.utcnow()
            await self.db.commit()
        
        return reward
