from fastapi import APIRouter

from app.apis.v1 import organisation

v1_router = APIRouter()
v1_router.include_router(
    organisation.router, prefix="/organisations", tags=["organisation-info"]
)
