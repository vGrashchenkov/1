from pages.register import Register


def test_register_page(browser):
    browser.implicitly_wait(3)
    browser.get(browser.url + Register.PATH)
    browser.find_element(**Register.HEADING)
    browser.find_element(**Register.LOGIN_LINK)
    browser.find_element(**Register.CONTINUE_BTN)

    personal_details = browser.find_element(**Register.PERSONAL_DETAILS)
    personal_details.find_element(**Register.INPUT_FIRST_NAME)
    personal_details.find_element(**Register.INPUT_LAST_NAME)
    personal_details.find_element(**Register.INPUT_EMAIL)
    personal_details.find_element(**Register.INPUT_TELEPHONE)

    password = browser.find_element(**Register.PASSWORD)
    password.find_element(**Register.INPUT_PASSWORD)
    password.find_element(**Register.INPUT_PASSWORD_CONFIRM)

    newsletter = browser.find_element(**Register.NEWSLETTER)
    newsletter.find_element(**Register.RADIO_BTN)
    newsletter.find_element(**Register.YES)
    newsletter.find_element(**Register.NO)
