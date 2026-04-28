import pytest
from playwright.sync_api import expect

from pages.playwright.search_page import SearchPage


@pytest.mark.ui
@pytest.mark.parametrize("query", ["qa", "aqa", "cars"])
def test_search_results_more_than_five(page, query):
    search_page = SearchPage(page)

    # 1. Открываем поисковик
    search_page.open()

    # 2. Выполняем поиск
    search_page.search(query)

    results = search_page.results()

    # 3. Дожидаемся появления результатов (хотя бы одного)
    expect(results.first).to_be_visible()

    # 4. Проверяем, что есть минимум 6 результатов
    expect(results.nth(5)).to_be_visible()
