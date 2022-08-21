""" API Controller for organisations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from schemas.response import SuccessResponse

from dependecy.db_session import get_organisation_dal
from schemas.organisation import OrganisationResponse, OrganisationRequest

from services import organisation as OrganisationService
from DAL.organisations import OrganisationDAO

from services.gateway import get_current_active_user
from models.user import UserDb

router = APIRouter()
logger = get_logger()


@router.get(
    "/{org_id}",
    response_model=SuccessResponse[list[OrganisationResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organisation(
    org_id: str,
    organisation_dal: OrganisationDAO = Depends(get_organisation_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""
    logger.info(current_user)
    response_data = await OrganisationService.get_organisations(
        org_id=org_id, organisation_dal=organisation_dal
    )

    return SuccessResponse(
        data=response_data, code="0000", message="fetched !"
    )


@router.post(
    "",
    response_model=SuccessResponse[OrganisationResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_organisation(
    payload: OrganisationRequest,
    organisation_dal: OrganisationDAO = Depends(get_organisation_dal),
    current_user: UserDb = Depends(get_current_active_user),
):
    """Get all referral info for user by id"""

    response_data = await OrganisationService.create_organisation(
        payload=payload, organisation_dal=organisation_dal
    )
    print(response_data)
    return SuccessResponse(
        data=response_data, code="W123", message="Created !"
    )
