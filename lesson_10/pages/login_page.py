from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Страница авторизации магазина."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

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
        Открывает страницу авторизации.

        :return: None.
        """
        self.driver.get(self.URL)

    def enter_username(self, username: str) -> None:
        """
        Вводит логин.

        :param username: str — имя пользователя.
        :return: None.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: str — пароль пользователя.
        :return: None.
        """
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа.

        :return: None.
        """
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str) -> None:
        """
        Авторизуется: вводит логин и пароль и нажимает кнопку входа.

        :param username: str — имя пользователя.
        :param password: str — пароль пользователя.
        :return: None.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
