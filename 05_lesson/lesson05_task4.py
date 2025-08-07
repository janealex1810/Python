from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/login")

    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text)

finally:

    driver.quit()
