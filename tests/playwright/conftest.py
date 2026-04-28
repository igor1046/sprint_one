import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """Playwright fixture that provides a browser page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10000)
        yield page
        context.close()
        browser.close()
