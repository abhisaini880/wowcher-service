from datetime import datetime
import json
from typing import Optional, Union

from pydantic import BaseModel


class OrganisationMeta(BaseModel):
    test_id: str


class OrganisationResponse(BaseModel):
    org_id: str
    org_name: str
    org_meta: OrganisationMeta

    class Config:
        orm_mode = True


class OrganisationRequest(BaseModel):
    org_name: str
    org_meta: OrganisationMeta
