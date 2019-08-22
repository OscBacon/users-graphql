#!/usr/bin/env python

import sys

from aiohttp import web

from users.app import init_app


if __name__ == '__main__':
    app = init_app()
    sys.exit(web.run_app(app))
