from email.policy import default
from typing import Text
from sqlalchemy import Column, String, BINARY, JSON, TEXT

from databases.mysql import Base
from models.custom_mixins import DateTimeMixin, UserMixin

from utils.utils import BinaryUUID
from uuid import uuid4

# Base = declarative_base(cls=Base)


class OrganisationDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organisations"

    org_id = Column(BinaryUUID, primary_key=True, default=uuid4)
    org_name = Column(String(100), nullable=False)
    org_meta = Column(JSON, nullable=True)
    theme = Column(JSON, nullable=True)

    def __repr__(self):
        return "Organisation: ({!r})".format(self.__dict__)
