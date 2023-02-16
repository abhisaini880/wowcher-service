from sqlalchemy import exc
from structlog import get_logger

from app.core.exceptions.generic import DatabaseException
from app.DAL.organizations import OrganizationDAO
from app.DAL.users import UserDAO
from app.databases.mysql import async_session

logger = get_logger()


async def get_organization_dal():
    print("creating dependency")
    session = async_session()
    async with session.begin():
        try:
            yield OrganizationDAO(session)
            await session.commit()
        except exc.SQLAlchemyError as err:
            logger.warning(f"MYSQL ERROR: {err}")
            raise DatabaseException
        finally:
            await session.close()


async def get_user_dal():
    print("creating dependency")
    session = async_session()
    async with session.begin():
        try:
            yield UserDAO(session)
            await session.commit()
        except exc.SQLAlchemyError as err:
            logger.warning(f"MYSQL ERROR: {err}")
            raise DatabaseException
        finally:
            await session.close()
