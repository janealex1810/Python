from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_number(self, number):
        self.driver.find_element(By.XPATH, f'//*[text()="{number}"]').click()

    def get_result(self, expected_text, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text)
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
