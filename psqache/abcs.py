"""This module contains the interfaces/protocols/abstract classes.

The interfaces are used to define the public API of the classes in the
module. They are used to define the expected behavior of the classes
and to provide a way to check if a class implements the expected
behavior.
"""

from typing import Any
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class ICache(Protocol):
    """Interface for cache engine implementations.

    This interface defines the expected behavior for cache engines, including methods
    for getting, setting, deleting, and checking the existence of cache entries, both
    synchronously and asynchronously.

    Methods:
        aget(key: str) -> Optional[Any]: Asynchronously get the value for the given key.
        get(key: str) -> Optional[Any]: Get the value for the given key.
        aset(key: str, value: Any, ttl: Optional[int] = None) -> None: Asynchronously
            set the value for the given key.
        set(key: str, value: Any, ttl: Optional[int] = None) -> None: Set the value
            for the given key.
        adelete(key: str) -> None: Asynchronously delete the value for the given key.
        delete(key: str) -> None: Delete the value for the given key.
        aclear() -> None: Asynchronously remove all the entries in the cache.
        clear() -> None: Remove all the entries in the cache.
        acleanup() -> None: Asynchronously remove the expired entries in the cache.
        cleanup() -> None: Remove the expired entries in the cache.
        ahas(key: str) -> bool: Asynchronously check if the given key is in the cache.
        has(key: str) -> bool: Check if the given key is in the cache.
    """

    async def aget(self, key: str) -> Any | None:
        """Get the value for the given key asynchronously.

        Args:
            key (str): The key to get the value for.

        Returns:
            Optional[Any]: The value for the given key.
        """
        ...

    def get(self, key: str) -> Any | None:
        """Get the value for the given key.

        Args:
            key (str): The key to get the value for.

        Returns:
            Optional[Any]: The value for the given key.
        """
        ...

    async def aset(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Set the value for the given key asynchronously.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set for the given key.
            ttl (Optional[int], optional): Time to live. Defaults to None.
        """
        ...

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Set the value for the given key.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to set for the given key.
            ttl (Optional[int], optional): Time to live. Defaults to None.
        """
        ...

    async def adelete(self, key: str) -> None:
        """Delete the value for the given key asynchronously.

        Args:
            key (str): The key to delete the value for.
        """
        ...

    def delete(self, key: str) -> None:
        """Delete the value for the given key.

        Args:
            key (str): The key to delete the value for.
        """

    async def aclear(self) -> None:
        """Remove all the entries in the cache asynchronously."""
        ...

    def clear(self) -> None:
        """Remove all the entries in the cache."""

    async def acleanup(self) -> None:
        """Remove the expired entries in the cache asynchronously."""
        ...

    def cleanup(self) -> None:
        """Remove the expired entries in the cache."""
        ...

    async def ahas(self, key: str) -> bool:
        """Check if the given key is in the cache asynchronously.

        Args:
            key (str): The key to check for.

        Returns:
            bool: True if the key is in the cache, False otherwise.
        """
        ...

    def has(self, key: str) -> bool:
        """Check if the given key is in the cache.

        Args:
            key (str): The key to check for.

        Returns:
            bool: True if the key is in the cache, False otherwise.
        """
        ...


@runtime_checkable
class ICacheBackend(Protocol):
    """Interface for cache backends implementations.

    This interface defines the expected behavior for backend classes, including
    methods for getting, setting, deleting, and checking the existence of entries
    asynchronously.

    Methods:
        get(key: str) -> Optional[dict]: Get the value for the given key.
        set(key: str, value: dict, ttl: int) -> None: Set the value for the given key.
        delete(key: str) -> None: Delete the value for the given key.
        clear() -> None: Remove all the entries in the repository.
        cleanup() -> None: Remove the expired entries in the repository.
        has(key: str) -> bool: Check if the given key is in the repository.
    """

    async def get(self, key: str) -> dict | None:
        """Retrieve a cache entry by key.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key, or None if not found or expired.
        """
        ...

    async def set(self, key: str, value: dict, ttl: int) -> None:
        """Set or update a cache entry with a time-to-live.

        Args:
            key: The key to set.
            value: The value to associate with the key.
            ttl: Time-to-live in seconds for the entry.
        """
        ...

    async def delete(self, key: str) -> None:
        """Delete a cache entry by key.

        Args:
            key: The key to delete.
        """
        ...

    async def clear(self) -> None:
        """Clear all cache entries."""
        ...

    async def cleanup(self) -> None:
        """Delete all expired cache entries."""
        ...

    async def has(self, key: str) -> bool:
        """Check if a cache entry exists and is not expired.

        Args:
            key: The key to check.

        Returns:
            True if the entry exists and is not expired, otherwise False.
        """
        ...
