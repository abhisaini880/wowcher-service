import traceback

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from structlog import get_logger

from .base import CustomException
from .generic import (
    CustomHTTPException,
    CustomRequestValidationException,
    InternalServerErrorException,
)

logger = get_logger()


def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        jsonable_encoder(exc.response), status_code=exc.status_code
    )


def generic_exception_handler(request: Request, exc: Exception):
    custom_exc = InternalServerErrorException()
    error_traceback = traceback.format_exception(
        etype=type(exc), value=exc, tb=exc.__traceback__
    )
    logger.error(f"{error_traceback =}")
    return custom_exception_handler(request=request, exc=custom_exc)


def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    custom_exc = CustomRequestValidationException(exc=exc)
    error_traceback = traceback.format_exception(
        etype=type(exc), value=exc, tb=exc.__traceback__
    )
    logger.error(f"{error_traceback =}")
    logger.error(f"{exc.errors() =}")
    logger.error(f"{exc.body =}")
    return custom_exception_handler(request=request, exc=custom_exc)


def pydantic_validation_exception_handler(
    request: Request, exc: ValidationError
):
    custom_exc = CustomRequestValidationException(exc=exc)
    error_traceback = traceback.format_exception(
        etype=type(exc), value=exc, tb=exc.__traceback__
    )
    logger.error(f"{error_traceback =}")
    logger.error(f"{exc.errors() =}")
    logger.error(f"{exc.raw_errors =}")
    return custom_exception_handler(request=request, exc=custom_exc)


def http_exception_handler(request: Request, exc: StarletteHTTPException):
    custom_exc = CustomHTTPException(exc=exc)
    logger.error(f"{exc.status_code =}")
    logger.error(f"{exc.detail =}")
    return custom_exception_handler(request=request, exc=custom_exc)
