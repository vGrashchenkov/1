from pages.main import Main


def test_main_page(browser):
    browser.implicitly_wait(3)
    browser.get(browser.url)
    browser.find_element(**Main.LOGO)
    browser.find_element(**Main.DIV_SEARCH) \
        .find_element(**Main.INPUT_SEARCH)
    browser.find_element(**Main.DIV_SEARCH) \
        .find_element(**Main.BUTTON_SEARCH)
    browser.find_element(**Main.DIV_CART) \
        .find_element(**Main.BUTTON_SEARCH) \
        .find_element(**Main.SPAN_CART)
    browser.find_element(**Main.SLIDESHOW)
    browser.find_element(**Main.CAROUSEL)


    assert len(browser.find_elements(**Main.MENU)) == 8
    assert len(browser.find_elements(**Main.FETURED)) == 4
