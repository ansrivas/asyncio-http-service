# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""All the todo routes go here."""

import aiohttp_jinja2
from aiohttp import web


class TodoHandler():
    """Index page for the server."""

    def __init__(self):
        """."""
        pass

    async def new_todo(self, request):
        """Return a simple hello."""
        return web.Response(text="This end point will take you to a new todo registration")

    async def list_todo(self, request):
        """Return a simple hello."""
        return web.Response(text="This end point will show a list of all the todos")

    async def completed_todo(self, request):
        """Return a simple hello."""
        return web.Response(text="This end point will show a list of completed todos with option to delete")
    # @aiohttp_jinja2.template('index.html')
    # async def post(self):
    #     async with self.request.app['db'].transaction() as conn:
    #         results = await get_all_clients(conn)
    #     return


todo_handler = TodoHandler()
todos_app = web.Application()
todos_app.router.add_get('/new_todo', todo_handler.new_todo, name='new_todo')
todos_app.router.add_get('/list_todo', todo_handler.list_todo, name='list_todo')
todos_app.router.add_get('/completed_todo', todo_handler.completed_todo, name='completed_todo')
