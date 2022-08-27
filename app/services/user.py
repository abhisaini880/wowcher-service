""" User Services """

""" Organisation service """
from app.DAL.users import UserDAO
from fastapi import Depends
from app.models.user import UserDb


async def get_user(email_id: str, user_dal: UserDAO):
    return await user_dal.get_user_by_email(email_id=email_id)


async def create_user(payload: UserDb, user_dal: UserDAO):
    return await user_dal.create_user(payload)


async def update_user():
    pass
