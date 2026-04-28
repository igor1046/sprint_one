from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class CiCdPage(BasePage):
    CONTACT_SALES_LINK = "a[href*='github.com/enterprise/contact']"

    def click_contact_sales(self):
        contact_sales_link = self.page.locator(self.CONTACT_SALES_LINK).first
        expect(contact_sales_link).to_be_visible()
        contact_sales_link.click()
