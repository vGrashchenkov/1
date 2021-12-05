from pages.admin_login import AdminLogin


def test_admin_login_page(browser):
    browser.implicitly_wait(3)
    browser.get(browser.url + AdminLogin.PATH)
    browser.find_element(**AdminLogin.INPUT_USERNAME)
    browser.find_element(**AdminLogin.INPUT_PASSWORD)
    browser.find_element(**AdminLogin.SUBMIT)
    browser.find_element(**AdminLogin.FORGOTTEN_PASSWORD)
    browser.find_element(**AdminLogin.OPEN_CART_LINK)
    browser.find_element(**AdminLogin.PANEL_TITLE)
