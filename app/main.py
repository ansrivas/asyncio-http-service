# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point of the app."""

import uvloop
import asyncio
from aiohttp import web
from app.db import init_db, close_db
from app.routes.index import Index
from app.utils import read_config_from_env


def setup_routes(app):
    """Setup all the routes here."""
    # app.router.add_route('*', '/', Index)

    index_resource = app.router.add_resource(r'/', name='index')
    index_resource.add_route('GET', Index)


def create_app():
    """Configure and create the aiohttp app."""
    # Create a uvloop
    loop = uvloop.new_event_loop()

    # Assing it to asyncio
    asyncio.set_event_loop(loop)

    app = web.Application()
    app['config'] = read_config_from_env('config_file')
    # app['pool'] = asyncio.get_event_loop().run_until_complete(init_db(config=app['config']))

    # aiohttp_jinja2.setup(
    #     app, loader=jinja2.PackageLoader('datemanager', 'templates'))

    # another way to create connection to the database
    app.on_startup.append(init_db)

    # shutdown db connection on exit
    app.on_cleanup.append(close_db)

    # setup views and routes
    setup_routes(app)

    # setup_middlewares(app)
    return app


app = create_app()
