from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class CiCdPage(BasePage):
    CONTACT_SALES_LINK = (
        By.CSS_SELECTOR,
        "a[href*='github.com/enterprise/contact']",
    )

    def click_contact_sales(self):
        self.click(self.CONTACT_SALES_LINK)
