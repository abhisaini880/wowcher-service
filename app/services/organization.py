""" Organization service """
from app.DAL.organizations import OrganizationDAO
from app.DAL.users import UserDAO
from app.models.organization import (
    OrganizationDb,
    OrganizationTeamDb,
    OrganizationMemberDb,
    TeamMemberDb,
)
from app.core.config import settings


async def get_organizations(org_id: str, organization_dal: OrganizationDAO):
    if org_id:
        return await organization_dal.get_organization_by_id(org_id=org_id)


async def create_organization(payload, organization_dal: OrganizationDAO):

    organization_data = OrganizationDb(
        name=payload.name,
        meta=payload.meta,
        created_by=settings.SYSTEM_USER_ID,
        updated_by=settings.SYSTEM_USER_ID,
    )

    return await organization_dal.create_organization(organization_data)


async def update_oragnisation():
    pass


async def get_organization_teams(
    org_id: str, organization_dal: OrganizationDAO
):
    if org_id:
        return await organization_dal.get_teams_by_organization_id(
            org_id=org_id
        )


async def create_organization_team(payload, organization_dal: OrganizationDAO):

    organization_team_data = OrganizationTeamDb(
        name=payload.name,
        organization_id=payload.organization_id,
        permissions=payload.permissions,
        created_by=settings.SYSTEM_USER_ID,
        updated_by=settings.SYSTEM_USER_ID,
    )

    return await organization_dal.create_organization_team(
        organization_team_data
    )


async def get_organization_members(
    org_id: str, organization_dal: OrganizationDAO
):
    if org_id:
        return await organization_dal.get_members_by_organization_id(
            org_id=org_id
        )


async def create_organization_member(
    payload, organization_dal: OrganizationDAO, current_user
):

    organization_member_data = OrganizationMemberDb(
        organization_id=payload.organization_id,
        user_id=payload.user_id,
        created_by=current_user.get("id"),
        updated_by=current_user.get("id"),
    )

    team_member_data = TeamMemberDb(
        team_id=payload.team_id,
        user_id=payload.user_id,
        created_by=current_user.get("id"),
        updated_by=current_user.get("id"),
    )

    (
        member_response,
        team_member_response,
    ) = await organization_dal.create_organization_member(
        organization_member_data, team_member_data
    )

    member_response["team_id"] = team_member_response["team_id"]
    return member_response
