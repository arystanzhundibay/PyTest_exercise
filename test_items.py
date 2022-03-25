import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    try:
        browser.get(link)
        add_to_basket_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        time.sleep(10)
    except Exception:
        add_to_basket_button = 0
    assert add_to_basket_button, 'Add to basket button not found'
