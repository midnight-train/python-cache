# psqache

A blazing-fast Cache Client Library for Python/asyncio powered by PostgreSQL

![PyPI](https://img.shields.io/pypi/v/psqache)
![Python](https://img.shields.io/pypi/pyversions/psqache)
![License](https://img.shields.io/github/license/midnight-train/python-cache)

## The Problem

It's the year 2099, and yes, we're still building high-performance backends. You'd think by now we'd have some universal, one-size-fits-all infrastructure solution, but no.

Instead, we're juggling multiple services: caches, message queues, databases — all to keep our apps blazing fast and reliable.

The typical backend stack looks something like this:

- `Redis` to cache the stuff we hit over and over
- `RabbitMQ` or Kafka for message queues to handle background tasks
- `PostgreSQL` for the real, persistent data

This multi-tool setup works, but it brings baggage:

- Multiple services to set up and maintain
- Complex monitoring and security configurations
- More potential points of failure
- Higher infrastructure costs
- Increased operational complexity

## Enter psqache: The Simplicity Play

What if your friendly, reliable PostgreSQL could handle both persistence AND caching? That's where `psqache` comes in.

`psqache` lets you:

- Use PostgreSQL as a high-performance cache
- Eliminate the need for separate caching services
- Reduce infrastructure complexity and costs
- Maintain high performance at scale
- Keep your stack simple and reliable

## Features

- 🚀 **Blazing Fast**: Optimized for high-throughput caching operations
- 🔄 **Async First**: Built for Python/asyncio with concurrency in mind
- 🛠 **Simple API**: Familiar cache interface (`get`, `set`, `delete`)
- ⏰ **TTL Support**: Automatic key expiration
- 🔍 **JSONB Storage**: Native support for complex data structures
- 🎯 **Type Safe**: Full typing support for modern Python
- 📊 **Monitoring**: Built-in metrics for cache operations

## Quick Start

TODO

## Why PostgreSQL?

PostgreSQL is the perfect foundation for a caching layer because:

- **Reliability**: Built-in durability and consistency guarantees
- **Performance**: Optimized for high-concurrency workloads
- **Flexibility**: Native JSONB support for complex data structures
- **Familiarity**: Uses technology you already know and trust
- **Simplicity**: One less service to maintain and monitor

Under the hood, `psqache` uses:

- Unlogged tables for maximum performance
- Computed expiration fields for automatic cleanup
- Optimized indexes for fast lookups
- Connection pooling for concurrent access

## Performance

TODO

## Configuration

TODO

## Contributing

TODO

## Roadmap

TODO

---

Built with ❤️ by [Midnight Train]
