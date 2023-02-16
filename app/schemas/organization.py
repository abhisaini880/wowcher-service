import json
import re
from datetime import datetime
from enum import Enum
from typing import Dict, Optional, Union

from pydantic import BaseModel, HttpUrl, ValidationError, validator


class OrganizationMeta(BaseModel):
    website_url: Optional[HttpUrl] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    industry: Optional[str] = None
    logo: Optional[str] = None

    @validator("phone")
    def phone_validation(cls, v):
        print("in phone number validation")
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise ValueError("Phone Number Invalid.")
        return v


class Module(Enum):
    ORG = "ORG"
    CAMP = "CAMP"


class Permissions(Enum):
    ALL = "ALL"
    READ = "READ"
    EDIT = "EDIT"


class OrganizationResponse(BaseModel):
    id: str
    name: str
    meta: OrganizationMeta

    class Config:
        orm_mode = True


class OrganizationRequest(BaseModel):
    name: str
    meta: OrganizationMeta


class OrganizationTeamRequest(BaseModel):
    name: str
    organization_id: str
    permissions: Dict[Module, Permissions]


class OrganizationTeamResponse(BaseModel):
    id: str
    name: str
    organization_id: str
    permissions: Dict[Module, Permissions]

    class Config:
        orm_mode = True


class OrganizationMemberRequest(BaseModel):
    organization_id: str
    user_id: str
    team_id: str


class OrganizationMemberResponse(BaseModel):
    organization_id: str
    user_id: str
    team_id: str

    class Config:
        orm_mode = True
