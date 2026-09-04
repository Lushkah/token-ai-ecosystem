"""Configuration settings for Token AI Ecosystem"""

from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # Platform Configuration
    PLATFORM_ENV: str = "development"
    PLATFORM_DEBUG: bool = True
    PLATFORM_HOST: str = "0.0.0.0"
    PLATFORM_PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql://tokenai:tokenai@localhost:5432/token_ai_ecosystem"
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_TTL: int = 3600
    
    # Token System
    TOKEN_TOTAL_SUPPLY: int = 1_000_000_000
    TOKEN_DECIMALS: int = 18
    TOKEN_SYMBOL: str = "TAI"
    
    # Agent Configuration
    AGENT_ENABLED_TYPES: List[str] = ["developer", "architect", "tester", "optimizer"]
    AGENT_MAX_CONCURRENT_TASKS: int = 10
    AGENT_TIMEOUT_SECONDS: int = 3600
    AGENT_RETRY_ATTEMPTS: int = 3
    
    # Reward System
    REWARD_BASE_AMOUNT: float = 100.0
    REWARD_QUALITY_MULTIPLIER: float = 1.5
    REWARD_INNOVATION_BONUS: float = 500.0
    REWARD_EFFICIENCY_BONUS: float = 300.0
    
    # Governance
    GOVERNANCE_VOTING_PERIOD_DAYS: int = 7
    GOVERNANCE_MIN_QUORUM: int = 30
    GOVERNANCE_APPROVAL_THRESHOLD: int = 50
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    
    # CORS
    CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
