from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(int(x))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, '#solve')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
