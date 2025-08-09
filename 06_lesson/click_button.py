from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()

message = driver.find_element(By.ID, "ajaxReturn").text
print(message)

driver.quit()
