"""This module holds the SQL queries used in the application.

This module loads SQL queries from a file and provides them as an object.
"""

import aiosql

from psqache.conf import QUERY_FILE_PATH

Queries = aiosql.from_path(QUERY_FILE_PATH, "asyncpg")
