from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie",
]


def test_shop_total():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page = MainPage(driver)
        main_page.add_products_to_cart(PRODUCTS)
        main_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_items = cart_page.get_item_names()
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Георгий", "Селиванов", "354000")
        checkout_page.click_continue()
        total = checkout_page.get_total()
    finally:
        # Закрытие браузера
        driver.quit()

    assert cart_items == PRODUCTS
    assert total == "$58.29"
