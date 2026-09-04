"""Token service"""

import logging
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.token import Token, TokenTransaction, TransactionType
from src.config import settings

logger = logging.getLogger(__name__)


class TokenService:
    """Service for token operations"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_or_create_token(self) -> Token:
        """Get or create the main token"""
        result = await self.db.execute(
            select(Token).where(Token.symbol == settings.TOKEN_SYMBOL)
        )
        token = result.scalar_one_or_none()
        
        if not token:
            token = Token(
                id="token-1",
                symbol=settings.TOKEN_SYMBOL,
                name="Token AI",
                total_supply=settings.TOKEN_TOTAL_SUPPLY,
                decimals=settings.TOKEN_DECIMALS,
            )
            self.db.add(token)
            await self.db.commit()
        
        return token
    
    async def create_transaction(
        self,
        transaction_type: TransactionType,
        to_address: str,
        amount: float,
        from_address: Optional[str] = None,
        agent_id: Optional[str] = None,
        task_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> TokenTransaction:
        """Create token transaction"""
        transaction = TokenTransaction(
            id=f"tx-{int(__import__('time').time() * 1000)}",
            transaction_type=transaction_type,
            from_address=from_address or "system",
            to_address=to_address,
            amount=amount,
            agent_id=agent_id,
            task_id=task_id,
            description=description,
        )
        self.db.add(transaction)
        await self.db.commit()
        return transaction
