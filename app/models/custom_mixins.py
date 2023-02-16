import arrow

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import declared_attr, relationship


def default_time():
    return arrow.utcnow()


class DateTimeMixin:
    created_at = Column(
        DateTime,
        default=default_time,
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=default_time,
        onupdate=default_time,
    )


class UserMixin:
    @declared_attr
    def created_by(cls):
        return Column(String(36), ForeignKey("users.id"), nullable=True)

    @declared_attr
    def updated_by(cls):
        return Column(String(36), ForeignKey("users.id"), nullable=True)

    @declared_attr
    def created_by_user(cls):
        return relationship(
            "UserDb", foreign_keys=[cls.created_by], remote_side="UserDb.id"
        )

    @declared_attr
    def updated_by_user(cls):
        return relationship(
            "UserDb", foreign_keys=[cls.updated_by], remote_side="UserDb.id"
        )
