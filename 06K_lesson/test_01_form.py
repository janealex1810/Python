import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_id, value in fields.items():
        driver.find_element(By.ID, field_id).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "is-invalid" in zip_code.get_attribute("class")

    for field_id in fields.keys():
        element = driver.find_element(By.ID, field_id)
        assert "is-valid" in element.get_attribute("class")
