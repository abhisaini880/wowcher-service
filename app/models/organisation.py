from typing import Text
from sqlalchemy import Column, String, BINARY, JSON, TEXT

from databases.mysql import Base
from models.custom_mixins import DateTimeMixin, UserMixin

# Base = declarative_base(cls=Base)


class OrganisationDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organisations"

    org_id = Column(BINARY, primary_key=True)
    org_name = Column(String(100), nullable=False)
    logo_url = Column(TEXT, nullable=True)
    theme = Column(JSON, nullable=True)
    test = Column(String(10))

    def __repr__(self):
        return "Organisation: ({!r})".format(self.__dict__)
