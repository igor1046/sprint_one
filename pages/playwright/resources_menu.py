from playwright.sync_api import Page, expect


class ResourcesMenu:
    RESOURCES_BUTTON_NAME = "Resources"
    TOPICS_SECTION_TEXT = "Explore by topic"
    TOPIC_LINKS = "li > a:visible"

    def __init__(self, page: Page):
        self.page = page

    def get_topics(self) -> list[str]:
        # Убеждаемся, что меню Resources открыто
        resources_button = self.page.get_by_role(
            "button", name=self.RESOURCES_BUTTON_NAME
        )
        expect(resources_button).to_have_attribute("aria-expanded", "true")

        # Ищем сам блок "Explore by topic" среди видимых элементов страницы
        topics_section = self.page.get_by_text(
            self.TOPICS_SECTION_TEXT, exact=False
        ).first
        expect(topics_section).to_be_visible()

        # Берем ближайший список после заголовка секции
        topics = topics_section.locator("xpath=following::ul[1]").locator(
            self.TOPIC_LINKS
        )

        # t = text
        return [t.strip() for t in topics.all_text_contents() if t.strip()]
