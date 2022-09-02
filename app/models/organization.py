""" models for organization """

from sqlalchemy import Column, String, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.databases.mysql import Base
from app.models.custom_mixins import DateTimeMixin, UserMixin

from app.utils.models import BinaryUUID
from uuid import uuid4


class OrganizationDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organizations"

    id = Column(BinaryUUID, primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    meta = Column(JSON, nullable=True)
    theme = Column(JSON, nullable=True)

    def __repr__(self):
        return "Organization: ({!r})".format(self.__dict__)


class OrganizationTeamDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organization_teams"

    id = Column(BinaryUUID, primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    organization_id = Column(BinaryUUID, ForeignKey("organizations.id"))
    permissions = Column(JSON)

    def __repr__(self):
        return "OrganizationTeam: ({!r})".format(self.__dict__)


class OrganizationMemberDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organization_members"

    organization_id = Column(
        BinaryUUID, ForeignKey("organizations.id"), primary_key=True
    )
    user_id = Column(BinaryUUID, ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return "OrganizationMember: ({!r})".format(self.__dict__)


class TeamMemberDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "team_members"

    team_id = Column(
        BinaryUUID, ForeignKey("organization_teams.id"), primary_key=True
    )
    user_id = Column(BinaryUUID, ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return "TeamMember: ({!r})".format(self.__dict__)
