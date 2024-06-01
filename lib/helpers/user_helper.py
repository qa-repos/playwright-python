from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from lib.serializers.models.login_view_model import LoginViewModel
from lib.serializers.models.register_view_model import RegisterViewModel


class UserHelper:
    @pytest.fixture(scope="session")
    def api_request_context(self: Playwright, base_url) -> Generator[APIRequestContext, None, None]:
        request_context = self.request.new_context(base_url=base_url)
        yield request_context
        request_context.dispose()

    @staticmethod
    def register_new_user(api_request_context: APIRequestContext, username, password, successful=True):
        user = RegisterViewModel(user_name=username, password=password)
        response = api_request_context.post("/Account/v1/User", form=user.model_dump(by_alias=True))

        if successful:
            assert response.status == 201
            return response.json()

    @staticmethod
    def login_to_bookstore(api_request_context: APIRequestContext, username, password):
        user = LoginViewModel(user_name=username, password=password)
        login = api_request_context.post("Account/v1/GenerateToken", form=user.model_dump(by_alias=True))
        assert login.ok
