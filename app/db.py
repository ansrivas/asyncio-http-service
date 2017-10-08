# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to handle database operations."""

import asyncpg


async def init_db(config):
    """Initialize a database based on a given config json and return the pool object.

    Args:
        config (yaml)   : A config file containing username, password, database,
            host, port, pool_maxsize, pool_minseize
    Returns:
        pool object
    """
    postgres = config['postgres']
    pool = await asyncpg.create_pool(
        database=postgres['database'],
        user=postgres['user'],
        password=postgres['password'],
        host=postgres['host'],
        port=postgres['port'],
        min_size=postgres['poolsize_min'],
        max_size=postgres['poolsize_max'],
    )
    return pool


async def close_pg(app):
    """Gracefully close the pool of connections to postgres.

    Args:
        app (object)    : Asyncio web app object
    """
    await app['db_pool'].close()
