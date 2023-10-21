import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(int(x))

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    submit_button = browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
