""" This module will generate the custom API doc info """

from collections import namedtuple


def generate_api_doc():
    api_doc = namedtuple(
        "api_doc",
        [
            "title",
            "description",
            "version",
            "license_info",
            "tags_metadata",
            "docs_url",
            "redoc_url",
            "logo",
        ],
    )
    api_doc_obj = api_doc(
        tags_metadata=[
            {
                "name": "Introduction",
                "description": " Welcome to the **wowcher API!**. \n\n Code references are presented in the main column and examples in the right column.",
            },
            {
                "name": "Authentication",
                "description": (
                    "The wowcher API uses access tokens to control access and authenticate requests, the access token will reflect the user permissions when used in API requests."
                    "The access token should be included in all API requests to the server in the Authorization header in the following way:"
                    "\n\n ***Authorization: Bearer wowcherwowcher***"
                ),
            },
            {
                "name": "organizations",
                "description": "Manage all operations related to organization.",
            },
        ],
        title="Wowcher API's",
        description="Wowcher Service API's will help you integrate differnet components with your app",
        version="0.1.0",
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        docs_url=None,
        redoc_url="/api/documentation",
        logo="https://raw.githubusercontent.com/abhisaini880/wowcher-service/3e816161e19f498c528166d50c886885f8ac291d/wowcher_logo.png",
    )

    return api_doc_obj
