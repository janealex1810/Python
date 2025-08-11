import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_flow(driver):

    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        inventory_page.add_item_to_cart(item)
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info("Иван", "Петров", "123456")

    total = checkout_page.get_total_amount()
    assert total == "Total: $58.29"
