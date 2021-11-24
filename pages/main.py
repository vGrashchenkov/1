from selenium.webdriver.common.by import By


class Main:
    LOGO = {'by': By.CSS_SELECTOR, 'value': '#logo > a > img'}
    DIV_SEARCH = {'by': By.ID, 'value': 'search'}
    INPUT_SEARCH = {'by': By.NAME, 'value': 'search'}
    BUTTON_SEARCH = {'by': By.CSS_SELECTOR, 'value': 'button[type="button"]'}
    DIV_CART = {'by': By.ID, 'value': 'cart'}
    BUTTON_CART = {'by': By.CSS_SELECTOR, 'value': 'button[type="button"]'}
    SPAN_CART = {'by': By.ID, 'value': 'cart-total'}
    MENU = {'by': By.CSS_SELECTOR, 'value': 'ul.navbar-nav > li'}
    FETURED = {'by': By.CLASS_NAME, 'value': 'product-thumb'}
