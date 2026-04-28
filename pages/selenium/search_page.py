from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from pages.selenium.base_page import BasePage


class SearchPage(BasePage):
    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[name="q"]')
    RESULTS = (
        By.CSS_SELECTOR,
        "article[data-testid='result'], div[data-testid='result']",
    )

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def search(self, query: str):
        search_input = self.wait_visible(self.SEARCH_INPUT)
        self.fill(self.SEARCH_INPUT, query)
        search_input.send_keys(Keys.ENTER)

    def get_results_count(self) -> int:
        self.wait.until(ec.visibility_of_any_elements_located(self.RESULTS))
        return len(self.driver.find_elements(*self.RESULTS))
