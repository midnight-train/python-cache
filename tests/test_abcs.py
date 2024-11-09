"""This module contains tests for the ABCs/Protocols."""

import pytest


@pytest.mark.asyncio
async def test_async_get_set(cache):
    """Test the async get and set methods.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    await cache.aset("key1", "value1")
    assert await cache.aget("key1") == "value1"


def test_sync_get_set(cache):
    """Test the sync get and set methods.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"


@pytest.mark.asyncio
async def test_async_delete(cache):
    """Test the async delete method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    await cache.aset("key1", "value1")
    await cache.adelete("key1")
    assert await cache.aget("key1") is None


def test_sync_delete(cache):
    """Test the sync delete method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    cache.set("key1", "value1")
    cache.delete("key1")
    assert cache.get("key1") is None


@pytest.mark.asyncio
async def test_async_clear(cache):
    """Test the async clear method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    await cache.aset("key1", "value1")
    await cache.aclear()
    assert await cache.aget("key1") is None


def test_sync_clear(cache):
    """Test the sync clear method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    cache.set("key1", "value1")
    cache.clear()
    assert cache.get("key1") is None


@pytest.mark.asyncio
async def test_async_has(cache):
    """Test the async has method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    await cache.aset("key1", "value1")
    assert await cache.ahas("key1") is True
    assert await cache.ahas("key2") is False


def test_sync_has(cache):
    """Test the sync has method.

    Args:
        cache (CacheProtocol): The cache object implement the CacheProtocol.
    """
    cache.set("key1", "value1")
    assert cache.has("key1") is True
    assert cache.has("key2") is False
