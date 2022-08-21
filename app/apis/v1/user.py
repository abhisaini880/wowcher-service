""" API Controller for organisations """

from fastapi import APIRouter, Depends, status

from structlog import get_logger
from schemas.response import SuccessResponse

from dependecy.db_session import get_organisation_dal
from schemas.organisation import OrganisationResponse, OrganisationRequest

from services import organisation as OrganisationService
from DAL.organisations import OrganisationDAO

router = APIRouter()
logger = get_logger()
