from fastapi import Depends
from starlette.exceptions import HTTPException
from structlog import get_logger

from app.models.user import UserDb
from app.services.gateway import get_current_active_user

logger = get_logger()

role_mapping = {
    "ADMIN": 0,
    "EDIT": 1,
    "READ": 2,
}


async def verify_user(
    module,
    role,
    user: UserDb = Depends(get_current_active_user),
):
    # fetch user organization team and permissions

    user_permissions = user.permissions

    required_role_priority = role_mapping[role]

    if (
        module not in user_permissions
        or required_role_priority < role_mapping[user_permissions[module]]
    ):
        raise HTTPException(status_code=403, detail="Operation not permitted")
