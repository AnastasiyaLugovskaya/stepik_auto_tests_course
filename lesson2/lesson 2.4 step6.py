from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = 'http://suninjuly.github.io/cats.html'
    browser.get(link)

    browser.find_element(By.ID, "button")
finally:
    browser.quit()