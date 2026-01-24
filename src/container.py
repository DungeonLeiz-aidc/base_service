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
from src.infrastructure.clients.redis_client import RedisInventoryCache
from src.infrastructure.clients.rabbitmq_client import RabbitMQPublisher
from src.application.service import PlaceOrderService
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


_container: Optional[AppContainer] = None


def get_container() -> AppContainer:
    """Get or initialize the global DI container."""
    global _container
    if _container is None:
        _container = AppContainer.get_instance()
    return _container
