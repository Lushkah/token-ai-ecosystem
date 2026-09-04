"""Agent service"""

import logging
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.agent import Agent, AgentStatus

logger = logging.getLogger(__name__)


class AgentService:
    """Service for agent operations"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def list_agents(self) -> List[Agent]:
        """List all agents"""
        result = await self.db.execute(select(Agent))
        return result.scalars().all()
    
    async def get_agent(self, agent_id: str) -> Optional[Agent]:
        """Get agent by ID"""
        result = await self.db.execute(
            select(Agent).where(Agent.id == agent_id)
        )
        return result.scalar_one_or_none()
    
    async def create_agent(self, agent_data: dict) -> Agent:
        """Create new agent"""
        agent = Agent(**agent_data)
        self.db.add(agent)
        await self.db.commit()
        return agent
    
    async def update_agent_status(self, agent_id: str, status: AgentStatus) -> Agent:
        """Update agent status"""
        agent = await self.get_agent(agent_id)
        if agent:
            agent.status = status
            await self.db.commit()
        return agent
