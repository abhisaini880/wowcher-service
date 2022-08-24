""" Organisation service """
from DAL.organisations import OrganisationDAO


async def get_organisations(org_id: str, organisation_dal: OrganisationDAO):
    if org_id:
        return await organisation_dal.get_organisation_by_id(org_id=org_id)


async def create_organisation(payload, organisation_dal: OrganisationDAO):
    return await organisation_dal.create_organisation(payload)


async def update_oragnisation():
    ...
