"""
dependencies.py

FastAPI dependency wrappers for application services.
These functions retrieve service instances from the centralized container.
"""

from typing import AsyncGenerator
from fastapi import Depends
from src.container import get_container
from src.application.service import PlaceOrderService


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


async def get_place_order_service(
    session=Depends(get_session)
) -> PlaceOrderService:
    """Inject PlaceOrderService with an active DB session."""
    container = get_container()
    return container.place_order_service(session)
