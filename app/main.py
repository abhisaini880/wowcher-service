""" Main module to create Fastapi app"""

# --- Standard library imports --- #

# --- Related third party imports --- #
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .apis.health import status_router

# --- Local application/library specific imports --- #
from .core.config import settings
from .core.exceptions.base import CustomException
from .core.exceptions.exception_handler import (
    custom_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    pydantic_validation_exception_handler,
    request_validation_exception_handler,
)
from .databases.mysql import Base, engine
from .routes import routes_v1
from .utils.api_doc import generate_api_doc

api_doc = generate_api_doc()


def create_app():
    """
    Create fast api app with the meta data and middleware data

    Returns:
        obj: fastapi app object
    """
    _app = FastAPI(
        docs_url=api_doc.docs_url,
        redoc_url=api_doc.redoc_url,
    )
    allowed_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(status_router)
    _app.include_router(routes_v1.router, prefix="/v1")

    return _app


app = create_app()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=api_doc.title,
        version=api_doc.version,
        description=api_doc.description,
        routes=app.routes,
        tags=api_doc.tags_metadata,
        license_info=api_doc.license_info,
    )
    openapi_schema["info"]["x-logo"] = {"url": api_doc.logo}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.add_exception_handler(
    RequestValidationError, request_validation_exception_handler
)
app.add_exception_handler(
    ValidationError, pydantic_validation_exception_handler
)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(CustomException, custom_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
