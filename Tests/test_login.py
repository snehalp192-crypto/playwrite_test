import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils import config
import time

def test_login_from_home(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate(config.BASE_URL)

    home_page.go_to_login()

    time.sleep(5)

    login_page.login(config.USER_NAME, config.PASSWORD)

    time.sleep(3)

