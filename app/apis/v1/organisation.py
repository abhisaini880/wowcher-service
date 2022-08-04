""" API Controller for organisations """

from fastapi import APIRouter, Depends

# from structlog import get_logger

# from app.dal.referral import ReferralDAL
# from app.dependencies import get_referral_dal
# from app.schemas.applied_referral import AppliedReferral
# from app.schemas.referral import ApplyReferralCodeRequest, UserInfoResponse
# from app.schemas.response import SuccessResponse
# from app.services import referral as ReferralService

router = APIRouter()
# logger = get_logger()


# @router.get(
#     "/{user_id}/info", response_model=SuccessResponse[UserInfoResponse]
# )
# async def get_user_referral_info(
#     user_id: str, referral_dal: ReferralDAL = Depends(get_referral_dal)
# ):
#     """Get all referral info for user by id"""

#     response_data = await ReferralService.get_user_referral_info(
#         user_id=user_id, referral_dal=referral_dal
#     )
#     return SuccessResponse[UserInfoResponse](data=response_data)


# @router.post(
#     "/{user_id}/apply", response_model=SuccessResponse[AppliedReferral]
# )
# async def apply_referral_code(
#     user_id: str,
#     payload: ApplyReferralCodeRequest,
#     referral_dal: ReferralDAL = Depends(get_referral_dal),
# ):
#     """Apply and validate Referral Code"""

#     response_data = await ReferralService.apply_referral_code(
#         user_id=user_id,
#         referrer_code=payload.referrer_code,
#         referral_dal=referral_dal,
#     )
#     return SuccessResponse[AppliedReferral](data=response_data)
