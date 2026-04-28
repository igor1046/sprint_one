from typing import TypeAlias

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

Locator: TypeAlias = tuple[str, str] | str
DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def _by(self, locator: Locator) -> tuple[str, str]:
        if isinstance(locator, str):
            return By.CSS_SELECTOR, locator
        return locator

    def wait_visible(self, locator: Locator):
        return self.wait.until(ec.visibility_of_element_located(self._by(locator)))

    def wait_clickable(self, locator: Locator):
        return self.wait.until(ec.element_to_be_clickable(self._by(locator)))

    def click(self, locator: Locator) -> None:
        self.wait_clickable(locator).click()

    def fill(self, locator: Locator, value: str) -> None:
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def should_have_text(self, locator: Locator, text: str) -> None:
        assert self.wait_visible(locator).text == text

    def should_contain_text(self, locator: Locator, text: str) -> None:
        assert text in self.wait_visible(locator).text

    def should_be_visible(self, locator: Locator) -> None:
        self.wait_visible(locator)

    def get_value(self, locator: Locator) -> str | None:
        return self.wait_visible(locator).get_attribute("value")
