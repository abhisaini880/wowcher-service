""" API Controller for organisations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from schemas.response import SuccessResponse

# from app.dal.referral import ReferralDAL
# from app.dependencies import get_referral_dal
from dependecy.db_session import get_organisation_dal
from schemas.organisation import OrganisationResponse, OrganisationRequest

# from app.schemas.referral import ApplyReferralCodeRequest, UserInfoResponse
from services.organisation import Organisation
from DAL.organisations import OrganisationDAO

router = APIRouter()
logger = get_logger()
OrganisationService = Organisation()


# @router.post(
#     "/organisation", response_model=SuccessResponse[OrganisationResponse]
# )
# async def create_organisation(
#     user_id: str, payload: createOrganisationRequest
# ):
#     """_summary_

#     Args:
#         user_id (str): _description_
#         payload (createOrganisationRequest): _description_
#     """

#     response_data = await OrganisationService.create_organisation()
#     return SuccessResponse[OrganisationResponse](data=response_data)


@router.get(
    "/{org_id}",
    response_model=SuccessResponse[list[OrganisationResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_organisation(
    org_id: str,
    organisation_dal: OrganisationDAO = Depends(get_organisation_dal),
):
    """Get all referral info for user by id"""

    response_data = await OrganisationService.get_organisations(
        org_id=org_id, organisation_dal=organisation_dal
    )
    print(response_data)
    # return SuccessResponse[OrganisationResponse](data=response_data)
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
):
    """Get all referral info for user by id"""

    response_data = await OrganisationService.create_organisation(
        payload=payload, organisation_dal=organisation_dal
    )
    print(response_data)
    return SuccessResponse(
        data=response_data, code="W123", message="Created !"
    )
