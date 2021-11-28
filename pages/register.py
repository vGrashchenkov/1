from selenium.webdriver.common.by import By


class Register:

    PATH = '/index.php?route=account/register'
    HEADING = {'by': By.CSS_SELECTOR, 'value': 'h1'}
    LOGIN_LINK = {'by': By.LINK_TEXT, 'value': 'login page'}

    PERSONAL_DETAILS = {'by': By.CSS_SELECTOR, 'value': '#account'}
    INPUT_FIRST_NAME = {'by': By.CSS_SELECTOR, 'value': '#input-firstname'}
    INPUT_LAST_NAME = {'by': By.CSS_SELECTOR, 'value': '#input-lastname'}
    INPUT_EMAIL = {'by': By.CSS_SELECTOR, 'value': '#input-email'}
    INPUT_TELEPHONE = {'by': By.CSS_SELECTOR, 'value': '#input-telephone'}

    PASSWORD = {'by': By.CSS_SELECTOR, 'value': 'fieldset:nth-of-type(2)'}
    INPUT_PASSWORD = {'by': By.CSS_SELECTOR, 'value': '#input-password'}
    INPUT_PASSWORD_CONFIRM = {'by': By.CSS_SELECTOR, 'value': '#input-confirm'}

    NEWSLETTER = {'by': By.CSS_SELECTOR, 'value': 'fieldset:nth-of-type(3)'}
    RADIO_BTN = {'by': By.CSS_SELECTOR, 'value': 'fieldset:nth-of-type(3) .col-sm-10'}
    YES = {'by': By.XPATH, 'value': '//label[contains(.,"Yes")]'}
    NO = {'by': By.XPATH, 'value': '//label[contains(.,"No")]'}

    CONTINUE_BTN = {'by': By.CSS_SELECTOR, 'value': '.btn-primary'}
