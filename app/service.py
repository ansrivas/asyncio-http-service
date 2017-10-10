# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of db services to be used across the application."""

from typing import List
from asyncpg import Connection
from asyncpg import Record
from app.utils import DataStatus
from app.models import users, todos


async def create_tables(conn):
    """Create all the tables and indices required for this app."""
    async with conn.transaction():
        await conn.execute(users.users_creation)
        await conn.execute(users.users_index_creation)
        await conn.execute(todos.todos_creation)
        await conn.execute(todos.todos_index_creation)


async def delete_tables(conn):
    """Delete all the tables/indices used in this app."""
    async with conn.transaction():
        await conn.execute(users.users_index_deletion)
        await conn.execute(todos.todos_index_deletion)
        await conn.execute(users.users_deletion)
        await conn.execute(todos.todos_deletion)


async def reset_tables(conn):
    """Delete and create all the tables used in this app."""
    async with conn.transaction():
        await delete_tables(conn)
        await create_tables(conn)


async def get_all_users(conn: Connection)-> DataStatus(List[Record], str, bool):
    """Return all the registered users for this app."""
    sql = "select email_address from public.users;"
    async with conn.transaction():
        results = await conn.fetch(sql)

    if len(results) == 0:
        return DataStatus([],  "No registered users found", False)

    return DataStatus(results, "", True)
