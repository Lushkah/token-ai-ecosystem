"""Task queue and scheduler"""

import logging
from typing import Dict, Any, List, Optional, Callable
from datetime import datetime
from enum import Enum
import asyncio

logger = logging.getLogger(__name__)


class TaskPriority(Enum):
    """Task priority levels"""
    LOW = 1
    MEDIUM = 5
    HIGH = 10


class TaskScheduler:
    """Task queue and scheduler for agent assignments"""
    
    def __init__(self):
        self.task_queue: List[Dict[str, Any]] = []
        self.active_tasks: Dict[str, Dict[str, Any]] = {}
        self.completed_tasks: List[Dict[str, Any]] = []
        self.callbacks: List[Callable] = []
    
    async def enqueue_task(
        self,
        task_id: str,
        task_type: str,
        description: str,
        priority: int = 5,
        estimated_difficulty: float = 5.0,
        base_reward: float = 100.0,
    ) -> Dict[str, Any]:
        """Enqueue a task for execution"""
        task = {
            "id": task_id,
            "type": task_type,
            "description": description,
            "priority": priority,
            "estimated_difficulty": estimated_difficulty,
            "base_reward": base_reward,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat(),
            "assigned_agent_id": None,
            "retry_count": 0,
            "max_retries": 3,
        }
        
        self.task_queue.append(task)
        # Sort by priority (highest first)
        self.task_queue.sort(key=lambda x: x["priority"], reverse=True)
        
        logger.info(f"Task enqueued: {task_id}")
        return task
    
    async def get_next_task(self) -> Optional[Dict[str, Any]]:
        """Get the next task from queue"""
        if not self.task_queue:
            return None
        
        task = self.task_queue.pop(0)
        task["status"] = "assigned"
        return task
    
    async def assign_task(
        self,
        task_id: str,
        agent_id: str,
    ) -> Dict[str, Any]:
        """Assign task to agent"""
        task = None
        for t in self.task_queue:
            if t["id"] == task_id:
                task = t
                break
        
        if not task:
            raise ValueError(f"Task {task_id} not found")
        
        task["assigned_agent_id"] = agent_id
        task["status"] = "assigned"
        task["assigned_at"] = datetime.utcnow().isoformat()
        
        self.task_queue.remove(task)
        self.active_tasks[task_id] = task
        
        logger.info(f"Task {task_id} assigned to agent {agent_id}")
        return task
    
    async def complete_task(
        self,
        task_id: str,
        result: Dict[str, Any],
        quality_score: float = 50.0,
    ) -> Dict[str, Any]:
        """Mark task as completed"""
        if task_id not in self.active_tasks:
            raise ValueError(f"Task {task_id} not active")
        
        task = self.active_tasks.pop(task_id)
        task["status"] = "completed"
        task["completed_at"] = datetime.utcnow().isoformat()
        task["result"] = result
        task["quality_score"] = quality_score
        
        self.completed_tasks.append(task)
        
        # Trigger callbacks
        for callback in self.callbacks:
            await callback(task)
        
        logger.info(f"Task {task_id} completed")
        return task
    
    async def fail_task(
        self,
        task_id: str,
        error: str,
    ) -> Dict[str, Any]:
        """Mark task as failed"""
        if task_id not in self.active_tasks:
            raise ValueError(f"Task {task_id} not active")
        
        task = self.active_tasks[task_id]
        task["retry_count"] += 1
        
        if task["retry_count"] >= task["max_retries"]:
            task["status"] = "failed"
            self.active_tasks.pop(task_id)
        else:
            task["status"] = "pending"
            # Re-enqueue
            self.task_queue.append(task)
            self.active_tasks.pop(task_id)
        
        task["error"] = error
        task["failed_at"] = datetime.utcnow().isoformat()
        
        logger.warning(f"Task {task_id} failed: {error}")
        return task
    
    def get_queue_status(self) -> Dict[str, Any]:
        """Get current queue status"""
        return {
            "pending_tasks": len(self.task_queue),
            "active_tasks": len(self.active_tasks),
            "completed_tasks": len(self.completed_tasks),
            "total_tasks": len(self.task_queue) + len(self.active_tasks) + len(self.completed_tasks),
        }
