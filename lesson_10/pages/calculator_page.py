from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Страница медленного калькулятора."""

    URL = ("https://bonigarcia.dev/"
           "selenium-webdriver-java/slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")
    SPINNER = (By.ID, "spinner")

    def __init__(self, driver: WebDriver) -> None:
        """
        Сохраняет драйвер и создаёт явное ожидание.

        :param driver: WebDriver — драйвер браузера.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None.
        """
        self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        """
        Вводит задержку вычисления в поле #delay.

        :param seconds: int — задержка в секундах.
        :return: None.
        """
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, key: str) -> None:
        """
        Нажимает одну кнопку калькулятора.

        :param key: str — текст кнопки, например "7", "+" или "=".
        :return: None.
        """
        button = (By.XPATH, f"//div[@class='keys']/span[text()='{key}']")
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def click_buttons(self, *keys: str) -> None:
        """
        Нажимает кнопки калькулятора по очереди.

        :param keys: str — тексты кнопок в порядке нажатия.
        :return: None.
        """
        for key in keys:
            self.click_button(key)

    def get_result(self, timeout: int) -> str:
        """
        Ждёт окончания вычисления и возвращает результат с экрана.

        После нажатия "=" появляется спиннер; он исчезает,
        когда на экране появляется результат.

        :param timeout: int — сколько секунд ждать результат.
        :return: str — текст на экране калькулятора.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.SPINNER))
        return self.driver.find_element(*self.RESULT_SCREEN).text
