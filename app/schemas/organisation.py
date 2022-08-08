from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class OrganisationResponse(BaseModel):
    user_id: str
    referrer_code: ReferralCode
    referrer_user_id: str
    is_same_company: Union[bool, None] = None
    applied_on: Optional[datetime]

    class Config:
        orm_mode = True
