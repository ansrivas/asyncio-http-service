# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to handle database operations."""

import asyncpg


async def init_db(app=None, config=None):
    """Initialize a database based on a given config json and return the pool object.

    Args:
        config (yaml)   : A config file containing username, password, database,
            host, port, pool_maxsize, pool_minseize
    Returns:
        pool object
    """
    # TODO: Looks a bit hacky (but this is just to enable testing of init_db)
    if not config:
        config = app['config']

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

    if app:
        app['pool'] = pool
    return pool


async def close_db(app):
    """Gracefully close the pool of connections to postgres.

    Args:
        app (object)    : Asyncio web app object
    """
    await app['pool'].close()
