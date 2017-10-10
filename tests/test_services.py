# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tables creations utitlities."""

import pytest
from app.service import get_all_users, insert_user


@pytest.mark.asyncio
async def test_get_all_users(pool_with_tables):
    """."""
    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            status = await get_all_users(conn)

    assert not status.data
    assert not status.is_success
    assert status.message == "No registered users found"


@pytest.mark.asyncio
async def test_get_one_user(pool_with_tables):
    """."""
    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            await conn.execute('''INSERT INTO users(id, created_timestamp, modified_timestamp, email_address) \
            VALUES (1, '2016-11-12', '2016-11-13', 'myemail@gmail.com')''')

    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            status = await get_all_users(conn)

    assert status.data[0]['email_address'] == "myemail@gmail.com"
    assert status.is_success
    assert status.message == ""


@pytest.mark.asyncio
async def test_insert_one_user(pool_with_tables):
    """."""
    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            status = await insert_user(conn, "ankur@gmail.com")

    assert not status.data
    assert status.is_success
    assert "Successfully registered" in status.message

    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            status = await conn.fetch("select * from users")

    assert len(status) == 1


@pytest.mark.asyncio
async def test_insert_same_user_two_times(pool_with_tables):
    """."""
    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            status = await insert_user(conn, "ankur@gmail.com")
            status = await insert_user(conn, "ankur@gmail.com")

    assert not status.data
    assert not status.is_success
    assert "violates unique constraint" in status.message
