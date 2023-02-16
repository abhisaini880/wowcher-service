""" models for organization """

from uuid import uuid4

from sqlalchemy import JSON, Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.databases.mysql import Base
from app.models.custom_mixins import DateTimeMixin, UserMixin


class OrganizationDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organizations"

    id = Column(String(36), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    meta = Column(JSON, nullable=True)
    theme = Column(JSON, nullable=True)

    members = relationship(
        "OrganizationMemberDb", back_populates="organization"
    )
    teams = relationship("OrganizationTeamDb", back_populates="organization")

    def __repr__(self):
        return "Organization: ({!r})".format(self.__dict__)


class OrganizationTeamDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organization_teams"

    id = Column(String(36), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    organization_id = Column(String(36), ForeignKey("organizations.id"))
    permissions = Column(JSON)

    organization = relationship("OrganizationDb", back_populates="teams")

    def __repr__(self):
        return "OrganizationTeam: ({!r})".format(self.__dict__)


class OrganizationMemberDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "organization_members"

    organization_id = Column(
        String(36), ForeignKey("organizations.id"), primary_key=True
    )
    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)

    organization = relationship("OrganizationDb", back_populates="members")

    def __repr__(self):
        return "OrganizationMember: ({!r})".format(self.__dict__)


class TeamMemberDb(Base, DateTimeMixin, UserMixin):
    __tablename__ = "team_members"

    team_id = Column(
        String(36), ForeignKey("organization_teams.id"), primary_key=True
    )
    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return "TeamMember: ({!r})".format(self.__dict__)
