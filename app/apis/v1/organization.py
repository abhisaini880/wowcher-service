""" API Controller for organizations """

# --- Standard library imports --- #
# --- Related third party imports --- #
from fastapi import APIRouter, Depends, status
from structlog import get_logger

from app.DAL.organizations import OrganizationDAO
from app.dependency.auth import verify_user
from app.dependency.db_session import get_organization_dal
from app.models.user import UserDb
from app.schemas.organization import (
    OrganizationMemberRequest,
    OrganizationMemberResponse,
    OrganizationRequest,
    OrganizationResponse,
    OrganizationTeamRequest,
    OrganizationTeamResponse,
)

# --- Local application/library specific imports --- #
from app.schemas.response import Response
from app.services import organization as OrganizationService
from app.services import user
from app.services.gateway import get_current_active_user

router = APIRouter()
logger = get_logger()

responses = {
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}


@router.get(
    "/{org_id}",
    response_model=Response[list[OrganizationResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organization(
    org_id: str,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """


    Args:
        org_id (str): _description_
        organization_dal (OrganizationDAO, optional): _description_. Defaults to Depends(get_organization_dal).
        current_user (UserDb, optional): _description_. Defaults to Depends(get_current_active_user).

    Returns:
        _type_: _description_
    """
    logger.info(current_user)
    response_data = await OrganizationService.get_organizations(
        org_id=org_id, organization_dal=organization_dal
    )

    print(response_data)

    return Response(data=response_data)


@router.post(
    "",
    response_model=Response[OrganizationResponse],
    responses={**responses, 201: {"data": {"id": "", "name": "", "meta": {}}}},
    status_code=status.HTTP_201_CREATED,
)
async def create_organization(
    payload: OrganizationRequest,
    organization_dal: OrganizationDAO = Depends(get_organization_dal),
    # dependencies=[Depends(verify_user)],
):
    """
    Create new organization

    Args:
        payload (OrganizationRequest): Organization meta data
        organization_dal (OrganizationDAO, optional): organiation data access layer object. Defaults to Depends(get_organization_dal).
        current_user (UserDb, optional): User requesting the API. Defaults to Depends(get_current_active_user).

    Returns:
        Response: Return created organization object
    """

    # Check if user has required permissions

    response_data = await OrganizationService.create_organization(
        payload=payload, organization_dal=organization_dal
    )
    print(response_data)
    return Response(data=response_data)


# @router.get(
#     "",
#     response_model=Response[OrganizationResponse],
#     responses={**responses, 201: {"data": {"id": "", "name": "", "meta": {}}}},
#     status_code=status.HTTP_201_CREATED,
# )
# async def get_organization_member(
#     payload: OrganizationRequest,
#     organization_dal: OrganizationDAO = Depends(get_organization_dal),
#     dependencies=[Depends(verify_user)],
# ):
#     """
#     Create new organization

#     Args:
#         payload (OrganizationRequest): Organization meta data
#         organization_dal (OrganizationDAO, optional): organiation data access layer object. Defaults to Depends(get_organization_dal).
#         current_user (UserDb, optional): User requesting the API. Defaults to Depends(get_current_active_user).

#     Returns:
#         Response: Return created organization object
#     """

#     # Check if user has required permissions

#     response_data = await OrganizationService.create_organization(
#         payload=payload, organization_dal=organization_dal
#     )
#     print(response_data)
#     return Response(data=response_data)


@router.get(
    "/{org_id}/teams",
    response_model=Response[list[OrganizationTeamResponse]],
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

    return Response(data=response_data)


@router.post(
    "/teams",
    response_model=Response[OrganizationTeamResponse],
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
    return Response(data=response_data)


@router.get(
    "/{org_id}/members",
    response_model=Response[list[OrganizationMemberResponse]],
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

    return Response(data=response_data)


@router.post(
    "/members",
    response_model=Response[OrganizationMemberResponse],
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
    return Response(data=response_data)
