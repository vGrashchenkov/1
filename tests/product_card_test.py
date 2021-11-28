import pytest

from pages.product_card import ProductCard


@pytest.mark.parametrize('product', ['/desktops/test', '/tablet/samsung-galaxy-tab-10-1'])
def test_product_card(browser, product):
    browser.implicitly_wait(3)
    browser.get(browser.url + ProductCard(product).PATH)

    product_options = browser.find_element(**ProductCard.PRODUCT_OPTIONS)
    product_options.find_element(**ProductCard.FINAL_PRICE)
    product_options.find_element(**ProductCard.AVAILABLE_OPTIONS)
    product_options.find_element(**ProductCard.NAME)
    product_options.find_element(**ProductCard.ADD_TO_CARD_BTN)

    description = browser.find_element(**ProductCard.DESCRIPTION)
    description.find_element(**ProductCard.PICTURES)
    description.find_element(**ProductCard.TABS)
