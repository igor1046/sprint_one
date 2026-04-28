import pytest

from pages.selenium.search_page import SearchPage


@pytest.mark.ui
@pytest.mark.parametrize("query", ["qa", "aqa", "cars"])
def test_search_sel(driver, query):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.search(query)

    assert search_page.get_results_count() > 5
