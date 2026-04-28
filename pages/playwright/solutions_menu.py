from playwright.sync_api import Page, expect


class SolutionsMenu:

    def __init__(self, page: Page):
        self.page = page

    def click_ci_cd(self):
        ci_cd_link = self.page.get_by_role("link", name="CI/CD")
        expect(ci_cd_link).to_be_visible()
        ci_cd_link.click()
