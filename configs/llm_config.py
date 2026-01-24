"""
llm_config.py

Configuration for AI and LLM integrations (OpenAI, Anthropic, etc.).
This file serves as a specialized module for managing AI-related technical parameters.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class LLMSettings(BaseSettings):
    """
    Settings for LLM model providers and generation parameters.
    """
    # LLM Provider Keys
    OPENAI_API_KEY: str = Field(default="sk-mock-key", alias="OPENAI_API_KEY")
    ANTHROPIC_API_KEY: str = Field(default="sk-ant-mock", alias="ANTHROPIC_API_KEY")
    
    # Model Selection
    PRIMARY_MODEL: str = Field(default="gpt-4-turbo")
    FALLBACK_MODEL: str = Field(default="gpt-3.5-turbo")

    # Generation Parameters
    LLM_TEMPERATURE: float = Field(default=0.7)
    LLM_MAX_TOKENS: int = Field(default=1024)
    LLM_TIMEOUT: int = Field(default=30)

    # Token Usage Management
    LLM_COST_LIMIT_DAILY: float = Field(default=5.0)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True
    )


# Singleton instance
llm_settings = LLMSettings()
