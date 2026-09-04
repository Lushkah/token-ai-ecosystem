"""Governance routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from src.database import get_db_session

router = APIRouter()


class ProposalResponse(BaseModel):
    """Proposal response model"""
    id: str
    title: str
    status: str
    votes_for: float
    votes_against: float
    votes_abstain: float


@router.get("/proposals")
async def list_proposals(db: AsyncSession = Depends(get_db_session)):
    """List all proposals"""
    return {
        "proposals": [],
        "total": 0,
    }


@router.get("/proposals/{proposal_id}")
async def get_proposal(proposal_id: str, db: AsyncSession = Depends(get_db_session)):
    """Get proposal by ID"""
    return {"proposal_id": proposal_id}


@router.post("/proposals")
async def create_proposal(db: AsyncSession = Depends(get_db_session)):
    """Create new proposal"""
    return {"message": "Proposal created"}


@router.post("/proposals/{proposal_id}/vote")
async def vote_on_proposal(proposal_id: str, db: AsyncSession = Depends(get_db_session)):
    """Vote on proposal"""
    return {"message": "Vote recorded"}
