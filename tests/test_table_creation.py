# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tables creations utitlities."""

import pytest
from app.service import create_tables


@pytest.mark.asyncio
async def test_table_creations(pool):
    """."""
    # Take a connection from the pool.
    async with pool.acquire() as conn:
        await create_tables(conn)
        async with conn.transaction():
            users = await conn.execute("""SELECT 'public.users'::regclass""")
            todos = await conn.execute("""SELECT 'public.todos'::regclass""")
    assert users, todos
