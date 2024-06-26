from fastapi import FastAPI

from .base import api_router
from src.shop.adapters.db.orm import start_mappers
from src.shop.config.containers import Container


def include_router(app_):
    app_.include_router(api_router)


def start_application():
    container = Container()
    app_ = FastAPI()
    app_.container = container
    include_router(app_)
    # start ORM mappers
    try:
        start_mappers()
    except Exception as err:
        # Checking if the mapper was already started
        if "already has a primary mapper defined" not in str(err):
            raise RuntimeError(err) from err
    return app_


app = start_application()
