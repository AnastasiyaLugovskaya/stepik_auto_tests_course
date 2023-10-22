import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Тут путь к конкретному исполняемому файлу (lesson_2_2_step7.py)
#print(os.path.abspath(__file__))
# А это путь к папке где он лежит (lesson2)
#print(os.path.abspath(os.path.dirname(__file__)))
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Solasanchik")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Kabanchik")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("Solasanchik@mailforspam.com")

    attachment = browser.find_element(By.ID, "file")
    attachment.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()


