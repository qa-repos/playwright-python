from enum import auto
import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect


def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
    books = api_request_context.get("/BookStore/v1/Books")
    assert books.ok
    books_response = books.json()
    assert books_response, "Noo books found!"
    # book = list(
    #     filter(lambda issue: issue["title"] == "[Bug] report 1", issues_response)
    # )[0]
    # assert book
    # assert book["body"] == "Bug description"