""" Data access objects of users Model """

from fastapi.encoders import jsonable_encoder
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import UserDb


class UserDAO:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_user_by_id(self, user_id: str):
        """_summary_

        Args:
            session (Session, optional): _description_. Defaults to Depends(get_db_session).
        """

        query = select(UserDb).where(UserDb.id == user_id)
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["UserDb"])

        return response

    async def get_user_by_email(self, email_id: str):
        """_summary_

        Args:
            session (Session, optional): _description_. Defaults to Depends(get_db_session).
        """

        query = select(UserDb).where(UserDb.email_id == email_id)
        query_response = await self.db_session.execute(query)

        response = []

        for object in query_response:
            parsed_obj = jsonable_encoder(object)
            response.append(parsed_obj["UserDb"])

        return response

    async def create_user(self, data: UserDb):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """

        db_data = UserDb(
            name=data.name,
            email_id=data.email_id,
            hashed_pwd=data.hashed_pwd,
            active=data.active,
            created_by=data.created_by,
            updated_by=data.updated_by,
        )

        self.db_session.add(db_data)
        await self.db_session.flush()

        print(db_data)

        return jsonable_encoder(db_data)
