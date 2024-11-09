"""This module contains global fixtures for the tests."""

import pytest

from tests.mocks import MockCache
from psqache.queries import Queries


@pytest.fixture
def cache():
    """Fixture for the cache object."""
    return MockCache()


@pytest.fixture
def queries():
    """Fixture for the query object."""
    return Queries
