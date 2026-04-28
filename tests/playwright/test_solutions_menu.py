import pytest

from pages.playwright.cicd_page import CiCdPage
from pages.playwright.contact_sales_page import ContactSalesPage
from pages.playwright.home_page import HomePage
from pages.playwright.resources_menu import ResourcesMenu
from pages.playwright.solutions_menu import SolutionsMenu


@pytest.mark.ui
def test_contact_sales(page):
    home = HomePage(page)
    menu = SolutionsMenu(page)
    cicd = CiCdPage(page)
    contact = ContactSalesPage(page)

    home.open()
    home.open_solutions_menu()
    menu.click_ci_cd()
    cicd.click_contact_sales()

    contact.fill_form()
    contact.check_filled_form()


@pytest.mark.ui
def test_resources_topics(page):
    home = HomePage(page)
    resources = ResourcesMenu(page)

    home.open()
    home.open_resources_menu()
    actual = resources.get_topics()

    expected = [
        "AI",
        "Software Development",
        "DevOps",
        "Security",
        "View all topics",
    ]

    assert set(expected).issubset(set(actual))
