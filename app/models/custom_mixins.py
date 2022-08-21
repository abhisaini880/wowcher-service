from datetime import datetime
from sqlalchemy import Column, DateTime, BINARY
from utils.models import BinaryUUID


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
    created_by = Column(BinaryUUID, nullable=False)
    updated_by = Column(BinaryUUID, nullable=False)
