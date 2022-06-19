from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from tortoise.contrib.fastapi import register_tortoise

from StatusService.models.config import TORTOISE_CONFIG
from StatusService.web.api.router import api_router
from StatusService.web.lifetime import register_shutdown_event, register_startup_event


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="StatusService",
        description="",
        version='1',
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    register_startup_event(app)
    register_shutdown_event(app)

    app.include_router(router=api_router, prefix="/api")
    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        add_exception_handlers=True,
        generate_schemas=True
    )

    return app
