from selenium.webdriver.common.by import By


def test_admin_login_page(browser):
    browser.get(browser.url + '/admin')
    browser.find_element(by=By.ID, value='input-username')
    browser.find_element(by=By.ID, value='input-password')
    browser.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]')
    browser.find_element(by=By.LINK_TEXT, value='Forgotten Password')
    browser.find_element(by=By.LINK_TEXT, value='OpenCart')
    browser.find_element(by=By.CLASS_NAME, value='panel-title')
