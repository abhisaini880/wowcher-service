""" Routes for v1 version app """

from fastapi import APIRouter

from app.apis.v1 import organization

from app.core import gateway

router = APIRouter()
router.include_router(
    organization.router, prefix="/organizations", tags=["organizations"]
)
router.include_router(gateway.router, prefix="/auth", tags=["Authentication"])
