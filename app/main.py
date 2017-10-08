# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point of the app."""

import uvloop
import jinja2
import pathlib
import asyncio
import logging
import aiohttp_jinja2
from aiohttp import web
from app.routes.index import Index
from app.routes.todos import todos_app
from app.db import init_db, close_db
from app.utils import read_config_from_env

logger = logging.getLogger(__name__)
PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    """Setup all the routes here."""
    # app.router.add_route('*', '/', Index)

    index_resource = app.router.add_resource(r'/', name='index')
    index_resource.add_route('GET', Index)

    app.add_subapp(r'/api/v1/todo', todos_app)

    app.router.add_static('/static/',
                          path=str(PROJECT_ROOT / 'static'),
                          name='static')

    # for resource in app.router.resources():
    #     print(resource)
    # for name, resource in app.router.named_resources().items():
    #     print(name, resource)


def create_app():
    """Configure and create the aiohttp app."""
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    app = web.Application()
    app['config'] = read_config_from_env('config_file')
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('app', 'templates'))

    setup_routes(app)

    return app


app = create_app()
