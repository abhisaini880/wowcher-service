""" Routes for v1 version app """

from fastapi import APIRouter

from apis.v1 import organisation

from core.middlewares import gateway

router = APIRouter()
router.include_router(
    organisation.router, prefix="/organisations", tags=["organisations"]
)
router.include_router(gateway.router, prefix="/auth", tags=["auth"])
