from selenium.webdriver.common.by import By


class ProductCard:

    def __init__(self, product_path):
        self.PATH = product_path

    PRODUCT_OPTIONS = {'by': By.CSS_SELECTOR, 'value': '#content .col-sm-4'}
    FINAL_PRICE = {'by': By.CSS_SELECTOR, 'value': '#content .col-sm-4 h2'}
    AVAILABLE_OPTIONS = {'by': By.CSS_SELECTOR, 'value': '#product'}
    NAME = {'by': By.CSS_SELECTOR, 'value': 'h1'}
    ADD_TO_CARD_BTN = {'by': By.ID, 'value': 'button-cart'}
    DESCRIPTION = {'by': By.CSS_SELECTOR, 'value': '.col-sm-8'}
    PICTURES = {'by': By.CSS_SELECTOR, 'value': '.thumbnails'}
    TABS = {'by': By.CSS_SELECTOR, 'value': '.nav-tabs'}
