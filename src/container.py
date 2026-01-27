"""
container.py

Centralized Dependency Injection container.
Initializes and manages instances of repositories, services, and clients.
"""

from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from redis import asyncio as aioredis
from loguru import logger

from src.infrastructure.repositories import ProductRepository, OrderRepository
from src.infrastructure.caching.redis_inventory_cache import RedisInventoryCache
from src.infrastructure.messaging.rabbitmq_publisher import RabbitMQPublisher
from src.infrastructure.clients.auth_provider import AuthProvider
from src.application.service import PlaceOrderService, SeedService
from configs.service_config import settings


class AppContainer:
    """
    Singleton DI Container to manage application-wide dependencies.
    """
    
    _instance: Optional["AppContainer"] = None
    
    def __init__(self):
        # Database setup
        self.engine = create_async_engine(
            settings.DATABASE_URL,
            pool_size=settings.DATABASE_POOL_SIZE,
            max_overflow=settings.DATABASE_MAX_OVERFLOW,
            echo=settings.DATABASE_ECHO,
        )
        self.session_factory = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )
        
        # Redis setup
        self.redis = aioredis.from_url(
            settings.REDIS_URL,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
            decode_responses=True
        )
        
        # Infrastructure Clients
        self.inventory_cache = RedisInventoryCache(self.redis)
        self.event_publisher = RabbitMQPublisher(settings.RABBITMQ_URL)
        self.auth_provider = AuthProvider(
            base_url=settings.AUTH_SERVICE_URL,
            api_key=settings.INTERNAL_API_KEY,
            jwt_secret=settings.SUPABASE_JWT_SECRET
        )
        
    @classmethod
    def get_instance(cls) -> "AppContainer":
        if cls._instance is None:
            cls._instance = AppContainer()
        return cls._instance

    # Methods to get service instances
    def product_repository(self, session: AsyncSession) -> ProductRepository:
        return ProductRepository(session)
    
    def order_repository(self, session: AsyncSession) -> OrderRepository:
        return OrderRepository(session)
    
    def place_order_service(self, session: AsyncSession) -> PlaceOrderService:
        return PlaceOrderService(
            product_repository=self.product_repository(session),
            order_repository=self.order_repository(session),
            inventory_cache=self.inventory_cache,
            event_publisher=self.event_publisher,
        )
    
    def seed_service(self, session: AsyncSession) -> SeedService:
        """Get an instance of SeedService."""
        return SeedService(
            product_repository=self.product_repository(session)
        )

    async def dispose(self) -> None:
        """
        Dispose of all persistent resources.
        Closes Database engines, Redis connection pools, and Message Brokers.
        Ensures loggers are completed and cleared to prevent semaphore leaks.
        """
        logger.info("AUDIT | START | DISPOSAL | Cleaning system resources...")
        
        try:
            # 1. Close PostgreSQL connections
            await self.engine.dispose()
            logger.debug("AUDIT | DISPOSAL | PostgreSQL engine disposed.")
            
            # 2. Close Redis connections
            await self.redis.close()
            # Explicitly disconnect the pool for Perfectionist integrity
            await self.redis.connection_pool.disconnect()
            logger.debug("AUDIT | DISPOSAL | Redis client and pool closed.")
            
            # 3. Close RabbitMQ connection
            try:
                await self.event_publisher.close()
                logger.debug("AUDIT | DISPOSAL | RabbitMQ connection closed.")
            except Exception as e:
                logger.warning(f"AUDIT | DISPOSAL | RabbitMQ close failed: {e}")

            # 4. Final step: Clear loggers to stop enqueue threads/processes (Fixes semaphore leaks)
            logger.info("AUDIT | SUCCESS | DISPOSAL | Resources cleared. Shutting down logging...")
            logger.remove()
            
        except Exception as e:
            # Last ditch effort for logging if logger not yet removed
            sys.stderr.write(f"AUDIT | CRITICAL | DISPOSAL FAILED: {str(e)}\n")


_container: Optional[AppContainer] = None


def get_container() -> AppContainer:
    """Get or initialize the global DI container."""
    global _container
    if _container is None:
        _container = AppContainer.get_instance()
    return _container
