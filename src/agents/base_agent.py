"""Base agent class"""

import logging
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, agent_id: str, name: str, agent_type: str):
        self.agent_id = agent_id
        self.name = name
        self.agent_type = agent_type
        self.status = "idle"
        self.current_task = None
        self.token_balance = 0.0
        self.success_rate = 0.0
        self.total_tasks_completed = 0
        self.average_quality_score = 0.0
    
    @abstractmethod
    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task and return result"""
        pass
    
    @abstractmethod
    async def evaluate_task(self, task: Dict[str, Any]) -> float:
        """Evaluate task quality (0-100)"""
        pass
    
    async def start_task(self, task: Dict[str, Any]) -> None:
        """Start executing a task"""
        self.status = "working"
        self.current_task = task
        logger.info(f"Agent {self.name} started task {task.get('id')}")
    
    async def complete_task(self, result: Dict[str, Any]) -> None:
        """Complete a task"""
        self.status = "idle"
        self.current_task = None
        self.total_tasks_completed += 1
        logger.info(f"Agent {self.name} completed task")
    
    async def pause(self) -> None:
        """Pause agent"""
        self.status = "paused"
        logger.info(f"Agent {self.name} paused")
    
    async def resume(self) -> None:
        """Resume agent"""
        self.status = "idle"
        logger.info(f"Agent {self.name} resumed")
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "type": self.agent_type,
            "status": self.status,
            "token_balance": self.token_balance,
            "tasks_completed": self.total_tasks_completed,
            "success_rate": self.success_rate,
            "quality_score": self.average_quality_score,
        }
