"""
rabbitmq_client.py

RabbitMQ client for publishing domain events.
"""

import json
from typing import Any, Dict
from aio_pika import connect, Message, ExchangeType, Connection, Channel, Exchange
from aio_pika.abc import AbstractRobustConnection
from loguru import logger


class RabbitMQPublisher:
    """
    RabbitMQ publisher for domain events.
    
    Publishes events to topic exchange for downstream consumers.
    """
    
    def __init__(
        self,
        rabbitmq_url: str,
        exchange_name: str = "order_events",
        exchange_type: ExchangeType = ExchangeType.TOPIC,
    ):
        """
        Initialize RabbitMQ publisher.
        
        Args:
            rabbitmq_url: RabbitMQ connection URL.
            exchange_name: Exchange name.
            exchange_type: Exchange type.
        """
        self.rabbitmq_url = rabbitmq_url
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.connection: AbstractRobustConnection | None = None
        self.channel: Channel | None = None
        self.exchange: Exchange | None = None
    
    async def connect(self) -> None:
        """Establish connection to RabbitMQ."""
        logger.info(f"Connecting to RabbitMQ: {self.rabbitmq_url}")
        
        self.connection = await connect(self.rabbitmq_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            self.exchange_type,
            durable=True,
        )
        
        logger.info(f"Connected to RabbitMQ exchange: {self.exchange_name}")
    
    async def close(self) -> None:
        """Close RabbitMQ connection."""
        if self.connection:
            await self.connection.close()
            logger.info("Closed RabbitMQ connection")
    
    async def publish(self, event: Any) -> None:
        """
        Publish domain event to RabbitMQ.
        
        Args:
            event: Domain event with to_dict() method.
        """
        if self.exchange is None:
            raise RuntimeError("Publisher not connected. Call connect() first.")
        
        # Convert event to dict
        event_dict = event.to_dict()
        event_type = event_dict.get("event_type", "unknown")
        
        # Serialize to JSON
        message_body = json.dumps(event_dict).encode()
        
        # Create message
        message = Message(
            body=message_body,
            content_type="application/json",
            delivery_mode=2,  # Persistent
        )
        
        # Routing key based on event type (e.g., "order.placed")
        routing_key = event_type
        
        # Publish to exchange
        await self.exchange.publish(
            message,
            routing_key=routing_key,
        )
        
        logger.info(f"Published event: {event_type} with routing key: {routing_key}")
