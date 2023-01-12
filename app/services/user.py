""" User Services """

""" Organization service """
from fastapi import Depends

from app.DAL.users import UserDAO
from app.models.user import UserDb


async def get_user(email_id: str, user_dal: UserDAO):
    return await user_dal.get_user_by_email(email_id=email_id)


async def create_user(payload: UserDb, user_dal: UserDAO):
    return await user_dal.create_user(payload)


async def update_user():
    pass


class User:
    def __init__(self, user_dal, id):
        self.user_dal = user_dal
        self.id = id

    def get_basic_details(self):
        """

        Args:
            query (_type_): _description_
        """
        pass

    def get_organization_details(self):

        # TODO:
        # 1. Get the basic details from get_basic_details
        # 2. fetch the organization details from organization dal
        # 3. fetch the permissions meta and form the scopes
        # 3. combine the data
        # 4. return

        user_basic_details = self.get_basic_details()

        organization_service = OrganizationSevice(self.db_session)
        user_organization_data = organization_service.get_member_details

        pass

    def create(self):
        pass

    def update(self):
        pass
