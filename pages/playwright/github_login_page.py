from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class GitHubLoginPage(BasePage):
    """Page Object для страницы логина GitHub"""

    URL = "https://github.com/login"

    # Локаторы
    USERNAME_FIELD = 'input[name="login"]'
    PASSWORD_FIELD = 'input[name="password"]'
    SIGN_IN_BUTTON = 'input[name="commit"]'
    USER_AVATAR = '[data-testid="github-avatar"]'

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def login(self, username: str, password: str):
        """Выполняет логин"""
        self.fill(self.USERNAME_FIELD, username)

        # Ждём появления поля пароля (иногда оно disabled для бота)
        password_locator = self.page.locator(self.PASSWORD_FIELD)
        password_locator.wait_for(state="visible", timeout=15000)
        if password_locator.is_disabled():
            self.page.evaluate(
                """selector => {
                    const el = document.querySelector(selector);
                    if (el) el.removeAttribute("disabled");
                }""",
                self.PASSWORD_FIELD,
            )

        self.fill(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BUTTON)

    def should_be_logged_in(self):
        """Проверка успешного входа"""
        user_avatar = self.page.locator(self.USER_AVATAR)
        expect(user_avatar).to_be_visible(timeout=15000)

    def should_show_error(self, expected_text: str):
        """Проверка сообщения об ошибке"""
        error_locator = self.page.get_by_text(expected_text, exact=False)
        expect(error_locator).to_be_visible(timeout=10000)
