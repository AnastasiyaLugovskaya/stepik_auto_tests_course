import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    total = int(x) + int(y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()