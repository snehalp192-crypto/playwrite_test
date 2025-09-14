class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.click(locator)

    def type_text(self, locator: str, text: str):
        self.page.fill(locator, text)

    def get_text(self, locator: str):
        return self.page.inner_text(locator)

    def is_visible(self, locator: str):
        return self.page.is_visible(locator)
