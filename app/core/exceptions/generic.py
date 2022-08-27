from typing import Union

from fastapi import status
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from structlog import get_logger

from .base import CustomException

logger = get_logger()

# ! Custom Codes are defined in app.exceptions.base.py
# ! Will have to add a code in that class for defining new exceptions
# * <--- GENERIC EXCEPTIONS --->


class DatabaseException(CustomException):
    """
    Trigger when anything related to database..
    will be included in db connections files
    * CustomCode = 1001
    """

    def __init__(self) -> None:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(status_code=status_code)


class CustomRequestValidationException(CustomException):
    """
    will trigger when any request pydantic validation fails
    * CustomCode = 1002
    """

    def __init__(
        self, exc: Union[RequestValidationError, ValidationError]
    ) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Invalid request. Please check your request and try again."
        super().__init__(
            status_code=status_code, message=message, details=exc.errors()
        )


class CustomHTTPException(CustomException):
    """
    catch fastapi/starlette http exceptions like 404
    * CustomCode = 1003
    """

    def __init__(self, exc: StarletteHTTPException) -> None:
        status_code = exc.status_code
        message = "This shouldn't have happened. Contact Tech Team."
        message = exc.detail if exc.detail else message
        super().__init__(status_code=status_code, message=message)


class InternalServerErrorException(CustomException):
    """
    catch all uncaught exceptions
    * CustomCode = 1999
    """

    def __init__(self) -> None:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = "This shouldn't have happened. Contact Tech Team."
        super().__init__(status_code=status_code, message=message)
