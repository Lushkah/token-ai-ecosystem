"""Agent models"""

from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, Float, DateTime, Enum as SQLEnum
from sqlalchemy import Boolean, Text, UniqueConstraint

from src.database import Base


class AgentStatus(str, Enum):
    """Agent status enumeration"""
    IDLE = "idle"
    WORKING = "working"
    PAUSED = "paused"
    OFFLINE = "offline"
    ERROR = "error"


class Agent(Base):
    """Agent model"""
    __tablename__ = "agents"
    
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    agent_type = Column(String(50), nullable=False, index=True)  # developer, architect, tester, optimizer
    status = Column(SQLEnum(AgentStatus), default=AgentStatus.IDLE, nullable=False)
    description = Column(Text, nullable=True)
    
    # Performance metrics
    total_tasks_completed = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)
    average_quality_score = Column(Float, default=0.0)
    
    # Token balance
    token_balance = Column(Float, default=0.0)
    
    # Configuration
    enabled = Column(Boolean, default=True)
    max_concurrent_tasks = Column(Integer, default=1)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_activity = Column(DateTime, nullable=True)
    
    __table_args__ = (
        UniqueConstraint('name', name='uq_agent_name'),
    )
