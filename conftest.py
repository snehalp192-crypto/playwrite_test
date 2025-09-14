import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
