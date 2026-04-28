from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class GitHubLoginPage(BasePage):
    URL = "https://github.com/login"

    USERNAME_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")
    USER_AVATAR = (By.CSS_SELECTOR, '[data-testid="github-avatar"]')
    ERROR_CONTAINER = (By.CSS_SELECTOR, "#js-flash-container")

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_FIELD, username)

        password_input = self.wait_visible(self.PASSWORD_FIELD)
        if not password_input.is_enabled():
            self.driver.execute_script(
                "arguments[0].removeAttribute('disabled')", password_input
            )
        self.fill(self.PASSWORD_FIELD, password)

        self.click(self.SIGN_IN_BUTTON)

    def should_be_logged_in(self):
        self.should_be_visible(self.USER_AVATAR)

    def should_show_error_contains(self, expected_text: str):
        self.should_contain_text(self.ERROR_CONTAINER, expected_text)
