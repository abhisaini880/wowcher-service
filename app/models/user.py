""" models for users """

from uuid import uuid4

from sqlalchemy import BOOLEAN, Column, DateTime, String

from app.databases.mysql import Base
from app.models.custom_mixins import DateTimeMixin, UserMixin
from app.utils.models import BinaryUUID


class UserDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "users"

    id = Column(BinaryUUID, primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    email_id = Column(String(100), nullable=False)
    hashed_pwd = Column(String(150), nullable=False)
    last_login = Column(DateTime, nullable=True)
    active = Column(BOOLEAN, default=True)

    def __repr__(self):
        return "User: ({!r})".format(self.__dict__)
