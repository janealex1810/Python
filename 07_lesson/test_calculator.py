import pytest
from selenium import webdriver
from calc_page import CalculatorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(setup):
    calculator = CalculatorPage(setup)
    calculator.enter_delay("45")
    calculator.click_number(7)
    calculator.click_operator("+")
    calculator.click_number(8)
    calculator.click_equal()

    WebDriverWait(setup, 60).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )

    result = calculator.get_result()
    assert result == "15"
