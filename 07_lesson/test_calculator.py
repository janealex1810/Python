import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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


class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield
        self.driver.quit()

    def test_calculator(self, setup):
        calculator = CalculatorPage(self.driver)
        calculator.enter_delay("45")

        calculator.click_number(7)
        calculator.click_operator("+")
        calculator.click_number(8)
        calculator.click_equal()

        time.sleep(45)

        result = calculator.get_result()
        assert result == "15"
