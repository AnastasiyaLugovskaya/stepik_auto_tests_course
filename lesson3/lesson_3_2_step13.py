import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestUniqueSelectors(unittest.TestCase):
    def execution(self, link):
        try:
            browser = webdriver.Chrome()
            browser.get(link)

            name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
            name.send_keys("value")

            last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
            last_name.send_keys("value")

            email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
            email.send_keys("value")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            return welcome_text
        finally:
            browser.quit()

    expected_message = 'Congratulations! You have successfully registered!'

    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
        actual_message = self.execution(link)
        self.assertEqual(actual_message, self.expected_message,
                         f"Expected{self.expected_message}, but got {actual_message}")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        actual_message = self.execution(link)
        self.assertEqual(actual_message, self.expected_message,
                         f"Expected{self.expected_message}, but got {actual_message}")


if __name__ == "__main__":
    unittest.main()
