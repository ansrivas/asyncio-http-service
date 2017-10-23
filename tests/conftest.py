# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of fixtures to be used across the tests."""

import os
import pytest
import pathlib
from collections import namedtuple
from app.db import init_db
from app.utils import read_config
from app.service import delete_tables, create_tables

file_parent = pathlib.Path(__file__).parent


@pytest.fixture(scope="function")
def config(request):
    """."""
    good_yaml = "data/config.yaml"
    bad_yaml = "data/wrong_config.yaml"
    good_filepath = os.path.join(file_parent, good_yaml)
    bad_filepath = os.path.join(file_parent, bad_yaml)

    Config = namedtuple("Config", "good_filepath bad_filepath")

    def tear_down():
        pass

    request.addfinalizer(tear_down)
    return Config(good_filepath, bad_filepath)


@pytest.fixture(scope="function")
async def pool(request, config, event_loop):
    """Create a db conneciton from a given config."""
    pool = await init_db(config=read_config(config.good_filepath))

    def tear_down():
        async def cleanup():
            # Event loop was not available here, so this little hack
            # https://github.com/pytest-dev/pytest-asyncio/issues/59
            async with pool.acquire() as conn:
                await delete_tables(conn)
            await pool.close()
        event_loop.run_until_complete(cleanup())

    request.addfinalizer(tear_down)
    return pool


@pytest.fixture(scope="function")
async def pool_with_tables(request, config, event_loop):
    """Create a db conneciton from a given config."""
    pool = await init_db(config=read_config(config.good_filepath))

    async with pool.acquire() as conn:
        async with conn.transaction():
            await create_tables(conn)

    def tear_down():
        async def cleanup():
            # Event loop was not available here, so this little hack
            # https://github.com/pytest-dev/pytest-asyncio/issues/59
            async with pool.acquire() as conn:
                await delete_tables(conn)
            await pool.close()
        event_loop.run_until_complete(cleanup())

    request.addfinalizer(tear_down)
    return pool
