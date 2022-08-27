from fastapi import Depends, status
from fastapi.security import OAuth2PasswordRequestForm


from fastapi import APIRouter, Depends, status

from structlog import get_logger
from app.schemas.response import SuccessResponse
from app.schemas.gateway import Token
from app.schemas.user import UserRegisterRequest, UserRegisterResponse

from app.dependency.db_session import get_user_dal

from app.DAL.users import UserDAO

from app.services import user as UserService
from app.services import gateway as GatewayService
from app.core.config import settings


router = APIRouter()
logger = get_logger()


@router.post(
    "/login",
    response_model=SuccessResponse[Token],
    status_code=status.HTTP_200_OK,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_dal: UserDAO = Depends(get_user_dal),
):
    """_summary_

    Args:
        form_data (OAuth2PasswordRequestForm, optional): _description_. Defaults to Depends().
        user_dal (UserDAO, optional): _description_. Defaults to Depends(get_user_dal).

    Returns:
        _type_: _description_
    """

    response_data = await GatewayService.login_user(
        payload=form_data, user_dal=user_dal
    )

    return SuccessResponse(data=response_data)


@router.post(
    "/signup",
    response_model=SuccessResponse[UserRegisterResponse],
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    payload: UserRegisterRequest, user_dal: UserDAO = Depends(get_user_dal)
):
    """_summary_

    Args:
        payload (UserRegisterRequest): _description_
        user_dal (UserDAO, optional): _description_. Defaults to Depends(get_user_dal).

    Returns:
        _type_: _description_
    """

    response_data = await GatewayService.register_user(
        payload=payload, user_dal=user_dal
    )

    return SuccessResponse(data=response_data)
