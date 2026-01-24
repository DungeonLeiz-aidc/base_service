"""
redis_client.py

Redis client for inventory caching and distributed locking.
Implements inventory reservation with distributed locks to prevent overselling.
"""

import asyncio
from typing import Optional
from redis import asyncio as aioredis
from loguru import logger

from src.domain.exceptions import InventoryLockError


class RedisInventoryCache:
    """
    Redis-based inventory cache with distributed locking.
    
    Uses Redis for:
    1. Fast inventory lookups (cache)
    2. Distributed locking to prevent race conditions
    3. Atomic stock reservation
    """
    
    def __init__(
        self,
        redis_client: aioredis.Redis,
        lock_timeout: int = 30,
        lock_sleep: float = 0.1,
    ):
        """
        Initialize Redis inventory cache.
        
        Args:
            redis_client: Redis client instance.
            lock_timeout: Lock timeout in seconds.
            lock_sleep: Sleep duration between lock acquisition retries.
        """
        self.redis = redis_client
        self.lock_timeout = lock_timeout
        self.lock_sleep = lock_sleep
    
    def _get_stock_key(self, product_id: int) -> str:
        """Get Redis key for product stock."""
        return f"inventory:product:{product_id}:stock"
    
    def _get_lock_key(self, product_id: int) -> str:
        """Get Redis key for product lock."""
        return f"inventory:product:{product_id}:lock"
    
    async def get_stock(self, product_id: int) -> Optional[int]:
        """
        Get current stock from cache.
        
        Args:
            product_id: Product ID.
            
        Returns:
            Current stock quantity or None if not cached.
        """
        key = self._get_stock_key(product_id)
        stock = await self.redis.get(key)
        
        if stock is None:
            return None
        
        return int(stock)
    
    async def set_stock(self, product_id: int, quantity: int, ttl: int = 3600) -> None:
        """
        Set stock in cache.
        
        Args:
            product_id: Product ID.
            quantity: Stock quantity.
            ttl: Time to live in seconds.
        """
        key = self._get_stock_key(product_id)
        await self.redis.setex(key, ttl, quantity)
        logger.debug(f"Cached stock for product {product_id}: {quantity}")
    
    async def check_and_reserve_stock(
        self,
        product_id: int,
        quantity: int,
        max_retries: int = 3,
    ) -> bool:
        """
        Check stock availability and reserve if available.
        
        Uses distributed lock to ensure atomic operation and prevent overselling.
        
        Args:
            product_id: Product ID.
            quantity: Quantity to reserve.
            max_retries: Maximum lock acquisition retries.
            
        Returns:
            True if reservation successful, False if insufficient stock.
            
        Raises:
            InventoryLockError: If unable to acquire lock after retries.
        """
        lock_key = self._get_lock_key(product_id)
        stock_key = self._get_stock_key(product_id)
        
        for attempt in range(max_retries):
            # Try to acquire distributed lock
            lock_acquired = await self.redis.set(
                lock_key,
                "1",
                ex=self.lock_timeout,
                nx=True,  # Only set if not exists
            )
            
            if not lock_acquired:
                logger.debug(
                    f"Failed to acquire lock for product {product_id}, "
                    f"attempt {attempt + 1}/{max_retries}"
                )
                await asyncio.sleep(self.lock_sleep)
                continue
            
            try:
                # Lock acquired, check and reserve stock
                current_stock = await self.redis.get(stock_key)
                
                if current_stock is None:
                    # Stock not in cache, cannot proceed
                    logger.warning(
                        f"Stock for product {product_id} not in cache"
                    )
                    return False
                
                current_stock = int(current_stock)
                
                if current_stock < quantity:
                    # Insufficient stock
                    logger.debug(
                        f"Insufficient stock for product {product_id}. "
                        f"Available: {current_stock}, Requested: {quantity}"
                    )
                    return False
                
                # Reserve stock (decrement)
                new_stock = current_stock - quantity
                await self.redis.set(stock_key, new_stock)
                
                logger.info(
                    f"Reserved {quantity} units of product {product_id}. "
                    f"Remaining: {new_stock}"
                )
                return True
                
            finally:
                # Always release lock
                await self.redis.delete(lock_key)
        
        # Failed to acquire lock after all retries
        raise InventoryLockError(
            product_id=product_id,
            reason=f"Could not acquire lock after {max_retries} attempts",
        )
    
    async def release_stock(self, product_id: int, quantity: int) -> None:
        """
        Release reserved stock (increment).
        
        Used when order is cancelled or fails.
        
        Args:
            product_id: Product ID.
            quantity: Quantity to release.
        """
        stock_key = self._get_stock_key(product_id)
        
        # Increment stock (atomic operation)
        new_stock = await self.redis.incrby(stock_key, quantity)
        
        logger.info(
            f"Released {quantity} units of product {product_id}. "
            f"New stock: {new_stock}"
        )
    
    async def sync_stock_from_db(
        self,
        product_id: int,
        quantity: int,
        ttl: int = 3600,
    ) -> None:
        """
        Sync stock from database to cache.
        
        Called periodically or after cache miss.
        
        Args:
            product_id: Product ID.
            quantity: Stock quantity from database.
            ttl: Cache TTL in seconds.
        """
        await self.set_stock(product_id, quantity, ttl)
        logger.debug(f"Synced stock for product {product_id} from DB: {quantity}")
    
    async def clear_stock(self, product_id: int) -> None:
        """
        Clear stock from cache.
        
        Args:
            product_id: Product ID.
        """
        stock_key = self._get_stock_key(product_id)
        await self.redis.delete(stock_key)
        logger.debug(f"Cleared stock cache for product {product_id}")
