import pytest
from playwright.sync_api import Page
from lib.pages.home_page import HomePage


@pytest.mark.ui
def test_demoqa_home_page_elements_should_be_visible(page: Page, base_url):
    home_page = HomePage(page)
    home_page.navigate(base_url)
    home_page.elements_are_visible()
