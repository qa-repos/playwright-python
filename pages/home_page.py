from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # page elements
        self.main_link = self.page.locator('[href="https://demoqa.com"]')

    def navigate(self, base_url):
        self.page.goto(base_url)

    def login_via_ui(self, email, password):
        self.email_field.type(email)
        self.password_field.type(password)
        self.login_button.click()

    def elements_are_visible(self):
        expect(self.manul_animation).to_be_visible()
        expect(self.ingarten_logo).to_be_visible()
        expect(self.welcome_text).to_be_visible()
        expect(self.email_field).to_be_visible()
        expect(self.password_field).to_be_visible()
        expect(self.remember_me_checkbox).to_be_visible()
        expect(self.forgot_password_link).to_be_visible()
        expect(self.login_button).to_be_visible()

    def check_validation_errors(self, email, password, base_url):
        assert self.page.url == f'{base_url}/login'
        validation_actions = {
            (True, True): (self.email_validation_error, self.field_required_message),
            (True, False): (self.email_validation_error, self.field_required_message),
            (False, True): (self.password_validation_error, self.field_required_message),
            (False, False): (self.email_validation_error, self.invalid_email_message),
        }

        error_element, error_message = validation_actions[(not email, not password)]
        expect(error_element).to_be_visible()
        expect(error_element).to_contain_text(error_message)

    def is_login_successful(self, result, base_url):
        if result:
            expect(self.page.get_by_text("Привет, Дмитрай")).to_be_visible()
            assert self.page.url == f'{base_url}/'
        else:
            assert self.page.url == f'{base_url}/login'
