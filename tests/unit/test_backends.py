import json
from unittest.mock import AsyncMock

import asyncpg
import pytest

from psqache.backends import PostgresBackend


@pytest.fixture
async def asyncpg_pool():
    """Fixture for the asyncpg pool object."""
    return AsyncMock(asyncpg.pool.Pool)


@pytest.fixture
async def postgres_backend(asyncpg_pool):
    """Fixture for the PostgresBackend object."""
    return PostgresBackend(pool=asyncpg_pool)


@pytest.mark.asyncio
async def test_get(postgres_backend, asyncpg_pool, queries):
    """Test the get method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    key = "test_key"
    asyncpg_pool.acquire.return_value.__aenter__.return_value.fetchval.return_value = (
        json.dumps({"data": "test_value"})
    )

    result = await postgres_backend.get(key)

    asyncpg_pool.acquire.return_value.__aenter__.return_value.fetchval.assert_called_once_with(
        queries.get_cache_entry.sql,
        key,
    )
    assert result == {"data": "test_value"}


@pytest.mark.asyncio
async def test_set(postgres_backend, asyncpg_pool, queries):
    """Test the set method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    key = "test_key"
    value = {"data": "test_value"}
    ttl = 60
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute = AsyncMock()

    await postgres_backend.set(key, value, ttl)
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute.assert_called_once_with(
        queries.set_cache_entry.sql,
        key,
        json.dumps(value),
        ttl,
    )


@pytest.mark.asyncio
async def test_delete(postgres_backend, asyncpg_pool, queries):
    """Test the delete method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    key = "test_key"
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute = AsyncMock()

    await postgres_backend.delete(key)
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute.assert_called_once_with(
        queries.delete_cache_entry.sql,
        key,
    )


@pytest.mark.asyncio
async def test_clear(postgres_backend, asyncpg_pool, queries):
    """Test the clear method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute = AsyncMock()

    await postgres_backend.clear()
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute.assert_called_once_with(
        queries.clear_cache_entries.sql,
    )


@pytest.mark.asyncio
async def test_cleanup(postgres_backend, asyncpg_pool, queries):
    """Test the cleanup method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute = AsyncMock()

    await postgres_backend.cleanup()
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute.assert_called_once_with(
        queries.cleanup_expired_cache_entries.sql,
    )


@pytest.mark.asyncio
async def test_has(postgres_backend, asyncpg_pool, queries):
    """Test the has method for the PostgresBackend.

    Args:
        postgres_backend (PostgresBackend): The PostgresBackend object.
        asyncpg_pool (AsyncMock): The pool object.
        queries (Queries): The queries object.
    """
    key = "test_key"
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute = AsyncMock(
        return_value=True,
    )

    result = await postgres_backend.has(key)
    assert result is True
    asyncpg_pool.acquire.return_value.__aenter__.return_value.execute.assert_called_once_with(
        queries.has_cache_entry.sql,
        key,
    )
