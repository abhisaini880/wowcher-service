""" Data access objects of organisations Model"""


# from .dependency.db_session import get_db_session
from sqlalchemy.orm import Session
from app.models.organisation import OrganisationDb
from sqlalchemy.future import select
from fastapi.encoders import jsonable_encoder


class OrganisationDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_organisation_by_id(self, org_id: str):
        """_summary_

        Args:
            session (Session, optional): _description_. Defaults to Depends(get_db_session).
        """

        query = select(OrganisationDb).where(OrganisationDb.id == org_id)
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["OrganisationDb"])

        return response

    async def create_organisation(self, data: OrganisationDb):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        db_data = OrganisationDb(
            name=data.name,
            meta=jsonable_encoder(data.meta),
            created_by=data.created_by,
            updated_by=data.updated_by,
        )

        self.db_session.add(db_data)
        await self.db_session.flush()

        return jsonable_encoder(db_data)
