from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext


class User:
    @pytest.fixture(scope="session")
    def api_request_context(
            self: Playwright, base_url
    ) -> Generator[APIRequestContext, None, None]:
        request_context = self.request.new_context(base_url=base_url)
        yield request_context
        request_context.dispose()

    def register_new_user(self, api_request_context: APIRequestContext, username, password):
        payload = {
            "userName": username,
            "password": password
        }
        new_user = api_request_context.post("/Account/v1/User", form=payload)
        assert new_user.ok
