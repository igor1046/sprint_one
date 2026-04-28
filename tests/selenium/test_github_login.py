import os

import pytest
from dotenv import load_dotenv

from pages.selenium.github_login_page import GitHubLoginPage

load_dotenv()


@pytest.mark.ui
def test_successful_login_sel(driver):
    username = os.getenv("GH_USER")
    password = os.getenv("GH_PASS")

    if not username or not password:
        pytest.skip("GH_USER или GH_PASS не указаны в .env файле")

    login_page = GitHubLoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    login_page.should_be_logged_in()


@pytest.mark.ui
def test_failed_login_sel(driver):
    login_page = GitHubLoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_password123")
    login_page.should_show_error_contains("Incorrect username or password.")
