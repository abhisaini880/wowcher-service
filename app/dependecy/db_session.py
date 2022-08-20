from sqlalchemy import exc
from structlog import get_logger

from databases.mysql import async_session
from core.exceptions.generic import DatabaseException

from DAL.organisations import OrganisationDAO

logger = get_logger()


async def get_organisation_dal():
    print("creating dependency")
    session = async_session()
    async with session.begin():
        try:
            yield OrganisationDAO(session)
            await session.commit()
        except exc.SQLAlchemyError as err:
            logger.warning(f"MYSQL ERROR: {err}")
            raise DatabaseException
        finally:
            await session.close()
