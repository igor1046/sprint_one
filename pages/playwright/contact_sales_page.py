from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class ContactSalesPage(BasePage):
    # Тестовые данные
    FIRST_NAME = "John"
    LAST_NAME = "Doe"

    def fill_first_name(self):
        self.page.get_by_label("First name").fill(self.FIRST_NAME)

    def fill_last_name(self):
        self.page.get_by_label("Last name").fill(self.LAST_NAME)

    def fill_form(self):
        self.fill_first_name()
        self.fill_last_name()

    def check_filled_form(self):
        first_name = self.page.get_by_label("First name")
        last_name = self.page.get_by_label("Last name")
        expect(first_name).to_have_value(self.FIRST_NAME)
        expect(last_name).to_have_value(self.LAST_NAME)
