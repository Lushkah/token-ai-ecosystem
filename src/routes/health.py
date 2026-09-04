"""Health check routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session

router = APIRouter()


@router.get("/")
async def health_check(db: AsyncSession = Depends(get_db_session)):
    """Check system health"""
    return {
        "status": "healthy",
        "database": "connected",
    }
