import pytest
from selenium import webdriver
from calc_page import CalculatorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(setup):
    calculator = CalculatorPage(setup)
    calculator.enter_delay("45")
    calculator.click_number(7)
    calculator.click_number("+")
    calculator.click_number(8)
    calculator.click_number("=")

    result = calculator.get_result("15")

    assert result == "15", f"Ожидали '15', но получили '{result}'"
    setup.quit()
