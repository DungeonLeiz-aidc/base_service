"""
payment_client.py

External payment gateway client (Abstract + Stripe Example).
Handles credit card processing logic.
"""

from typing import Protocol
from loguru import logger


class IPaymentClient(Protocol):
    """Interface for payment clients."""
    async def process_payment(self, amount: float, currency: str) -> bool:
        ...


class StripePaymentClient(IPaymentClient):
    """Stripe implementation of the payment client."""
    
    async def process_payment(self, amount: float, currency: str) -> bool:
        logger.info(f"Processing Stripe payment: {amount} {currency}")
        # Mock success
        return True
