from practice_2.pages.login_page import LoginPage

def test_login_success(driver):
    page = LoginPage(driver)

    page.open()
    page.login("standard_user", "secret_sauce")

    assert "inventory" in page.get_url(), "inventory должен быть в url после логина"