import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(int(x))

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    time.sleep(20)
    browser.quit()