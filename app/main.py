import os

from fastapi import Depends, FastAPI, HTTPException, Request, Response

# from sqlalchemy.orm import Session

import uvicorn

from models import organisation
from core.config import settings
from databases.mysql import engine, Base

# from models import organisation


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


def create_app():
    """_summary_

    Returns:
        _type_: _description_
    """
    _app = FastAPI(title="Customer-Loyality-Service")
    # allowed_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS]

    # _app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=allowed_origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    # # _app.add_middleware(RawContextMiddleware)

    # _app.include_router(status_router)
    # _app.include_router(v1_router, prefix="/v1", tags=["v1"])

    return _app


app = create_app()


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# TODO:
# 1. services can be called from api or can be executed as a single entity
# 2. DAO layer is between service and database
# 3. apis will have diffenent versions
# 4. models will have table schema
# 5. Database connection and middlewares

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
