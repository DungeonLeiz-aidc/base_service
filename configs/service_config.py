"""
service_config.py

Service configuration using Pydantic.
Handles environment variables with validation and default values.
"""

from enum import Enum
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class AppEnvironment(str, Enum):
    """Supported application environments."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class LogFormat(str, Enum):
    """Supported logging formats."""
    PRETTY = "pretty"
    JSON = "json"


class ServiceSettings(BaseSettings):
    """
    Centralized service configuration using Pydantic.
    Handles environment variables with validation and default values.
    """
    # Project Info
    PROJECT_NAME: str = "OrderPlacementService"
    DEBUG: bool = False
    ENVIRONMENT: AppEnvironment = AppEnvironment.DEVELOPMENT

    # Logging Configuration
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: LogFormat = LogFormat.PRETTY
    LOG_DIR: str = Field(default="logs")
    LOG_RETENTION: str = Field(default="90 days")
    LOG_ROTATION: str = Field(default="00:00")

    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api"
    API_RELOAD: bool = True

    # Database - PostgreSQL
    DATABASE_URL: str = Field(..., alias="DATABASE_URL")
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    DATABASE_ECHO: bool = False

    # Redis Settings
    REDIS_URL: str = Field(..., alias="REDIS_URL")
    REDIS_MAX_CONNECTIONS: int = 50

    # RabbitMQ Settings
    RABBITMQ_URL: str = Field(..., alias="RABBITMQ_URL")

    # CORS Settings
    CORS_ORIGINS: List[str] = ["*"]

    # Internal Service Communication
    AUTH_SERVICE_URL: str = Field(default="http://auth-service:8000")
    INTERNAL_API_KEY: str = Field(default="your-internal-api-key")

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    SUPABASE_JWT_SECRET: str = Field(default="your-supabase-jwt-secret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True
    )


# Singleton instance to be used across the application
settings = ServiceSettings()