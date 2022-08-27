""" Gateway services """

from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import status, Depends
from typing import Union
from app.DAL.users import UserDAO
from app.models.user import UserDb
from app.schemas.gateway import TokenData
from . import user as UserService
from fastapi.exceptions import HTTPException
from app.dependency.db_session import get_user_dal

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# to get a string like this run:
# openssl rand -hex 32


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(user_dal: UserDAO, email_id: str, password: str):
    user = await user_dal.get_user_by_email(email_id=email_id)
    if not user:
        return False
    user = user[0]
    if not verify_password(password, user.get("hashed_pwd")):
        return False
    return user


def create_access_token(
    data: dict, expires_delta: Union[timedelta, None] = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(
    data: dict, expires_delta: Union[timedelta, None] = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


async def get_current_user(
    user_dal: UserDAO = Depends(get_user_dal),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        print(payload)
        if not payload:
            raise credentials_exception
        username: str = payload.get("email_id")
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = await user_dal.get_user_by_email(email_id=token_data.username)

    if user is None:
        raise credentials_exception
    return user[0]


async def get_current_active_user(
    current_user: UserDb = Depends(get_current_user),
):
    if not current_user.get("active"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def login_user(payload, user_dal):

    # authenticate user
    authenticated_user = await authenticate_user(
        user_dal=user_dal, email_id=payload.username, password=payload.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    refresh_token_expires = timedelta(
        minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
    )

    access_token = create_access_token(
        data=authenticated_user, expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(
        data=authenticated_user, expires_delta=refresh_token_expires
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


async def register_user(payload, user_dal):

    # check if already exitss
    user_data = await UserService.get_user(
        email_id=payload.email_id, user_dal=user_dal
    )

    if user_data:
        raise Exception

    # create password hash
    hashed_pwd = get_password_hash(payload.password)

    parsed_user_data = UserDb(
        email_id=payload.email_id,
        user_name=payload.user_name,
        hashed_pwd=hashed_pwd,
        active=True,
    )

    # call user service method `create_user`
    return await UserService.create_user(
        payload=parsed_user_data, user_dal=user_dal
    )
