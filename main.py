#!/usr/bin/env python3
"""
Token AI Ecosystem - Main Entry Point
"""

import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import settings
from src.database import init_db
from src.routes import (
    agents,
    governance,
    health,
    tasks,
    tokens,
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    logger.info("Starting Token AI Ecosystem...")
    await init_db()
    logger.info("Database initialized")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Token AI Ecosystem...")


# Create FastAPI application
app = FastAPI(
    title="Token AI Ecosystem",
    description="A comprehensive ecosystem and token-based AI self-building platform",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Check system health"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "version": "0.1.0",
            "environment": settings.PLATFORM_ENV,
        }
    )


# Root endpoint
@app.get("/", tags=["Info"])
async def root():
    """Welcome to Token AI Ecosystem"""
    return {
        "name": "Token AI Ecosystem",
        "description": "A self-building AI platform powered by tokens",
        "version": "0.1.0",
        "docs": "/docs",
    }


# Include routers
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["Agents"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(tokens.router, prefix="/api/v1/tokens", tags=["Tokens"])
app.include_router(governance.router, prefix="/api/v1/governance", tags=["Governance"])


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "type": type(exc).__name__,
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {settings.PLATFORM_HOST}:{settings.PLATFORM_PORT}")
    logger.info(f"Environment: {settings.PLATFORM_ENV}")
    logger.info(f"Debug: {settings.PLATFORM_DEBUG}")
    
    uvicorn.run(
        "main:app",
        host=settings.PLATFORM_HOST,
        port=settings.PLATFORM_PORT,
        reload=settings.PLATFORM_DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
