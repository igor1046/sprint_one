import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Selenium fixture that provides a Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Selenium Manager auto-resolves a compatible driver for installed Chrome.
    web_driver = webdriver.Chrome(options=options)
    web_driver.implicitly_wait(0)
    yield web_driver
    web_driver.quit()
