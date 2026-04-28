from pages.playwright.base_page import BasePage


class SearchPage(BasePage):
    URL = "https://duckduckgo.com/"

    RESULTS = '[data-testid="result"]'

    def open(self, url: str | None = None):
        super().open(url or self.URL)

    def search(self, query: str):
        search_input = self.page.get_by_role("combobox")
        search_input.fill(query)
        search_input.press("Enter")

    def results(self):
        return self.page.locator(self.RESULTS)
