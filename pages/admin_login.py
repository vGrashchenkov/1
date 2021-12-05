from selenium.webdriver.common.by import By


class AdminLogin:

    PATH = '/admin'
    INPUT_USERNAME = {'by': By.ID, 'value': 'input-username'}
    INPUT_PASSWORD = {'by': By.ID, 'value': 'input-password'}
    SUBMIT = {'by': By.CSS_SELECTOR, 'value': 'button[type="submit"]'}
    FORGOTTEN_PASSWORD = {'by': By.LINK_TEXT, 'value': 'Forgotten Password'}
    OPEN_CART_LINK = {'by': By.LINK_TEXT, 'value': 'OpenCart'}
    PANEL_TITLE = {'by': By.CLASS_NAME, 'value': 'panel-title'}


