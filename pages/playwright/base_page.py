from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Открывает страницу и ждёт базовой загрузки DOM"""
        self.page.goto(url, wait_until="domcontentloaded")
        self.page.wait_for_load_state("load")

    def click(self, selector: str):
        """Клик по элементу с ожиданием"""
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        """Заполнение поля"""
        self.page.locator(selector).fill(value)

    def should_have_text(self, selector: str, text: str):
        """Проверка текста элемента"""
        expect(self.page.locator(selector)).to_have_text(text)

    def should_contain_text(self, selector: str, text: str):
        """Проверка частичного совпадения текста"""
        expect(self.page.locator(selector)).to_contain_text(text)

    def should_be_visible(self, selector: str):
        """Проверка видимости элемента"""
        expect(self.page.locator(selector)).to_be_visible()
