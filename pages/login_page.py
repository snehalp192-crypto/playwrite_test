from pages.base_page import BasePage
from playwright.sync_api import expect
import time

class LoginPage(BasePage):
    URL = "https://verbals.io/login"
    USERNAME_INPUT = "input[name='email']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    SUCCESS = 'span.tw-text-sm.tw-text-gray-600'
    verify = 'span[class="tw-text-sm tw-text-gray-600]'
    def load(self):
        self.navigate(self.URL)
        self.login_button(self)

    def login(self, username, password):

        time.sleep(10)
        success_text = self.page.locator(self.SUCCESS)
        expect(success_text).to_have_text("Success!", timeout=15000)

        self.page.click(self.USERNAME_INPUT)
        
        self.page.type(self.USERNAME_INPUT, username, delay=50)
        self.page.press(self.USERNAME_INPUT, "Tab")
        
        self.page.click(self.PASSWORD_INPUT)
        self.page.type(self.PASSWORD_INPUT, password, delay=50)
        self.page.press(self.PASSWORD_INPUT, "Tab")
        time.sleep(5)
        self.click(self.LOGIN_BUTTON)

