import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(int(x))

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(result)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()