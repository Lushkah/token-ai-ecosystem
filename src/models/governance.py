"""Governance models"""

from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum
from sqlalchemy import Float, ForeignKey, Text, Boolean

from src.database import Base


class ProposalStatus(str, Enum):
    """Proposal status enumeration"""
    DRAFT = "draft"
    ACTIVE = "active"
    PASSED = "passed"
    REJECTED = "rejected"
    EXECUTED = "executed"
    CANCELLED = "cancelled"


class VoteChoice(str, Enum):
    """Vote choice enumeration"""
    FOR = "for"
    AGAINST = "against"
    ABSTAIN = "abstain"


class Proposal(Base):
    """Governance proposal model"""
    __tablename__ = "proposals"
    
    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    status = Column(SQLEnum(ProposalStatus), default=ProposalStatus.DRAFT, nullable=False)
    
    # Creator
    creator_id = Column(String(36), nullable=False, index=True)  # Agent or User ID
    
    # Voting
    votes_for = Column(Float, default=0.0)
    votes_against = Column(Float, default=0.0)
    votes_abstain = Column(Float, default=0.0)
    total_votes = Column(Float, default=0.0)
    
    # Thresholds
    quorum_percentage = Column(Float, default=30.0)
    approval_percentage = Column(Float, default=50.0)
    
    # Configuration
    voting_starts_at = Column(DateTime, nullable=False)
    voting_ends_at = Column(DateTime, nullable=False)
    
    # Execution
    executed = Column(Boolean, default=False)
    executed_at = Column(DateTime, nullable=True)
    execution_result = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Vote(Base):
    """Vote model"""
    __tablename__ = "votes"
    
    id = Column(String(36), primary_key=True, index=True)
    proposal_id = Column(String(36), ForeignKey('proposals.id'), nullable=False, index=True)
    voter_id = Column(String(36), nullable=False, index=True)  # Agent or User ID
    choice = Column(SQLEnum(VoteChoice), nullable=False)
    
    # Voting power
    voting_power = Column(Float, nullable=False)  # Tokens staked
    
    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
