import pytest
from selenium import webdriver
from calc_page import CalculatorPage
import time


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
