"""This module contains mock implementations for testing purposes."""

from typing import Any

from psqache.abcs import CacheProtocol


class MockCache(CacheProtocol):
    """Mock implementation of the CacheProtocol for testing purposes."""

    def __init__(self):
        """Initialize the mock cache storage.

        Attributes:
            store (dict): The cache storage.
        """
        self.store = {}

    async def aget(self, key: str) -> Any | None:
        """Mock implementation of the async get method."""
        return self.store.get(key)

    def get(self, key: str) -> Any | None:
        """Mock implementation of the sync get method."""
        return self.store.get(key)

    async def aset(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Mock implementation of the async set method."""
        self.store[key] = value

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Mock implementation of the sync set method."""
        self.store[key] = value

    async def adelete(self, key: str) -> None:
        """Mock implementation of the async delete method."""
        if key in self.store:
            del self.store[key]

    def delete(self, key: str) -> None:
        """Mock implementation of the sync delete method."""
        if key in self.store:
            del self.store[key]

    async def aclear(self) -> None:
        """Mock implementation of the async clear method."""
        self.store.clear()

    def clear(self) -> None:
        """Mock implementation of the sync clear method."""
        self.store.clear()

    async def acleanup(self) -> None:
        """Mock implementation of the async cleanup method."""
        # Mock implementation does not handle TTL

    def cleanup(self) -> None:
        """Mock implementation of the sync cleanup method."""
        # Mock implementation does not handle TTL

    async def ahas(self, key: str) -> bool:
        """Mock implementation of the async has method."""
        return key in self.store

    def has(self, key: str) -> bool:
        """Mock implementation of the sync has method."""
        return key in self.store
