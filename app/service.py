# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of db services to be used across the application."""

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
