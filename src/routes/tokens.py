"""Token routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from src.database import get_db_session

router = APIRouter()


class TokenInfoResponse(BaseModel):
    """Token info response model"""
    symbol: str
    name: str
    total_supply: float
    circulating_supply: float
    decimals: int


@router.get("/info")
async def get_token_info(db: AsyncSession = Depends(get_db_session)):
    """Get token information"""
    return {
        "symbol": "TAI",
        "name": "Token AI",
        "total_supply": 1_000_000_000,
        "circulating_supply": 0,
        "decimals": 18,
    }


@router.get("/balance/{address}")
async def get_balance(address: str, db: AsyncSession = Depends(get_db_session)):
    """Get token balance for address"""
    return {
        "address": address,
        "balance": 0.0,
    }


@router.get("/transactions/{address}")
async def get_transactions(address: str, db: AsyncSession = Depends(get_db_session)):
    """Get token transactions for address"""
    return {
        "address": address,
        "transactions": [],
        "total": 0,
    }
