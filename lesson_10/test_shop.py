import allure
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


@allure.title("Итоговая стоимость заказа из трёх товаров")
@allure.description("Авторизация под standard_user, добавление трёх товаров "
                    "в корзину, оформление заказа и проверка суммы $58.29.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        with allure.step("Открыть сайт магазина"):
            login_page.open()
        with allure.step("Авторизоваться как standard_user"):
            login_page.login("standard_user", "secret_sauce")

        main_page = MainPage(driver)
        with allure.step("Добавить товары в корзину"):
            main_page.add_products_to_cart(PRODUCTS)
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Прочитать список товаров в корзине"):
            cart_items = cart_page.get_item_names()
        with allure.step("Нажать Checkout"):
            cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        with allure.step("Заполнить форму: имя, фамилия, почтовый индекс"):
            checkout_page.fill_form("Георгий", "Селиванов", "354000")
        with allure.step("Нажать Continue"):
            checkout_page.click_continue()
        with allure.step("Прочитать итоговую стоимость"):
            total = checkout_page.get_total()
    finally:
        # Закрытие браузера
        driver.quit()

    with allure.step("Проверить, что в корзине три выбранных товара"):
        assert cart_items == PRODUCTS
    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == "$58.29"
