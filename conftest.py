from typing import Generator
from dotenv import load_dotenv

import os
import pytest
from playwright.sync_api import Playwright, APIRequestContext

load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.fixture(scope="session")
def base_url():
    return os.getenv('DOMAIN')


@pytest.fixture(scope="session")
def request_context(
        playwright: Playwright, base_url
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()
