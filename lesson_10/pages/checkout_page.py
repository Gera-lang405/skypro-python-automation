from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """Оформление заказа: форма данных покупателя и итоговая стоимость."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Сохраняет драйвер и создаёт явное ожидание.

        :param driver: WebDriver — драйвер браузера.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму данными покупателя.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_code: str — почтовый индекс.
        :return: None.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(
            *self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку Continue.

        :return: None.
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self) -> str:
        """
        Возвращает итоговую стоимость заказа.

        :return: str — сумма без подписи "Total:", например "$58.29".
        """
        total_text = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)).text
        return total_text.replace("Total:", "").strip()
