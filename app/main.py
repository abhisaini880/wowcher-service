from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from .core.config import settings
from .databases.mysql import engine, Base
from .apis.health import status_router
from .routes import routes_v1
from .core.exceptions.base import CustomException
from .core.exceptions.exception_handler import (
    custom_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    pydantic_validation_exception_handler,
    request_validation_exception_handler,
)

from fastapi import APIRouter, Request, Response
from typing import Callable
from fastapi.routing import APIRoute

# Handle CORS
class CORSHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def preflight_handler(request: Request) -> Response:
            if request.method == "OPTIONS":
                response = Response()
                response.headers["Access-Control-Allow-Origin"] = "*"
                response.headers[
                    "Access-Control-Allow-Methods"
                ] = "POST, GET, DELETE, OPTIONS"
                response.headers[
                    "Access-Control-Allow-Headers"
                ] = "Authorization, Content-Type"
            else:
                response = await original_route_handler(request)

            return response

        return preflight_handler


router = APIRouter(route_class=CORSHandler)


def create_app():
    """_summary_

    Returns:
        _type_: _description_
    """
    _app = FastAPI(
        title="Wowcher-Service",
        docs_url=None,
        redoc_url="/api/documentation",
    )
    allowed_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # _app.add_middleware(RawContextMiddleware)

    _app.include_router(status_router)
    _app.include_router(routes_v1.router, prefix="/v1")
    _app.include_router(router)

    return _app


app = create_app()


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
