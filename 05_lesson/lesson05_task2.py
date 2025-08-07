from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    time.sleep(2)

finally:

    driver.quit()
