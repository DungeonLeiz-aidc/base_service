"""
test_redis_client.py

Unit tests for RedisInventoryCache using mocks.
"""

import pytest
from unittest.mock import AsyncMock, patch
from src.infrastructure.clients.redis_client import RedisInventoryCache
from src.domain.exceptions import InventoryLockError


@pytest.fixture
def mock_redis():
    return AsyncMock()


@pytest.fixture
def inventory_cache(mock_redis):
    return RedisInventoryCache(redis_client=mock_redis)


@pytest.mark.asyncio
class TestRedisInventoryCache:
    """Tests for Redis inventory management and locking."""

    async def test_get_stock(self, inventory_cache, mock_redis):
        mock_redis.get.return_value = b"50"
        
        stock = await inventory_cache.get_stock(1)
        
        assert stock == 50
        mock_redis.get.assert_called_with("inventory:product:1:stock")

    async def test_set_stock(self, inventory_cache, mock_redis):
        await inventory_cache.set_stock(1, 100, ttl=60)
        mock_redis.setex.assert_called_with("inventory:product:1:stock", 60, 100)

    async def test_reserve_stock_success(self, inventory_cache, mock_redis):
        """Should acquire lock, check stock, decrement, and release lock."""
        # Arrange
        product_id = 1
        quantity = 5
        mock_redis.set.return_value = True  # Lock acquired
        mock_redis.get.return_value = b"10" # Current stock
        
        # Act
        result = await inventory_cache.check_and_reserve_stock(product_id, quantity)
        
        # Assert
        assert result is True
        mock_redis.set.assert_called() # Lock key
        mock_redis.get.assert_called_with("inventory:product:1:stock")
        mock_redis.set.assert_any_call("inventory:product:1:stock", 5) # New stock
        mock_redis.delete.assert_called_with("inventory:product:1:lock")

    async def test_reserve_stock_insufficient(self, inventory_cache, mock_redis):
        """Should release lock and return False if stock is insufficient."""
        # Arrange
        mock_redis.set.return_value = True
        mock_redis.get.return_value = b"2"
        
        # Act
        result = await inventory_cache.check_and_reserve_stock(1, 5)
        
        # Assert
        assert result is False
        mock_redis.delete.assert_called_with("inventory:product:1:lock")

    async def test_reserve_stock_lock_fail(self, inventory_cache, mock_redis):
        """Should raise InventoryLockError if lock cannot be acquired."""
        # Arrange
        mock_redis.set.return_value = False # Lock failed
        
        # Act & Assert
        with pytest.raises(InventoryLockError):
            await inventory_cache.check_and_reserve_stock(1, 1, max_retries=1)

    async def test_release_stock(self, inventory_cache, mock_redis):
        await inventory_cache.release_stock(1, 10)
        mock_redis.incrby.assert_called_with("inventory:product:1:stock", 10)
