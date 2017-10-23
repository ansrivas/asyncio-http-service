# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of db services to be used across the application."""

from typing import List
from app.models import users, todos
from asyncpg import Record, Connection
from app.utils import DataStatus, tzware_datetime


async def create_tables(conn: Connection)->None:
    """Create all the tables and indices required for this app."""
    async with conn.transaction():
        await conn.execute(users.users_creation)
        await conn.execute(users.users_index_creation)
        await conn.execute(todos.todos_creation)
        await conn.execute(todos.todos_index_creation)


async def delete_tables(conn: Connection)->None:
    """Delete all the tables/indices used in this app."""
    async with conn.transaction():
        await conn.execute(users.users_index_deletion)
        await conn.execute(todos.todos_index_deletion)
        await conn.execute(users.users_deletion)
        await conn.execute(todos.todos_deletion)


async def reset_tables(conn: Connection)->None:
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


async def insert_user(conn: Connection, email_address)-> DataStatus(List[Record], str, bool):
    """Insert a new user given email_address."""
    sql = "INSERT INTO users(created_timestamp, modified_timestamp, email_address) VALUES ($1, $2, $3);"
    now = tzware_datetime()
    try:
        async with conn.transaction():
            result = await conn.execute(sql, now, now, email_address)
            if result == "INSERT 0 1":
                return DataStatus([],  "Successfully registered the customers", True)

            return DataStatus([], "Something went wrong", False)
    except Exception as ex:
        return DataStatus([], ex.message, False)
