"""Token and transaction models"""

from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum
from sqlalchemy import Float, ForeignKey, Text

from src.database import Base


class TransactionType(str, Enum):
    """Transaction type enumeration"""
    REWARD = "reward"
    STAKE = "stake"
    UNSTAKE = "unstake"
    TRANSFER = "transfer"
    BURN = "burn"
    MINT = "mint"
    GOVERNANCE_VOTE = "governance_vote"


class Token(Base):
    """Token model"""
    __tablename__ = "tokens"
    
    id = Column(String(36), primary_key=True, index=True)
    symbol = Column(String(10), default="TAI", nullable=False)
    name = Column(String(255), default="Token AI", nullable=False)
    
    # Supply
    total_supply = Column(Float, default=1_000_000_000.0)
    circulating_supply = Column(Float, default=0.0)
    burned = Column(Float, default=0.0)
    
    # Decimals
    decimals = Column(Integer, default=18)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TokenTransaction(Base):
    """Token transaction model"""
    __tablename__ = "token_transactions"
    
    id = Column(String(36), primary_key=True, index=True)
    transaction_type = Column(SQLEnum(TransactionType), nullable=False, index=True)
    
    # Participants
    from_address = Column(String(255), nullable=True, index=True)  # Can be system
    to_address = Column(String(255), nullable=False, index=True)
    
    # Amount
    amount = Column(Float, nullable=False)
    
    # Related entities
    agent_id = Column(String(36), ForeignKey('agents.id'), nullable=True, index=True)
    task_id = Column(String(36), ForeignKey('tasks.id'), nullable=True, index=True)
    
    # Details
    description = Column(Text, nullable=True)
    metadata = Column(Text, nullable=True)  # JSON
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
