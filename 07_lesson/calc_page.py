from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.send_keys(delay)

    def click_number(self, number):
        self.driver.find_element(By.CSS_SELECTOR, f'button#number-{number}').click()

    def click_operator(self, operator):
        self.driver.find_element(By.CSS_SELECTOR, f'button#operator-{operator}').click()

    def click_equal(self):
        self.driver.find_element(By.CSS_SELECTOR, "button#calculate").click()

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#result").text
