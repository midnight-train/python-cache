"""Package for caching data from PostgreSQL database.

This package provides a way to cache data from a PostgreSQL database to
improve the performance of applications that need to access the same
data multiple times.

The motivation for this package is to reduce infrastructure complexity
and costs by reducing the number of services/instances needed to be deployed
to support the application.

By taking advantage of Postgres abilities, we can use it as:
- A persistent store for application data.
- A cache for frequently accessed data.
- A message queue for asynchronous processing.

We can eliminate the need for additional services like Redis, Memcached,
or RabbitMQ, which can reduce the complexity of the infrastructure and
reduce the costs associated with deploying and maintaining these services.

The package provides a way to cache data using a PostgreSQL database.
"""
