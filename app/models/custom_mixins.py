from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declared_attr


def default_time():
    return datetime.utcnow()


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
    created_by = Column(String(100), nullable=False)
    updated_by = Column(String(100), nullable=False)
