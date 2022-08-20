""" Routes for v1 version app """

from fastapi import APIRouter

from apis.v1 import organisation

router = APIRouter()
router.include_router(
    organisation.router, prefix="/organisations", tags=["organisations"]
)
