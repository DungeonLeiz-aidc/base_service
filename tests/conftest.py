"""
conftest.py

Global fixtures and configuration for the test suite.
Includes mandatory resource cleanup for the centralized AppContainer.
"""

import pytest
import pytest_asyncio
import asyncio
from src.container import get_container


@pytest_asyncio.fixture(scope="session", autouse=True)
async def cleanup_container():
    """
    Session-scoped fixture to ensure AppContainer resources are disposed of
    at the end of the test suite.
    """
    yield
    
    # After all tests are done
    container = get_container()
    await container.dispose()


@pytest.fixture(scope="session")
def event_loop():
    """
    Custom event loop fixture to maintain a single loop across the test session.
    Prevents loop-related resource leakage.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
