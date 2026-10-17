from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """Страница корзины."""

    ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Сохраняет драйвер и создаёт явное ожидание.

        :param driver: WebDriver — драйвер браузера.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_item_names(self) -> list[str]:
        """
        Возвращает названия товаров в корзине.

        :return: list[str] — названия товаров в порядке отображения.
        """
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]

    def click_checkout(self) -> None:
        """
        Нажимает кнопку Checkout.

        :return: None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
