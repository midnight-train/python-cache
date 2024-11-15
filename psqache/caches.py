"""This module contains the cache implementations."""

from typing import Any

import asyncpg
from asgiref.sync import async_to_sync

from psqache.abcs import ICacheBackend
from psqache.backends import PostgresBackend


class PsQache:
    """PsQache Cache implementation.

    Implements the ICache interface.
    Uses Postgres as the default cache backend.
    """

    DEFAULT_TTL = 28 * 24 * 60 * 60  # 4 weeks

    def __init__(self, backend: ICacheBackend) -> None:
        """Initialize the PsQache cache.

        Args:
            backend (ICacheBackend): The cache backend to use.
        """
        self.backend: ICacheBackend = backend

    @classmethod
    def use_postgres_backend(
        cls,
        dsn: str,
        min_size: int = 15,
        max_size: int = 25,
    ) -> "PsQache":
        """Create a PsQache instance with the Postgres backend.

        Args:
            dsn (str): The DSN for the Postgres database.
            min_size (int): The minimum number of connections in the pool.
            max_size (int): The maximum number of connections in the pool.

        Returns:
            PsQache: The PsQache instance with the Postgres backend.
        """
        return cls(
            backend=PostgresBackend(
                pool=asyncpg.create_pool(dsn=dsn, min_size=min_size, max_size=max_size),
            ),
        )

    async def aget(self, key: str) -> dict[Any, Any] | None:
        """Get the value for the given key asynchronously.

        Args:
            key (str): The key to get the value for.

        Returns:
            Optional[Any]: The value for the given key.
        """
        return await self.backend.get(key)

    get = async_to_sync(aget)

    async def aset(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Set the value for the given key asynchronously.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set for the given key.
            ttl (Optional[int], optional): Time to live. Defaults to None.
        """
        await self.backend.set(key, value, ttl or self.DEFAULT_TTL)

    set = async_to_sync(aset)

    async def adelete(self, key: str) -> None:
        """Delete the value for the given key asynchronously.

        Args:
            key (str): The key to delete the value for.
        """
        await self.backend.delete(key)

    delete = async_to_sync(adelete)

    async def ahas(self, key: str) -> bool:
        """Check if the given key is in the cache asynchronously.

        Args:
            key (str): The key to check.

        Returns:
            bool: True if the key is in the cache, False otherwise.
        """
        return await self.backend.has(key)

    has = async_to_sync(ahas)

    async def aclear(self) -> None:
        """Clear all cache entries asynchronously."""
        await self.backend.clear()

    clear = async_to_sync(aclear)

    async def acleanup(self) -> None:
        """Delete all expired cache entries asynchronously."""
        await self.backend.cleanup()

    cleanup = async_to_sync(acleanup)
