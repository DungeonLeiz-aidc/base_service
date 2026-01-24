"""
payment_client.py

External payment gateway client (Abstract + Stripe Example).
Handles credit card processing logic.
"""

import time
from typing import Protocol
from loguru import logger
from src.domain.exceptions import PaymentFailedError


class IPaymentClient(Protocol):
    """Interface for payment clients."""
    async def process_payment(self, amount: float, currency: str) -> bool:
        ...


class StripePaymentClient(IPaymentClient):
    """
    Stripe implementation of the payment client with a simple Circuit Breaker.
    Protects the system from repeated failures of the external payment gateway.
    """
    
    def __init__(self):
        self._state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        self._failure_count = 0
        self._failure_threshold = 3
        self._recovery_timeout = 30  # seconds
        self._last_failure_time = 0

    async def process_payment(self, amount: float, currency: str) -> bool:
        if self._state == "OPEN":
            if time.time() - self._last_failure_time > self._recovery_timeout:
                logger.info("Circuit Breaker: Transitioning to HALF_OPEN")
                self._state = "HALF_OPEN"
            else:
                logger.warning("Circuit Breaker: State is OPEN. Rejecting payment.")
                raise PaymentFailedError("Payment gateway is currently unavailable (Circuit Open)")

        try:
            logger.info(f"Processing Stripe payment: {amount} {currency}")
            # Simulate actual processing or failure
            # result = await self._call_stripe_api(...)
            result = True 
            
            if result:
                if self._state == "HALF_OPEN":
                    logger.info("Circuit Breaker: Transitioning to CLOSED")
                    self._state = "CLOSED"
                    self._failure_count = 0
                return True
            else:
                raise Exception("Stripe API error")
                
        except Exception as e:
            self._failure_count += 1
            self._last_failure_time = time.time()
            if self._failure_count >= self._failure_threshold:
                logger.error(f"Circuit Breaker: Failure threshold reached. Transitioning to OPEN. Error: {e}")
                self._state = "OPEN"
            raise PaymentFailedError(str(e))
