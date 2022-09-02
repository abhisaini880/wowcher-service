""" Data access objects of organizations Model"""


# from .dependency.db_session import get_db_session
from sqlalchemy.orm import Session
from app.models.organization import (
    OrganizationDb,
    OrganizationMemberDb,
    OrganizationTeamDb,
    TeamMemberDb,
)
from sqlalchemy.future import select
from fastapi.encoders import jsonable_encoder


class OrganizationDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_organization_by_id(self, org_id: str):
        """_summary_

        Args:
            session (Session, optional): _description_. Defaults to Depends(get_db_session).
        """

        query = select(OrganizationDb).where(OrganizationDb.id == org_id)
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["OrganizationDb"])

        return response

    async def create_organization(self, data: OrganizationDb):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        db_data = OrganizationDb(
            name=data.name,
            meta=jsonable_encoder(data.meta),
            created_by=data.created_by,
            updated_by=data.updated_by,
        )

        self.db_session.add(db_data)
        await self.db_session.flush()

        return jsonable_encoder(db_data)

    async def get_teams_by_organization_id(self, org_id):
        """_summary_

        Args:
            org_id (_type_): _description_
        """
        query = select(OrganizationTeamDb).where(
            OrganizationTeamDb.organization_id == org_id
        )
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["OrganizationTeamDb"])

        return response

    async def create_organization_team(self, data: OrganizationTeamDb):
        """_summary_

        Args:
            data (OrganizationTeamDb): _description_
        """

        db_data = OrganizationTeamDb(
            name=data.name,
            organization_id=data.organization_id,
            permissions=jsonable_encoder(data.permissions),
            created_by=data.created_by,
            updated_by=data.updated_by,
        )

        self.db_session.add(db_data)
        await self.db_session.flush()

        return jsonable_encoder(db_data)

    async def get_members_by_organization_id(self, org_id):
        """_summary_

        Args:
            org_id (_type_): _description_
        """
        query = select(OrganizationMemberDb).where(
            OrganizationMemberDb.organization_id == org_id
        )
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["OrganizationMemberDb"])

        return response

    async def create_organization_member(
        self, member_data: OrganizationMemberDb, team_member_data: TeamMemberDb
    ):
        """_summary_

        Args:
            data (OrganizationMemberDb): _description_
        """

        # member_db_data = OrganizationMemberDb(
        #     organization_id=member_data.organization_id,
        #     user_id=member_data.user_id,
        #     active=member_data.active,
        #     created_by=member_data.created_by,
        #     updated_by=member_data.updated_by,
        # )

        # team_member_db_data = TeamMemberDb(
        #     team_id=team_member_data.team_id,
        #     user_id=team_member_data.user_id,
        #     active=team_member_data.active,
        #     created_by=team_member_data.created_by,
        #     updated_by=team_member_data.updated_by,
        # )

        self.db_session.add(member_data)
        await self.db_session.flush()

        self.db_session.add(team_member_data)
        await self.db_session.flush()

        return jsonable_encoder(member_data), jsonable_encoder(
            team_member_data
        )
