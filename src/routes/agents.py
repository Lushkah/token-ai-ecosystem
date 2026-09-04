"""Agent routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from src.database import get_db_session

router = APIRouter()


class AgentResponse(BaseModel):
    """Agent response model"""
    id: str
    name: str
    agent_type: str
    status: str
    token_balance: float
    total_tasks_completed: int
    success_rate: float


@router.get("/")
async def list_agents(db: AsyncSession = Depends(get_db_session)):
    """List all agents"""
    return {
        "agents": [],
        "total": 0,
    }


@router.get("/{agent_id}")
async def get_agent(agent_id: str, db: AsyncSession = Depends(get_db_session)):
    """Get agent by ID"""
    return {"agent_id": agent_id}


@router.post("/")
async def create_agent(db: AsyncSession = Depends(get_db_session)):
    """Create new agent"""
    return {"message": "Agent created"}
