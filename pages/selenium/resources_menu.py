from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class ResourcesMenu(BasePage):
    EXPECTED_TOPICS = [
        "AI",
        "DevOps",
        "Security",
        "Software Development",
        "View all topics",
    ]
    TOPICS_LINKS = (
        By.CSS_SELECTOR,
        "a[href*='/resources/articles?topic='], "
        "a[data-analytics-event*='view_all_topics']",
    )

    def get_topics(self) -> list[str]:
        elems = self.wait.until(lambda d: d.find_elements(*self.TOPICS_LINKS))
        return [el.text.strip() for el in elems if el.text.strip()]
