import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_is_available(browser):
    browser.get(link)

    # check for different language
    # time.sleep(30) # turn off comment and run command "pytest -s --language=fr test_items.py"

    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket'))
    )

    assert bool(element)
