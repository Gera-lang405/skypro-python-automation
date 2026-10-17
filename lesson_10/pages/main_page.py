from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    """Главная страница магазина со списком товаров."""

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Сохраняет драйвер и создаёт явное ожидание.

        :param driver: WebDriver — драйвер браузера.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по его названию.

        :param product_name: str — название товара,
            например "Sauce Labs Backpack".
        :return: None.
        """
        # Кнопка товара: add-to-cart-sauce-labs-backpack и т. п.
        button_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.wait.until(
            EC.element_to_be_clickable((By.ID, button_id))).click()

    def add_products_to_cart(self, product_names: list[str]) -> None:
        """
        Добавляет в корзину несколько товаров.

        :param product_names: list[str] — названия товаров.
        :return: None.
        """
        for name in product_names:
            self.add_to_cart(name)

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None.
        """
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
