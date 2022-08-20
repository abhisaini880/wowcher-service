# from passlib.context import CryptContext
# import os
# from datetime import datetime, timedelta
# from typing import Union, Any
# from jose import jwt


# password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
# REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
# ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]  # should be kept secret
# JWT_REFRESH_SECRET_KEY = os.environ[
#     "JWT_REFRESH_SECRET_KEY"
# ]  # should be kept secret


# def get_hashed_password(password: str) -> str:
#     return password_context.hash(password)


# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)


# def create_access_token(
#     subject: Union[str, Any], expires_delta: int = None
# ) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(
#             minutes=ACCESS_TOKEN_EXPIRE_MINUTES
#         )

#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
#     return encoded_jwt


# def create_refresh_token(
#     subject: Union[str, Any], expires_delta: int = None
# ) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(
#             minutes=REFRESH_TOKEN_EXPIRE_MINUTES
#         )

#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
#     return encoded_jwt

import uuid

from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.types import TypeDecorator


class BinaryUUID(TypeDecorator):
    """Optimize UUID keys. Store as 16 bit binary, retrieve as uuid.
    inspired by:
        http://mysqlserverteam.com/storing-uuid-values-in-mysql-tables/
    """

    impl = BINARY(16)

    def process_bind_param(self, value, dialect):
        try:
            return value.bytes
        except AttributeError:
            try:
                return uuid.UUID(value).bytes
            except TypeError:
                # for some reason we ended up with the bytestring
                # ¯\_(ツ)_/¯
                # I'm not sure why you would do that,
                # but here you go anyway.
                return value

    def process_result_value(self, value, dialect):
        try:
            return uuid.UUID(bytes=value)
        except Exception:
            return value
