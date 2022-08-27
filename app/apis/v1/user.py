""" API Controller for organisations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from app.schemas.response import SuccessResponse

from app.dependency.db_session import get_organisation_dal
from app.schemas.organisation import OrganisationResponse, OrganisationRequest

from services import organisation as OrganisationService
from app.DAL.organisations import OrganisationDAO

router = APIRouter()
logger = get_logger()
