from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import PostgresDsn

from urllib.parse import quote_plus as urlquote

from core.config import settings


SQLALCHEMY_DATABASE_URL = PostgresDsn.build(
    scheme="mysql+asyncmy",
    user=settings.RELATIONAL_DB_USER,
    password=urlquote(settings.RELATIONAL_DB_PASSWORD),
    host=settings.RELATIONAL_DB_HOST,
    path=f"/{settings.RELATIONAL_DB_NAME or ''}",
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, autocommit=True, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()
