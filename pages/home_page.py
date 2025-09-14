from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_LINK = "a[aria-label='go to login']"
    HEADER = "h1"

    def get_header_text(self):
        return self.get_text(self.HEADER)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)
