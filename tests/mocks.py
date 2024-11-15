"""This module contains mock implementations for testing purposes."""

from typing import Any

from asgiref import sync as asgiref_sync

from psqache import abcs


class MockCache(abcs.ICache):
    """Mock implementation of the CacheProtocol for testing purposes."""

    def __init__(self, backend: abcs.ICacheBackend):
        """Initialize the mock cache storage.

        Attributes:
            store (dict): The cache storage.
        """
        self.backend = backend

    async def aget(self, key: str) -> Any | None:
        """Mock implementation of the async get method."""
        return await self.backend.get(key)

    def get(self, key: str) -> Any | None:
        """Mock implementation of the sync get method."""
        return asgiref_sync.async_to_sync(self.aget)(key)

    async def aset(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Mock implementation of the async set method."""
        _ttl = ttl if ttl is not None else 3600
        await self.backend.set(key, value, _ttl)

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Mock implementation of the sync set method."""
        asgiref_sync.async_to_sync(self.aset)(key, value, ttl)

    async def adelete(self, key: str) -> None:
        """Mock implementation of the async delete method."""
        await self.backend.delete(key)

    def delete(self, key: str) -> None:
        """Mock implementation of the sync delete method."""
        asgiref_sync.async_to_sync(self.adelete)(key)

    async def aclear(self) -> None:
        """Mock implementation of the async clear method."""
        await self.backend.clear()

    def clear(self) -> None:
        """Mock implementation of the sync clear method."""
        asgiref_sync.async_to_sync(self.aclear)()

    async def acleanup(self) -> None:
        """Mock implementation of the async cleanup method."""
        await self.backend.cleanup()

    def cleanup(self) -> None:
        """Mock implementation of the sync cleanup method."""
        asgiref_sync.async_to_sync(self.acleanup)()

    async def ahas(self, key: str) -> bool:
        """Mock implementation of the async has method."""
        return await self.backend.has(key)

    def has(self, key: str) -> bool:
        """Mock implementation of the sync has method."""
        return asgiref_sync.async_to_sync(self.ahas)(key)


class MockBackend(abcs.ICacheBackend):
    """Mock implementation of the CacheBackendProtocol for testing purposes."""

    def __init__(self):
        """Initialize the mock cache backend.

        Attributes:
            store (dict): The cache storage.
        """
        self.store = {}

    async def get(self, key: str) -> Any | None:
        """Mock implementation of the sync get method."""
        return self.store.get(key)

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Mock implementation of the async set method."""
        self.store[key] = value

    async def delete(self, key: str) -> None:
        """Mock implementation of the async delete method."""
        if key in self.store:
            del self.store[key]

    async def clear(self) -> None:
        """Mock implementation of the async clear method."""
        self.store.clear()

    async def cleanup(self) -> None:
        """Mock implementation of the async cleanup method."""
        self.store.clear()

    async def has(self, key: str) -> bool:
        """Mock implementation of the async has method."""
        return key in self.store
