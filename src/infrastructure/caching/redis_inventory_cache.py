"""
redis_inventory_cache.py

Redis-based implementation of IInventoryCache.
Provides atomic stock reservation using distributed locks.
"""

import asyncio
from typing import Optional
from redis import asyncio as aioredis
from loguru import logger

from src.interface.protocols.infrastructure import IInventoryCache
from src.domain.exceptions import InventoryLockError


class RedisInventoryCache(IInventoryCache):
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
        """Get current stock from cache."""
        key = self._get_stock_key(product_id)
        stock = await self.redis.get(key)
        
        if stock is None:
            return None
        
        return int(stock)
    
    async def set_stock(self, product_id: int, quantity: int, ttl: int = 3600) -> None:
        """Set stock in cache."""
        key = self._get_stock_key(product_id)
        await self.redis.setex(key, ttl, quantity)
        logger.debug(f"Cached stock for product {product_id}: {quantity}")
    
    async def check_and_reserve_stock(
        self,
        product_id: int,
        quantity: int,
        max_retries: int = 3,
    ) -> bool:
        """Check stock availability and reserve if available using distributed lock."""
        lock_key = self._get_lock_key(product_id)
        stock_key = self._get_stock_key(product_id)
        
        for attempt in range(max_retries):
            lock_acquired = await self.redis.set(
                lock_key,
                "1",
                ex=self.lock_timeout,
                nx=True,
            )
            
            if not lock_acquired:
                logger.debug(f"Failed to acquire lock for product {product_id}, attempt {attempt + 1}")
                await asyncio.sleep(self.lock_sleep)
                continue
            
            try:
                current_stock = await self.redis.get(stock_key)
                
                if current_stock is None:
                    logger.warning(f"Stock for product {product_id} not in cache")
                    return False
                
                current_stock = int(current_stock)
                
                if current_stock < quantity:
                    logger.debug(f"Insufficient stock for product {product_id}")
                    return False
                
                new_stock = current_stock - quantity
                await self.redis.set(stock_key, new_stock)
                
                logger.info(f"Reserved {quantity} units of product {product_id}")
                return True
                
            finally:
                await self.redis.delete(lock_key)
        
        raise InventoryLockError(
            product_id=product_id,
            reason=f"Could not acquire lock after {max_retries} attempts",
        )
    
    async def release_stock(self, product_id: int, quantity: int) -> None:
        """Release reserved stock (increment)."""
        stock_key = self._get_stock_key(product_id)
        new_stock = await self.redis.incrby(stock_key, quantity)
        logger.info(f"Released {quantity} units of product {product_id}. New stock: {new_stock}")
