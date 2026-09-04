"""Task routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from src.database import get_db_session

router = APIRouter()


class TaskResponse(BaseModel):
    """Task response model"""
    id: str
    title: str
    status: str
    assigned_agent_id: str | None
    priority: int
    base_reward: float


@router.get("/")
async def list_tasks(db: AsyncSession = Depends(get_db_session)):
    """List all tasks"""
    return {
        "tasks": [],
        "total": 0,
    }


@router.get("/{task_id}")
async def get_task(task_id: str, db: AsyncSession = Depends(get_db_session)):
    """Get task by ID"""
    return {"task_id": task_id}


@router.post("/")
async def create_task(db: AsyncSession = Depends(get_db_session)):
    """Create new task"""
    return {"message": "Task created"}


@router.patch("/{task_id}")
async def update_task(task_id: str, db: AsyncSession = Depends(get_db_session)):
    """Update task"""
    return {"message": "Task updated"}
