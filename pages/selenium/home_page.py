from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class HomePage(BasePage):
    URL = "https://github.com/"
    HEADER_MENU_BUTTONS = (
        By.CSS_SELECTOR,
        "button.js-details-target, button[class*='NavDropdown-module__button']",
    )

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def _get_menu_button(self, title: str):
        def find_button(_driver):
            for button in _driver.find_elements(*self.HEADER_MENU_BUTTONS):
                if button.is_displayed() and button.text.strip() == title:
                    return button
            return False

        return self.wait.until(find_button)

    def open_solutions_menu(self):
        button = self._get_menu_button("Solutions")
        ActionChains(self.driver).move_to_element(button).perform()
        if button.get_attribute("aria-expanded") != "true":
            button.click()

    def open_resources_menu(self):
        button = self._get_menu_button("Resources")
        ActionChains(self.driver).move_to_element(button).perform()
        if button.get_attribute("aria-expanded") != "true":
            button.click()
