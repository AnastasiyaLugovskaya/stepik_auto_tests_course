from lesson3 import auth_credentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math
import pytest

links = [
    'https://stepik.org/lesson/236895/step/1',  # correct
    'https://stepik.org/lesson/236896/step/1',  # correct
    'https://stepik.org/lesson/236897/step/1',  # correct
    'https://stepik.org/lesson/236898/step/1',  # The owls
    'https://stepik.org/lesson/236899/step/1',  # are not
    'https://stepik.org/lesson/236903/step/1',  # correct
    'https://stepik.org/lesson/236904/step/1',  # correct
    'https://stepik.org/lesson/236905/step/1'   # what they seem! OvO
]


@pytest.mark.parametrize('link', links)
def test_get_secret_message(browser, link):
    browser.get(link)

    login_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__auth_login')))
    login_button.click()

    login_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'id_login_email')))
    login_field.send_keys(auth_credentials.login)

    password_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'id_login_password')))
    password_field.send_keys(auth_credentials.password)

    submit_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.sign-form__btn')))
    submit_button.click()

    time.sleep(5)

    textarea = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))
    textarea.clear()
    textarea.send_keys(str(math.log(int(time.time()))))

    bttns = browser.find_elements(By.CSS_SELECTOR, 'button.again-btn')
    print(bttns, len(bttns))
    is_again_button_present = len(bttns) > 0
    if is_again_button_present:
        again_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.again-btn')))
        again_button.click()

        ok_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'footer.modal-popup__footer button:first-child')))
        ok_button.click()
    else:

        submission_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        submission_button.click()

    notice = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.lesson__hint > p'))).text

    assert 'Correct!' in notice


if __name__ == "__main__":
    pytest.main()
