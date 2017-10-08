# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""All the routes go here."""

import aiohttp_jinja2
from aiohttp import web
from app.routes.todos import todos_app


class Index(web.View):
    """Index page for the server."""

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        """Return a simple hello."""
        return {
            'new_todo_url': todos_app.router['new_todo'].url_for(),
            'list_todo_url': todos_app.router['list_todo'].url_for(),
            'completed_todo_url': todos_app.router['completed_todo'].url_for(),
        }

    # @aiohttp_jinja2.template('index.html')
    # async def get(self):
    #     async with self.request.app['db'].transaction() as conn:
    #         results = await get_all_clients(conn)
    #     return
