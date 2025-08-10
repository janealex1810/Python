import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following-sibling::div//button").click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.XPATH, "//button[text()='Checkout']").click()

    def get_item_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label").text


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, ".btn_primary").click()


class TestSauceDemo:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        yield
        self.driver.quit()

    def test_shopping_cart(self, setup):
        login_page = LoginPage(self.driver)
        login_page.input_username("standard_user")
        login_page.input_password("secret_sauce")
        login_page.click_login()

        main_page = MainPage(self.driver)
        main_page.add_to_cart("Sauce Labs Backpack")
        main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        main_page.add_to_cart("Sauce Labs Onesie")

        main_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_form("John", "Doe", "12345")

        total = cart_page.get_item_total()
        assert "Total: $58.29" in total
