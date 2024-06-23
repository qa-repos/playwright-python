import time
from urllib.parse import urlparse, parse_qs

import pytest
from playwright.sync_api import Page, expect
from lib.pages.home_page import HomePage


@pytest.mark.ui
def test_demo_qa_home_page_elements_should_be_visible(page: Page, base_url):
    home_page = HomePage(page)
    home_page.navigate(base_url)
    home_page.elements_are_visible()


def test_get_request_headers(page: Page, base_url, intercept_route):
    route_pattern = "**/Account/v1/GenerateToken"
    intercepted_data = intercept_route(route_pattern)
    # page.route(, handle_route)
    page.goto(f'{base_url}/books')
    # Click the button that triggers the request
    expect(page.locator('span.text', has_text='Login')).to_be_visible()
    page.locator('span.text', has_text='Login').click()
    page.locator('input#userName').type('someStuff')
    page.locator('input#password').type('someStuff')
    page.locator('button#login').click()
    # time.sleep(3)
    # query_params = setup_routes
    print(intercepted_data)
