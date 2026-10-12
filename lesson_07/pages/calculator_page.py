from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница медленного калькулятора."""

    URL = ("https://bonigarcia.dev/"
           "selenium-webdriver-java/slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")
    SPINNER = (By.ID, "spinner")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, key):
        button = (By.XPATH, f"//div[@class='keys']/span[text()='{key}']")
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def click_buttons(self, *keys):
        for key in keys:
            self.click_button(key)

    def get_result(self, timeout):
        # После нажатия "=" появляется спиннер и исчезает,
        # когда на экране появляется результат
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.SPINNER))
        return self.driver.find_element(*self.RESULT_SCREEN).text
