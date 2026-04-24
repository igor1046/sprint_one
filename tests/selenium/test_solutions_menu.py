import pytest
from pages.selenium.cicd_page import CiCdPage
from pages.selenium.contact_sales_page import ContactSalesPage
from pages.selenium.home_page import HomePage
from pages.selenium.resources_menu import ResourcesMenu
from pages.selenium.solutions_menu import SolutionsMenu

@pytest.mark.ui
def test_contact_sales(driver):
    home = HomePage(driver)
    menu = SolutionsMenu(driver)
    cicd = CiCdPage(driver)
    contact = ContactSalesPage(driver)

    home.open()
    home.open_solutions_menu()
    menu.click_ci_cd()
    cicd.click_contact_sales()

    contact.fill_form()
    contact.check_filled_form()

@pytest.mark.ui
def test_resources_sel(driver):
    home = HomePage(driver)
    resources = ResourcesMenu(driver)

    home.open()
    home.open_resources_menu()
    actual_topics = resources.get_topics()

    assert set(resources.EXPECTED_TOPICS).issubset(set(actual_topics))
