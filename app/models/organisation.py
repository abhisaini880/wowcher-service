""" models for organisation """

from sqlalchemy import Column, String, BINARY, JSON, TEXT

from app.databases.mysql import Base
from app.models.custom_mixins import DateTimeMixin, UserMixin

from app.utils.models import BinaryUUID
from uuid import uuid4


class OrganisationDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organisations"

    org_id = Column(BinaryUUID, primary_key=True, default=uuid4)
    org_name = Column(String(100), nullable=False)
    org_meta = Column(JSON, nullable=True)
    theme = Column(JSON, nullable=True)

    def __repr__(self):
        return "Organisation: ({!r})".format(self.__dict__)
