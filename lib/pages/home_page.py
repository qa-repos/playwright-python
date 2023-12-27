from playwright.sync_api import Page, expect, Error


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # page elements
        self.main_link = self.page.locator('[href="https://demoqa.com"]')
        self.elements_tile = self.page.locator(":text('Elements')")
        self.forms_tile = self.page.locator(":text('Forms')")
        self.alerts_frame_windows_tile = self.page.locator(":text('Alerts, Frame & Windows')")
        self.widgets_tile = self.page.locator(":text('Widgets')")
        self.interactions_tile = self.page.locator(":text('Interactions')")
        self.book_store_tile = self.page.locator(":text('Book Store Application')")
        self.tiles = [
            self.elements_tile,
            self.forms_tile,
            self.alerts_frame_windows_tile,
            self.widgets_tile,
            self.interactions_tile,
            self.book_store_tile
        ]

    def navigate(self, base_url):
        self.page.goto(base_url)

    def elements_are_visible(self):
        try:
            expect(self.main_link).to_be_visible()
            for tile in self.tiles:
                expect(tile).to_be_visible()
        except Error:
            return False
        return True
