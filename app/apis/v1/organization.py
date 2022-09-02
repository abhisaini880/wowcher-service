""" API Controller for organizations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from app.schemas.response import SuccessResponse

from app.dependency.db_session import get_organization_dal
from app.schemas.organization import (
    OrganizationResponse,
    OrganizationRequest,
    OrganizationTeamRequest,
    OrganizationTeamResponse,
    OrganizationMemberRequest,
    OrganizationMemberResponse,
)

from app.services import organization as OrganizationService
from app.DAL.organizations import OrganizationDAO

from app.services.gateway import get_current_active_user
from app.models.user import UserDb

router = APIRouter()
logger = get_logger()


@router.get(
    "/{org_id}",
    response_model=SuccessResponse[list[OrganizationResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organization(
    org_id: str,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""
    logger.info(current_user)
    response_data = await OrganizationService.get_organizations(
        org_id=org_id, organization_dal=organization_dal
    )

    print(response_data)

    return SuccessResponse(data=response_data)


@router.post(
    "",
    response_model=SuccessResponse[OrganizationResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_organization(
    payload: OrganizationRequest,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""
    print("inside create organization")
    response_data = await OrganizationService.create_organization(
        payload=payload, organization_dal=organization_dal
    )
    print(response_data)
    return SuccessResponse(data=response_data)


@router.get(
    "/{org_id}/teams",
    response_model=SuccessResponse[list[OrganizationTeamResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organization_teams(
    org_id: str,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""
    logger.info(current_user)
    response_data = await OrganizationService.get_organization_teams(
        org_id=org_id, organization_dal=organization_dal
    )

    print(response_data)

    return SuccessResponse(data=response_data)


@router.post(
    "/teams",
    response_model=SuccessResponse[OrganizationTeamResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_organization_team(
    payload: OrganizationTeamRequest,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    print(current_user)
    response_data = await OrganizationService.create_organization_team(
        payload=payload, organization_dal=organization_dal
    )
    print(response_data)
    return SuccessResponse(data=response_data)


@router.get(
    "/{org_id}/members",
    response_model=SuccessResponse[list[OrganizationMemberResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organization_members(
    org_id: str,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""
    logger.info(current_user)
    response_data = await OrganizationService.get_organization_members(
        org_id=org_id, organization_dal=organization_dal
    )

    print(response_data)

    return SuccessResponse(data=response_data)


@router.post(
    "/members",
    response_model=SuccessResponse[OrganizationMemberResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_organization_member(
    payload: OrganizationMemberRequest,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    print(current_user)
    response_data = await OrganizationService.create_organization_member(
        payload=payload,
        organization_dal=organization_dal,
        current_user=current_user,
    )
    print(response_data)
    return SuccessResponse(data=response_data)
