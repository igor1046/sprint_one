import os
import pytest
from dotenv import load_dotenv
from pages.playwright.github_login_page import GitHubLoginPage

# Загружаем переменные окружения
load_dotenv()

@pytest.mark.skip
def test_successful_github_login(page):
    """Тест успешной авторизации на GitHub"""
    # Получаем данные из .env
    username = os.getenv("GH_USER")
    password = os.getenv("GH_PASS")

    # Если credentials нет в .env — пропускаем тест
    if not username or not password:
        pytest.skip("GH_USER или GH_PASS не указаны в .env файле")

    login_page = GitHubLoginPage(page)
    login_page.open()
    login_page.login(username, password)

    # Проверка успешного входа
    login_page.should_be_logged_in()

    print(f"✅ Успешный логин под пользователем: {username}")

@pytest.mark.ui
def test_failed_github_login(page):
    """Тест неуспешной авторизации"""
    login_page = GitHubLoginPage(page)
    login_page.open()
    login_page.login("wrong_user", "wrong_password123")
    login_page.should_show_error("Incorrect username or password.")
