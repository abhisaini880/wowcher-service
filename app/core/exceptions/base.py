from enum import Enum
from typing import Any, Optional

from fastapi import status
from structlog import get_logger

from app.schemas.response import ErrorResponse

logger = get_logger()

CUSTOM_CODE_PREFIX = "REF-"


class _CustomExceptionCodes(int, Enum):
    # * generic errors
    DatabaseException = 101
    CustomRequestValidationException = 102
    CustomHTTPException = 190
    InternalServerErrorException = 199
    # * referral code errors
    UserAlreadyReferredException = 201
    InvalidAppliedReferrerCodeException = 202
    ReferralCodeGenerationLimitExceededException = 203
    # * sf sync errors
    InvalidSfSyncType = 211
    ViceVersaCodeAppliedException = 204
    OlderUserNotEligibleException = 205
    # * integration exception
    UserAccountServiceException = 301


class CustomException(Exception):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        marshalled_code: Optional[str] = None,
        message: Optional[str] = None,
        details: Optional[Any] = None,
    ) -> None:
        self.name = self.__class__.__name__
        self.error_code = _CustomExceptionCodes[self.name]
        default_code = f"{CUSTOM_CODE_PREFIX}{self.error_code}"
        self.code = marshalled_code if marshalled_code else default_code
        self.response = ErrorResponse[dict](code=self.code)
        self.status_code = status_code
        if message:
            self.response.message = self.message = message
        if details:
            self.response.details = self.details = details

        logger.warning(
            (
                "Custom Exception Occured"
                f" | {self.name}"
                f" | {self.code}"
                f" | {self.status_code}"
            )
        )