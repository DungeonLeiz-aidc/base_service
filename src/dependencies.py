"""
dependencies.py

FastAPI dependency wrappers for application services and security.
These functions retrieve service instances from the centralized container
and enforce security constraints like Bearer token validation.
"""

from typing import AsyncGenerator, Dict, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from loguru import logger

from src.container import get_container
from src.application.service import PlaceOrderService


# Security schema for Bearer Token
security = HTTPBearer()


async def get_session() -> AsyncGenerator:
    """Provide an async database session."""
    container = get_container()
    async with container.session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def get_auth_payload(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> Dict[str, Any]:
    """
    Validate Bearer token and return the decoded payload.

    Args:
        credentials: Bearer token credentials from the Request header.

    Returns:
        Decoded JWT payload.

    Raises:
        HTTPException: If token is invalid or missing.
    """
    container = get_container()
    try:
        token = credentials.credentials
        payload = container.auth_provider.verify_token(token)
        return payload
    except ValueError as e:
        logger.warning(f"AUDIT | Security Breach Attempt | {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e


async def get_place_order_service(
    session=Depends(get_session)
) -> PlaceOrderService:
    """Inject PlaceOrderService with an active DB session."""
    container = get_container()
    return container.place_order_service(session)
