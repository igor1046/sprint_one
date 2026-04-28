from pages.selenium.base_page import BasePage


class ContactSalesPage(BasePage):
    FIRST_NAME = "John"
    LAST_NAME = "Doe"

    FIRST_NAME_INPUT = "#form-field-first_name"
    LAST_NAME_INPUT = "#form-field-last_name"

    def fill_form(self):
        self.fill(self.FIRST_NAME_INPUT, self.FIRST_NAME)
        self.fill(self.LAST_NAME_INPUT, self.LAST_NAME)

    def check_filled_form(self):
        assert self.get_value(self.FIRST_NAME_INPUT) == self.FIRST_NAME
        assert self.get_value(self.LAST_NAME_INPUT) == self.LAST_NAME
