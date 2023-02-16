from fastapi import APIRouter

status_router = APIRouter()


@status_router.get("/status", include_in_schema=False)
async def get_status():
    return "wowcher services are running!"
