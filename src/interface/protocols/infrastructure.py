"""
infrastructure.py

Protocols for infrastructure services (Caching, Messaging).
These interfaces define the contracts for technical services used by the application.
"""

from typing import Protocol


class IInventoryCache(Protocol):
    """Protocol for inventory caching service."""
    
    async def check_and_reserve_stock(
        self, product_id: int, quantity: int
    ) -> bool:
        """Check stock availability and reserve if available."""
        ...
    
    async def release_stock(self, product_id: int, quantity: int) -> None:
        """Release reserved stock."""
        ...


class IEventPublisher(Protocol):
    """Protocol for event publishing service."""
    
    async def publish(self, event) -> None:
        """Publish domain event."""
        ...
