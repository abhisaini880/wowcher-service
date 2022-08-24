from typing import Any, Generic, Optional, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")

DEFAULT_ERR_MESSAGE = "Oops !! This shouldn't have happened. Please try again."


class BaseResponse(GenericModel, Generic[DataT]):
    code: Optional[str]
    message: Optional[str]
    data: Optional[DataT] = None

    def dict(self, *args, **kwargs):
        if kwargs and kwargs.get("exclude_none") is not None:
            kwargs["exclude_none"] = True
            return GenericModel.dict(self, *args, **kwargs)


class SuccessResponse(BaseResponse[DataT], Generic[DataT]):
    message: Optional[str]
    data: DataT


class ErrorResponse(BaseResponse[DataT], Generic[DataT]):
    code: str
    message: str = DEFAULT_ERR_MESSAGE
    details: Optional[Any]
