from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext


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
