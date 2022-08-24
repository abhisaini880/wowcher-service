from typing import Optional

from fastapi import status

from base import CustomException


class UserAccountServiceException(CustomException):
    """
    trigger when any user account service related error
    * CustomCode = 301
    """

    def __init__(
        self,
        status_code: Optional[int] = status.HTTP_500_INTERNAL_SERVER_ERROR,
        marshalled_code: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:

        status_code = (
            status_code
            if status_code
            else status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        default_message = "Error connecting to User Account Service."
        message = message if message else default_message

        # marshall error_code and status_code from User Account Service
        # if received, to quickly get through the actual issue
        super().__init__(
            status_code=status_code,
            marshalled_code=marshalled_code,
            message=message,
        )
