"""This module holds the configuration for the application.

The configuration is loaded from environment variables.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
QUERIES_FILE_PATH = ROOT_DIR / "psqache/queries.sql"
