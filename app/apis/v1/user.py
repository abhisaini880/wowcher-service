""" API Controller for organizations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from app.schemas.response import SuccessResponse

from app.dependency.db_session import get_organization_dal
from app.schemas.organization import OrganizationResponse, OrganizationRequest

from services import organization as OrganizationService
from app.DAL.organizations import OrganizationDAO

router = APIRouter()
logger = get_logger()
