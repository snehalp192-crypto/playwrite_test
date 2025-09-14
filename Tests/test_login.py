import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils import config
import time

def test_login_from_home(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # Step 1: Navigate to homepage
    home_page.navigate(config.BASE_URL)

    # Step 2: Click Login
    home_page.go_to_login()
    # assert "/login" in page.url  # confirm navigation
    time.sleep(5)
    # Step 3: Perform login
    login_page.login(config.USER_NAME, config.PASSWORD)

    time.sleep(3)
    # Step 4: Verify success (adjust selector after login!)
    # assert page.is_visible("text=Dashboard") or page.is_visible("text=Welcome")
