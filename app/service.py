# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of db services to be used across the application."""

from typing import List
from asyncpg import Connection
from asyncpg import Record
from app.utils import DataStatus
from app.models import users, todos


async def create_tables(conn):
    """Create all the tables required for this app."""
    async with conn.transaction():
        # Run the query passing the request argument.
        await conn.execute(users.users_creation)
        await conn.execute(users.users_index_creation)
        await conn.execute(todos.todos_creation)
        await conn.execute(todos.todos_index_creation)


async def delete_tables(conn):
    """Create all the tables required for this app."""
    async with conn.transaction():
        # Run the query passing the request argument.
        await conn.execute(users.users_index_deletion)
        await conn.execute(todos.todos_index_deletion)
        await conn.execute(users.users_deletion)
        await conn.execute(todos.todos_deletion)


async def reset_tables(conn):
    """Create all the tables required for this app."""
    async with conn.transaction():
        # Run the query passing the request argument.
        await delete_tables(conn)
        await create_tables(conn)


async def get_all_users(conn: Connection)-> List[Record]:
    """Return all the registered users for this app."""
    sql = "select email_address from public.users;"
    async with conn.transaction():
        results = await conn.fetch(sql)

    if not len(results):
        # TODO: use a named tuple here or just tuple as did in previous application.
        msg = "No registered users found"
        return DataStatus(None, msg, False)
    return DataStatus(results, "", True)
