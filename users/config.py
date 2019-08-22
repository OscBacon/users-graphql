import dotenv
import os
from aiohttp import web


ENVVARS = [
    "LOG_LEVEL",
]


def get_config() -> dict:
    dotenv.load_dotenv()
    return {envvar: os.getenv(envvar) for envvar in ENVVARS}


def init_config(app: web.Application) -> None:
    app["config"] = get_config()
