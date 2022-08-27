""" Organisation service """
from app.DAL.organisations import OrganisationDAO
from app.models.organisation import OrganisationDb
from app.core.config import settings


async def get_organisations(org_id: str, organisation_dal: OrganisationDAO):
    if org_id:
        return await organisation_dal.get_organisation_by_id(org_id=org_id)


async def create_organisation(payload, organisation_dal: OrganisationDAO):

    organisation_data = OrganisationDb(
        name=payload.name,
        meta=payload.meta,
        created_by=settings.SYSTEM_USER_ID,
        updated_by=settings.SYSTEM_USER_ID,
    )

    return await organisation_dal.create_organisation(organisation_data)


async def update_oragnisation():
    pass
