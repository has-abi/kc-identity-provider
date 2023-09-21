import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config import Settings, get_settings
from src.containers import Container
from src.apis.auth_api import auth_router


def server(settings: Settings = get_settings()) -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        docs_url=f"{settings.API_PREFIX}/docs",
    )
    app.include_router(auth_router, prefix=settings.API_PREFIX)
    container = Container()
    app.container = container  # type: ignore
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
