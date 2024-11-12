from unittest.mock import AsyncMock
from unittest.mock import patch

import pytest

from psqache.caches import PsQache
from psqache.abcs import ICache
from psqache.abcs import ICacheBackend


@pytest.fixture
def backend():
    """Fixture for the cache backend."""
    backend = AsyncMock(spec=ICacheBackend)
    return backend


@pytest.fixture
def cache(backend):
    """Fixture for the cache object."""
    return PsQache(backend=backend)


@pytest.mark.asyncio
async def test_aget(cache, backend):
    """Test the aget method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    backend.get.return_value = {"key": "value"}
    result = await cache.aget("test_key")
    backend.get.assert_awaited_once_with("test_key")
    assert result == {"key": "value"}


def test_get(cache, backend):
    """Test the get method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    backend.get.return_value = {"key": "value"}
    result = cache.get("test_key")
    backend.get.assert_called_once_with("test_key")
    assert result == {"key": "value"}


@pytest.mark.asyncio
async def test_aset(cache, backend):
    """Test the aset method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    await cache.aset("test_key", "test_value", 100)
    backend.set.assert_awaited_once_with("test_key", "test_value", 100)


def test_set(cache, backend):
    """Test the set method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    cache.set("test_key", "test_value", 100)
    backend.set.assert_called_once_with("test_key", "test_value", 100)


@pytest.mark.asyncio
async def test_adelete(cache, backend):
    """Test the adelete method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    await cache.adelete("test_key")
    backend.delete.assert_awaited_once_with("test_key")


def test_delete(cache, backend):
    """Test the delete method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    cache.delete("test_key")
    backend.delete.assert_called_once_with("test_key")


@pytest.mark.asyncio
async def test_ahas(cache, backend):
    """Test the ahas method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    backend.has.return_value = True
    result = await cache.ahas("test_key")
    backend.has.assert_awaited_once_with("test_key")
    assert result is True


def test_has(cache, backend):
    """Test the has method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    backend.has.return_value = True
    result = cache.has("test_key")
    backend.has.assert_called_once_with("test_key")
    assert result is True


@pytest.mark.asyncio
async def test_aclear(cache, backend):
    """Test the aclear method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    await cache.aclear()
    backend.clear.assert_awaited_once()


def test_clear(cache, backend):
    """Test the clear method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    cache.clear()
    backend.clear.assert_called_once()


@pytest.mark.asyncio
async def test_acleanup(cache, backend):
    """Test the acleanup method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    await cache.acleanup()
    backend.cleanup.assert_awaited_once()


def test_cleanup(cache, backend):
    """Test the cleanup method for the PsQache cache.

    Args:
        cache (PsQache): The PsQache cache object.
        backend (AsyncMock): The backend object.
    """
    cache.cleanup()
    backend.cleanup.assert_called_once()


def test_use_postgres_backend():
    """Test the use_postgres_backend method for the PsQache class."""
    with patch("psqache.caches.asyncpg.create_pool") as create_pool:
        cache = PsQache.use_postgres_backend(dsn="test_dsn")
        assert isinstance(cache.backend, ICacheBackend)
        assert isinstance(cache, ICache)
        create_pool.assert_called_once_with(dsn="test_dsn", min_size=15, max_size=25)
