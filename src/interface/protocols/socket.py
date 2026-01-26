"""
socket.py

Technical protocol for socket communication.
Defines the contract for sending and receiving raw data.
"""

from typing import Protocol, Any

class ISocketClient(Protocol):
    """
    Protocol for Socket Client.
    Ensures consistent interface for any socket-based communication.
    """

    async def connect(self, host: str, port: int) -> None:
        """Establish connection to the remote host."""
        ...

    async def send(self, data: Any) -> None:
        """Send data through the socket."""
        ...

    async def receive(self, buffer_size: int = 1024) -> bytes:
        """Receive data from the socket."""
        ...

    async def close(self) -> None:
        """Terminate the socket connection."""
        ...