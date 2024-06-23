from typing import Generator
from urllib.parse import urlparse, parse_qs

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


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def intercept_route(page):
    def setup_routes(route_pattern):
        intercepted_data = {
            'query_params': {},
            'headers': {},
            'full_url': '',
            'resource_type': ''
        }

        # Define a function to capture query parameters and handle XHR requests
        def handle_route(route):
            request = route.request
            intercepted_data['headers'].update(request.headers)
            intercepted_data['full_url'] = request.url
            intercepted_data['resource_type'] = request.resource_type

            # Parse the query parameters
            parsed_url = urlparse(request.url)
            intercepted_data['query_params'].update(parse_qs(parsed_url.query))

            route.continue_()

        page.route(route_pattern, handle_route)

        return intercepted_data

    return setup_routes
