import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_demoqa_home_page_elements_should_be_visible(page: Page, base_url):
    home_page = HomePage(page)
    home_page.navigate(base_url)

    # # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))
    #
    # # create a locator
    # get_started = page.get_by_role("link", name="Get started")
    #
    # # Expect an attribute "to be strictly equal" to the value.
    # expect(get_started).to_have_attribute("href", "/docs/intro")
    #
    # # Click the get started link.
    # get_started.click()
    #
    # # Expects the URL to contain intro.
    # expect(page).to_have_url(re.compile(".*intro"))