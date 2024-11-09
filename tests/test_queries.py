def test_create_psqache_table(queries):
    """Test the create_psqache_table method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "create_psqache_table")
    assert "create_psqache_table" in queries._available_queries
    assert queries.create_psqache_table.sql.startswith(
        "CREATE UNLOGGED TABLE IF NOT EXISTS psqache"
    )


def test_set_cache_entry(queries):
    """Test the set_cache_entry method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "set_cache_entry")
    assert "set_cache_entry" in queries._available_queries


def test_get_cache_entry(queries):
    """Test the get_cache_entry method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "get_cache_entry")
    assert "get_cache_entry" in queries._available_queries


def test_delete_cache_entry(queries):
    """Test the delete_cache_entry method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "delete_cache_entry")
    assert "delete_cache_entry" in queries._available_queries


def test_clear_cache_entries(queries):
    """Test the clear_cache method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "clear_cache_entries")
    assert "clear_cache_entries" in queries._available_queries


def test_cleanup_expired_cache_entries(queries):
    """Test the cleanup_expired_cache_entries method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "cleanup_expired_cache_entries")
    assert "cleanup_expired_cache_entries" in queries._available_queries


def test_has_cache_entry(queries):
    """Test the has_cache_entry method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "has_cache_entry")
    assert "has_cache_entry" in queries._available_queries


def test_drop_cache_table(queries):
    """Test the drop_cache_table method.

    Args:
        queries (Queries): The queries object.
    """
    assert hasattr(queries, "drop_cache_table")
    assert "drop_cache_table" in queries._available_queries
    assert queries.drop_cache_table.sql.startswith("DROP TABLE IF EXISTS psqache")
