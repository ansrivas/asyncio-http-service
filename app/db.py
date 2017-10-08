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
    pool = await asyncpg.create_pool(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        min_size=config['poolsize_min'],
        max_size=config['poolsize_max'],
    )
    return pool
