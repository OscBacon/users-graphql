#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

from aiohttp import web
from tartiflette import Engine
from tartiflette_aiohttp import register_graphql_handlers

from users import version as app_version
from users.config import init_config


engine = Engine(
    [
        os.path.dirname(os.path.abspath(__file__)) + "/sdl/queries.graphql",
        os.path.dirname(os.path.abspath(__file__)) + "/sdl/directives.graphql",
    ],
    modules=[
        "users.resolvers.resolvers",
    ],
)

async def version(request):
    response = {"version": app_version}
    return web.json_response(response)


async def init_app():
    app = web.Application()

    init_config(app)  # must be first

    logging.basicConfig(
        level=getattr(logging, app["config"]["LOG_LEVEL"]),
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    )

    app.router.add_get('/', version)
    app.router.add_get('/version', version)

    return register_graphql_handlers(
        app=app,
        engine=engine,
        executor_http_endpoint="/graphql",
        executor_http_methods=["POST", "GET"],
        graphiql_enabled=True,
    )
