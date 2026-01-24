"""
test_rabbitmq_client.py

Unit tests for RabbitMQPublisher using mocks.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.infrastructure.clients.rabbitmq_client import RabbitMQPublisher


@pytest.fixture
def mock_event():
    event = MagicMock()
    event.to_dict.return_value = {
        "event_type": "order.placed",
        "order_id": 123
    }
    return event


@pytest.mark.asyncio
class TestRabbitMQPublisher:
    """Tests for RabbitMQ event publishing."""

    async def test_publish_success(self, mock_event):
        # Arrange
        publisher = RabbitMQPublisher(rabbitmq_url="amqp://test")
        publisher.exchange = AsyncMock()
        
        # Act
        await publisher.publish(mock_event)
        
        # Assert
        publisher.exchange.publish.assert_called_once()
        args, kwargs = publisher.exchange.publish.call_args
        assert kwargs["routing_key"] == "order.placed"
        assert b"order.placed" in args[0].body

    async def test_publish_without_connection(self, mock_event):
        # Arrange
        publisher = RabbitMQPublisher(rabbitmq_url="amqp://test")
        
        # Act & Assert
        with pytest.raises(RuntimeError, match="Publisher not connected"):
            await publisher.publish(mock_event)

    @patch("src.infrastructure.clients.rabbitmq_client.connect")
    async def test_connect(self, mock_connect):
        # Arrange
        mock_conn = AsyncMock()
        mock_channel = AsyncMock()
        mock_connect.return_value = mock_conn
        mock_conn.channel.return_value = mock_channel
        
        publisher = RabbitMQPublisher(rabbitmq_url="amqp://test")
        
        # Act
        await publisher.connect()
        
        # Assert
        assert publisher.connection == mock_conn
        mock_channel.declare_exchange.assert_called_once()
