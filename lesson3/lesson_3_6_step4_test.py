from lesson3 import auth_credentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'https://stepik.org/lesson/236895/step/1'


def test_authorize_on_stepik_account(browser):
    browser.get(link)

    login_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__auth_login')))
    login_button.click()

    auth_form_selector = 'header.light-tabs__header '
    auth_form = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, auth_form_selector)))

    login_field = browser.find_element(By.ID, 'id_login_email')
    login_field.send_keys(auth_credentials.login)

    password_field = browser.find_element(By.ID, 'id_login_password')
    password_field.send_keys(auth_credentials.password)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn')
    submit_button.click()

    assert WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(auth_form))
