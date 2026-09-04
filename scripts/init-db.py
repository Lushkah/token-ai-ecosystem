#!/usr/bin/env python3
"""Database initialization script"""

import asyncio
import logging
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import init_db, engine
from src.models import Agent, Token
from src.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init_sample_data():
    """Initialize sample data"""
    async with engine.begin() as conn:
        # Create tables
        await init_db()
        
        logger.info("Database initialization completed")


if __name__ == "__main__":
    logger.info("Starting database initialization...")
    asyncio.run(init_sample_data())
    logger.info("Database initialization successful!")
