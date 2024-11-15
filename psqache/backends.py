"""This module contains the postgres cache backend implementation."""

import json
from typing import Any

import asyncpg

from psqache.queries import Queries


class PostgresBackend:
    """Postgres backend implementation of the cache.

    This class implements the cache backend using a Postgres database.
    Implements the ICacheBackend interface.
    """

    def __init__(self, pool: asyncpg.pool.Pool) -> None:
        """Initialize the PostgresBackend.

        Args:
            pool (asyncpg.pool.Pool): The pool to use for database connections.
        """
        self.pool = pool

    async def get(self, key: str) -> Any | None:
        """Retrieve a cache entry by key.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key, or None if not found or expired.
        """
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            value = await connection.fetchval(Queries.get_cache_entry.sql, key)
            return json.loads(value)

    async def set(self, key: str, value: dict, ttl: int) -> None:
        """Set or update a cache entry with a time-to-live.

        Args:
            key: The key to set.
            value: The value to associate with the key.
            ttl: Time-to-live in seconds for the entry.
        """
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            await connection.execute(
                Queries.set_cache_entry.sql,
                key,
                json.dumps(value),
                ttl,
            )

    async def delete(self, key: str) -> None:
        """Delete a cache entry by key.

        Args:
            key: The key to delete.
        """
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            await connection.execute(Queries.delete_cache_entry.sql, key)

    async def clear(self) -> None:
        """Clear all cache entries."""
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            await connection.execute(Queries.clear_cache_entries.sql)

    async def cleanup(self) -> None:
        """Delete all expired cache entries."""
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            await connection.execute(Queries.cleanup_expired_cache_entries.sql)

    async def has(self, key: str) -> bool:
        """Check if a cache entry exists and is not expired.

        Args:
            key: The key to check.

        Returns:
            True if the entry exists and is not expired, otherwise False.
        """
        connection: asyncpg.Connection
        async with self.pool.acquire() as connection:
            res = await connection.execute(Queries.has_cache_entry.sql, key)
            return bool(res)
