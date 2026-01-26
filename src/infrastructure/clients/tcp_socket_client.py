"""
tcp_socket_client.py

TCP implementation of ISocketClient using Python's asyncio.
Includes comprehensive logging for audit and debugging.
"""

import asyncio
from loguru import logger
from src.interface.protocols.socket import ISocketClient

class TcpSocketClient(ISocketClient):
    """
    Standard TCP Socket implementation.
    Handles low-level I/O operations and connection state.
    """

    def __init__(self):
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None
        self._is_connected: bool = False

    async def connect(self, host: str, port: int) -> None:
        """
        Connects to the specified host and port.
        Logs the initiation and result of the connection.
        """
        logger.info(f"Action: Initiating TCP connection to {host}:{port}")
        try:
            self._reader, self._writer = await asyncio.open_connection(host, port)
            self._is_connected = True
            logger.success(f"Audit: Successfully connected to {host}:{port}")
        except Exception as e:
            logger.error(f"Audit: Failed to connect to {host}:{port}. Error: {str(e)}")
            raise

    async def send(self, data: str) -> None:
        """
        Sends encoded string data.
        Verifies connection status before transmission.
        """
        if not self._is_connected or not self._writer:
            logger.critical("Action: Attempted to send data without active connection.")
            raise ConnectionError("Socket is not connected.")

        logger.debug(f"Action: Sending {len(data)} bytes of data.")
        try:
            self._writer.write(data.encode())
            await self._writer.drain()
            logger.debug("Audit: Data transmitted successfully.")
        except Exception as e:
            logger.error(f"Audit: Data transmission failed: {str(e)}")
            raise

    async def receive(self, buffer_size: int = 1024) -> bytes:
        """
        Receives raw bytes from the stream.
        Logs the volume of data received.
        """
        if not self._is_connected or not self._reader:
            raise ConnectionError("Socket is not connected.")

        logger.debug(f"Action: Waiting for data (buffer size: {buffer_size}).")
        data = await self._reader.read(buffer_size)
        logger.info(f"Audit: Received {len(data)} bytes from remote.")
        return data

    async def close(self) -> None:
        """
        Safely closes the connection and cleans up resources.
        """
        if self._writer:
            logger.info("Action: Closing TCP socket connection.")
            self._writer.close()
            await self._writer.wait_closed()
            self._is_connected = False
            logger.success("Audit: Socket connection closed safely.")