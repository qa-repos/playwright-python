import time
import pytest

from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from api.helpers.helpers.user import User

username = f"{int(time.time())}"
password = "P@SSWord1"

user_helper = User()


@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright, base_url
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()


def test_get_all_books(api_request_context: APIRequestContext) -> None:
    books = api_request_context.get("/BookStore/v1/Books")
    assert books.ok
    books_response = books.json()
    assert books_response, "Noo books found!"


def test_register_new_user(api_request_context: APIRequestContext) -> None:
    user_helper.register_new_user(api_request_context, username, password)


def test_login_successfully(api_request_context: APIRequestContext) -> None:
    user_helper.login_to_bookstore(api_request_context, username, password)
