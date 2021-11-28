import pytest

from pages.catalog import Catalog


@pytest.mark.parametrize('catalog_path', ['/desktops', '/laptop-notebook'])
def test_catalog_desktops(browser, catalog_path):
    browser.implicitly_wait(3)
    browser.get(browser.url + Catalog(catalog_path).PATH)
    browser.find_element(**Catalog.DESKTOPS_DESCR)
    browser.find_element(**Catalog.ITEMS)
    browser.find_element(**Catalog.REFINE_SEARCH)
    browser.find_element(**Catalog.GRID_VIEW_BUTTON)
    browser.find_element(**Catalog.LIST_VIEW_BUTTON)
    browser.find_element(**Catalog.BREADCRUMB)
    browser.find_element(**Catalog.LEFT_MEU)
