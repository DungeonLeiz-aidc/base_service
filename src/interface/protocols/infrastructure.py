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


class IAuthProvider(Protocol):
    """Protocol for authentication provider."""
    
    async def verify_token(self, token: str) -> dict:
        """Verify a JWT token and return the payload."""
        ...

    async def authorize(self, token: str, required_permission: str) -> bool:
        """Check if a user has a specific permission via central Auth Service."""
        ...
