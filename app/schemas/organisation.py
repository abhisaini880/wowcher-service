from datetime import datetime
import json
from typing import Optional, Union

from pydantic import BaseModel


class OrganisationMeta(BaseModel):
    test_id: str


class OrganisationResponse(BaseModel):
    id: str
    name: str
    meta: OrganisationMeta

    class Config:
        orm_mode = True


class OrganisationRequest(BaseModel):
    name: str
    meta: OrganisationMeta
