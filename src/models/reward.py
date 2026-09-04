"""Reward models"""

from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum
from sqlalchemy import Float, ForeignKey, Text

from src.database import Base


class RewardType(str, Enum):
    """Reward type enumeration"""
    TASK_COMPLETION = "task_completion"
    QUALITY_BONUS = "quality_bonus"
    INNOVATION_BONUS = "innovation_bonus"
    EFFICIENCY_BONUS = "efficiency_bonus"
    BUG_BOUNTY = "bug_bounty"
    GOVERNANCE = "governance"


class Reward(Base):
    """Reward model"""
    __tablename__ = "rewards"
    
    id = Column(String(36), primary_key=True, index=True)
    agent_id = Column(String(36), ForeignKey('agents.id'), nullable=False, index=True)
    reward_type = Column(SQLEnum(RewardType), nullable=False)
    
    # Amount and multiplier
    base_amount = Column(Float, nullable=False)
    multiplier = Column(Float, default=1.0)
    final_amount = Column(Float, nullable=False)
    
    # Related entities
    task_id = Column(String(36), ForeignKey('tasks.id'), nullable=True, index=True)
    proposal_id = Column(String(36), ForeignKey('proposals.id'), nullable=True, index=True)
    
    # Details
    reason = Column(Text, nullable=True)
    metadata = Column(Text, nullable=True)  # JSON with additional context
    
    # Status
    is_claimed = Column(Integer, default=0)  # Boolean
    claimed_at = Column(DateTime, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
