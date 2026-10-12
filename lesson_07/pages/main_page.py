from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Главная страница магазина со списком товаров."""

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name):
        # Кнопка товара: add-to-cart-sauce-labs-backpack и т. п.
        button_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.wait.until(
            EC.element_to_be_clickable((By.ID, button_id))).click()

    def add_products_to_cart(self, product_names):
        for name in product_names:
            self.add_to_cart(name)

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
