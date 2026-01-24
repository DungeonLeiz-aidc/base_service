"""
infrastructure/schemas.py

Infrastructure-specific data schemas and models.
Includes Redis message formats and external API response structures.
"""

from pydantic import BaseModel
from typing import Dict, Any


class RedisLockMetadata(BaseModel):
    """Schema for metadata stored in Redis locks."""
    order_id: int
    locked_at: float
    owner_id: str


class ExternalAPILog(BaseModel):
    """Schema for logging external API interactions."""
    service_name: str
    endpoint: str
    status_code: int
    payload: Dict[str, Any]
