# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""All the routes go here."""

import aiohttp_jinja2
from aiohttp import web


class Index(web.View):
    """Index page for the server."""

    async def get(self):
        """Return a simple hello."""
        return web.Response(text="Hello, world")

    # @aiohttp_jinja2.template('index.html')
    # async def get(self):
    #     async with self.request.app['db'].transaction() as conn:
    #         results = await get_all_clients(conn)
    #     return
