"""This module contains global fixtures for the tests."""

import pytest

from psqache.queries import Queries


@pytest.fixture
def queries():
    """Fixture for the query object."""
    return Queries
