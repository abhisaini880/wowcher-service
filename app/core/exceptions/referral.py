from base import CustomException
from fastapi import status
from structlog import get_logger

logger = get_logger()


# * <--- APPLYING REFERRAL EXCEPTIONS --->
# to use when user has already applied a coupon code
class UserAlreadyReferredException(CustomException):
    def __init__(self) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "User has already applied a code successfully."
        super().__init__(status_code=status_code, message=message)


# to use when the applied referrer code doeesn't exist in the database
class InvalidAppliedReferrerCodeException(CustomException):
    def __init__(self, own_referral_code: bool = False) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Applied Referrer Code is invalid."
        if own_referral_code:
            message = "Own Referral Code can't be applied."
        message = f"{message} Please provide a valid code."
        super().__init__(status_code=status_code, message=message)


# to use when user has already applied a coupon code
class ReferralCodeGenerationLimitExceededException(CustomException):
    def __init__(self) -> None:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = "Something went wrong !! Please try again."
        super().__init__(status_code=status_code, message=message)


# to use when user A already used refferal code of User B
class ViceVersaCodeAppliedException(CustomException):
    def __init__(self) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Not Eligible for Code Redemption"
        super().__init__(status_code=status_code, message=message)


# Date Check validation
class OlderUserNotEligibleException(CustomException):
    def __init__(self) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Not Eligible for Referral Code"
        super().__init__(status_code=status_code, message=message)
