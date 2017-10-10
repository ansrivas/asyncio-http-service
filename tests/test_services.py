# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tables creations utitlities."""

import pytest
from app.service import get_all_users


@pytest.mark.asyncio
async def test_get_all_users(pool_with_tables):
    """."""
    async with pool_with_tables.acquire() as conn:
        async with conn.transaction():
            users = await get_all_users(conn)

    assert users is None
