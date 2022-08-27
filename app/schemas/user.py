from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name: str
    email_id: Union[str, None] = None
    active: Union[bool, None] = None


class UserRegisterRequest(User):
    password: str


class UserRegisterResponse(User):
    id: str
