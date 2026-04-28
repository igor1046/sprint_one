from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class SolutionsMenu(BasePage):
    CI_CD_LINK = (By.CSS_SELECTOR, "a[href*='/solutions/'][href*='ci']")

    def click_ci_cd(self):
        self.click(self.CI_CD_LINK)
