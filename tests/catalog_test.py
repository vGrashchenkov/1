from pages.catalog import Desktops


def test_catalog_desktops(browser):
    browser.implicitly_wait(3)
    browser.get(browser.url + Desktops.PATH)
    browser.find_element(**Desktops.DESKTOPS_DESCR)
    browser.find_element(**Desktops.ITEMS)
    browser.find_element(**Desktops.REFINE_SEARCH)
    browser.find_element(**Desktops.GRID_VIEW_BUTTON)
    browser.find_element(**Desktops.LIST_VIEW_BUTTON)
    browser.find_element(**Desktops.BREADCRUMB)
    browser.find_element(**Desktops.LEFT_MEU)


