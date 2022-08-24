""" models for users """

from sqlalchemy import Column, String, DateTime, BOOLEAN

from databases.mysql import Base
from models.custom_mixins import DateTimeMixin, UserMixin

from utils.models import BinaryUUID
from uuid import uuid4


class UserDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "users"

    user_id = Column(BinaryUUID, primary_key=True, default=uuid4)
    user_name = Column(String(100), nullable=False)
    email_id = Column(String(100), nullable=False)
    hashed_pwd = Column(String(150), nullable=False)
    last_login = Column(DateTime, nullable=True)
    active = Column(BOOLEAN, default=True)

    def __repr__(self):
        return "User: ({!r})".format(self.__dict__)
