""" Organisation service """
from DAL.organisations import OrganisationDAO

# from dependecy.db_session import get_db_session
from sqlalchemy.orm import Session
from fastapi import Depends


class Organisation:
    def __init__(self):
        pass

    async def get_organisations(
        self, org_id: str, organisation_dal: OrganisationDAO
    ):
        if org_id:
            return await organisation_dal.get_organisation_by_id(org_id=org_id)

    async def create_organisation(
        self, payload, organisation_dal: OrganisationDAO
    ):
        return await organisation_dal.create_organisation(payload)

    async def update_oragnisation(self):
        ...
