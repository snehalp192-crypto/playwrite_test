from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    URL = "https://verbals.io/login"
    USERNAME_INPUT = "input[name='email']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def load(self):
        self.navigate(self.URL)
        self.login_button(self)

    def login(self, username, password):
        self.page.click(self.USERNAME_INPUT)
        self.page.type(self.USERNAME_INPUT, username, delay=50)
        self.page.press(self.USERNAME_INPUT, "Tab")

        # self.page.click(self.PASSWORD_INPUT)
        self.page.type(self.PASSWORD_INPUT, password, delay=50)

        self.page.press(self.PASSWORD_INPUT, "Tab")
        self.click(self.LOGIN_BUTTON)
