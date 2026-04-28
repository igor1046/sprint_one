from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class HomePage(BasePage):
    URL = "https://github.com/home"
    SOLUTIONS_BUTTON_NAME = "Solutions"
    RESOURCES_BUTTON_NAME = "Resources"

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def _open_top_menu(self, menu_name: str):
        menu_button = self.page.get_by_role("button", name=menu_name)
        menu_button.wait_for(state="visible")
        menu_button.hover()
        if menu_button.get_attribute("aria-expanded") != "true":
            menu_button.click()
        expect(menu_button).to_have_attribute("aria-expanded", "true")

    def open_solutions_menu(self):
        self._open_top_menu(self.SOLUTIONS_BUTTON_NAME)

    def open_resources_menu(self):
        self._open_top_menu(self.RESOURCES_BUTTON_NAME)
