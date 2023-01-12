""" API Controller for organizations """

from fastapi import APIRouter, Depends, status
from services import organization as OrganizationService
from structlog import get_logger

from app.DAL.organizations import OrganizationDAO
from app.dependency.db_session import get_organization_dal
from app.schemas.organization import OrganizationRequest, OrganizationResponse
from app.schemas.response import Response

router = APIRouter()
logger = get_logger()


# @router.get(
#     "",
#     response_model=Response[list[OrganizationResponse]],
#     status_code=status.HTTP_200_OK,
# )
# async def get_user(
#     current_user: UserDb = Depends(get_current_active_user),
# ):
#     """
#     Args:
#         org_id (str): _description_
#         organization_dal (OrganizationDAO, optional): _description_. Defaults to Depends(get_organization_dal).
#         current_user (UserDb, optional): _description_. Defaults to Depends(get_current_active_user).

#     Returns:
#         _type_: _description_
#     """
#     logger.info(current_user)
#     response_data = await OrganizationService.get_organization_members(
#         org_id=org_id, organization_dal=organization_dal
#     )

#     print(response_data)

#     return Response(data=response_data)
