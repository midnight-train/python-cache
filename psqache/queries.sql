-- name: create_psqache_table
/*
 Create a table to store cache entries.

 The table has the following columns:
 - key (TEXT): The key of the cache entry.
 - value (JSONB): The value of the cache entry.
 - ttl (INT): The time-to-live of the cache entry in seconds.
 - created_at (TIMESTAMP): The time when the cache entry was created.
 - expires_at (TIMESTAMP): The time when the cache entry will expire.

 The table is unlogged to avoid writing cache entries to the WAL.
 */
CREATE UNLOGGED TABLE IF NOT EXISTS psqache (
    key TEXT PRIMARY KEY,
    value JSONB NOT NULL,
    ttl INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE GENERATED ALWAYS AS (
        created_at + (ttl || ' seconds')::INTERVAL
    ) STORED
);
-- Index on expires_at column to speed up cleanup of expired cache entries.
CREATE INDEX IF NOT EXISTS idx_expires_at ON psqache (expires_at)
WHERE expires_at <= NOW();
-- name: set_cache_entry
/*
 Set a cache entry.

 If a cache entry with the given key already exists, update it.
 Otherwise, insert a new cache entry.

 The cache entry will expire after the given time-to-live (ttl) in seconds.
 This function automatically updates `created_at` for existing entries to
 reset the expiration time.
 */
DO $$ BEGIN
INSERT INTO psqache (key, value, ttl, created_at)
VALUES ($1, $2, $3, NOW()) ON CONFLICT (key) DO
UPDATE
SET value = EXCLUDED.value,
    ttl = EXCLUDED.ttl,
    created_at = NOW();
END $$;
-- name: get_cache_entry
/*
 Get a cache entry by key.

 If the cache entry exists and has not expired, return the value.
 Otherwise, return NULL.
 */
SELECT value
FROM psqache
WHERE
    key = $1
    AND expires_at > NOW();
-- name: delete_cache_entry
/*
 Delete a cache entry by key.

 If the cache entry exists, delete it. If the cache entry with the specified
 key does not exist, no action is taken.
 */
DELETE FROM psqache
WHERE key = $1;
-- name: clear_cache_entries
/*
 Clear all cache entries.
 */
TRUNCATE psqache;
-- name: cleanup_expired_cache_entries
/*
 Cleanup expired cache entries.

 Delete all cache entries that have expired.
 */
DELETE FROM psqache
WHERE expires_at <= NOW();
-- name: has_cache_entry
/*
 Check if a cache entry exists by key.

 Return TRUE if the cache entry exists and has not expired.
 Otherwise, return FALSE.
 */
SELECT EXISTS(
    SELECT 1
    FROM psqache
    WHERE
        key = $1
        AND expires_at > NOW()
) AS entry_exists;
-- name: drop_cache_table
/*
 Drop the cache table.
 */
DROP TABLE IF EXISTS psqache;
