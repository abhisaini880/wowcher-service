""" Gateway Module to manage user signup and login """

# --- Standard library imports --- #

# --- Related third party imports --- #
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from structlog import get_logger

# --- Local application/library specific imports --- #
from app.DAL.users import UserDAO
from app.dependency.db_session import get_user_dal
from app.schemas.gateway import Token
from app.schemas.response import Response
from app.schemas.user import UserRegisterRequest, UserRegisterResponse
from app.services import gateway as GatewayService

router = APIRouter()
logger = get_logger()


@router.post(
    "/login",
    response_model=Response[Token],
    status_code=status.HTTP_200_OK,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_dal: UserDAO = Depends(get_user_dal),
):
    """
    In order to access API on behalf of registered user,
    generate the access token and refresh token.
    * Pass this access token in every API request headers.
    * Use the refresh token to generate new access token once access token is expired.
    """

    response_data = await GatewayService.login_user(
        payload=form_data, user_dal=user_dal
    )

    return Response(data=response_data)


@router.post(
    "/signup",
    response_model=Response[UserRegisterResponse],
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    payload: UserRegisterRequest, user_dal: UserDAO = Depends(get_user_dal)
):
    """
    Register new user in the system.
    """

    response_data = await GatewayService.register_user(
        payload=payload, user_dal=user_dal
    )

    return Response(data=response_data)
