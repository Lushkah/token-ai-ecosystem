"""Task models"""

from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum
from sqlalchemy import Text, Float, ForeignKey, Boolean

from src.database import Base


class TaskStatus(str, Enum):
    """Task status enumeration"""
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskType(str, Enum):
    """Task type enumeration"""
    FEATURE = "feature"
    BUG_FIX = "bug_fix"
    OPTIMIZATION = "optimization"
    TESTING = "testing"
    REFACTORING = "refactoring"
    DOCUMENTATION = "documentation"


class Task(Base):
    """Task model"""
    __tablename__ = "tasks"
    
    id = Column(String(36), primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    task_type = Column(SQLEnum(TaskType), nullable=False)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.PENDING, nullable=False, index=True)
    
    # Assignment
    assigned_agent_id = Column(String(36), ForeignKey('agents.id'), nullable=True, index=True)
    
    # Priority and difficulty
    priority = Column(Integer, default=5)  # 1-10 scale
    estimated_difficulty = Column(Float, default=5.0)  # 1-10 scale
    
    # Reward
    base_reward = Column(Float, default=100.0)
    actual_reward = Column(Float, nullable=True)
    reward_multiplier = Column(Float, default=1.0)
    
    # Metrics
    quality_score = Column(Float, nullable=True)  # 0-100
    execution_time_seconds = Column(Integer, nullable=True)
    
    # Results
    result_summary = Column(Text, nullable=True)
    result_details = Column(Text, nullable=True)
    
    # Status tracking
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    assigned_at = Column(DateTime, nullable=True)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
