"""Task service"""

import logging
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.task import Task, TaskStatus

logger = logging.getLogger(__name__)


class TaskService:
    """Service for task operations"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def list_tasks(self) -> List[Task]:
        """List all tasks"""
        result = await self.db.execute(select(Task))
        return result.scalars().all()
    
    async def get_task(self, task_id: str) -> Optional[Task]:
        """Get task by ID"""
        result = await self.db.execute(
            select(Task).where(Task.id == task_id)
        )
        return result.scalar_one_or_none()
    
    async def create_task(self, task_data: dict) -> Task:
        """Create new task"""
        task = Task(**task_data)
        self.db.add(task)
        await self.db.commit()
        return task
    
    async def update_task_status(self, task_id: str, status: TaskStatus) -> Task:
        """Update task status"""
        task = await self.get_task(task_id)
        if task:
            task.status = status
            await self.db.commit()
        return task
