"""
client_config.py

Configuration for external service clients (Stripe, Email, etc.).
This file serves as a professional example of modularizing external integration settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class ClientSettings(BaseSettings):
    """
    Settings specifically for external integration clients.
    """
    # Stripe Payment Settings
    STRIPE_API_KEY: str = Field(default="sk_test_mock", alias="STRIPE_API_KEY")
    STRIPE_WEBHOOK_SECRET: str = Field(default="whsec_mock", alias="STRIPE_WEBHOOK_SECRET")
    
    # Email Client Settings (e.g., SendGrid, Mailtrap)
    MAIL_SERVER: str = Field(default="smtp.mailtrap.io")
    MAIL_PORT: int = Field(default=587)
    MAIL_USERNAME: str = Field(default="user_mock")
    MAIL_PASSWORD: str = Field(default="pass_mock")
    MAIL_FROM: str = Field(default="no-reply@oms.com")

    # Circuit Breaker Defaults for Clients
    CLIENT_RETRY_ATTEMPTS: int = 3
    CLIENT_CIRCUIT_BREAKER_THRESHOLD: int = 5
    CLIENT_CIRCUIT_BREAKER_TIMEOUT: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True
    )


# Singleton instance
client_settings = ClientSettings()
