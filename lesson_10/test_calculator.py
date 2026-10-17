import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage

DELAY = 45


@allure.title("Сложение 7 + 8 в медленном калькуляторе")
@allure.description("Задержка 45 секунд, нажатие кнопок 7, +, 8, = "
                    "и проверка результата 15 после окончания вычисления.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        calculator = CalculatorPage(driver)
        with allure.step("Открыть страницу калькулятора"):
            calculator.open()
        with allure.step(f"Ввести задержку {DELAY} секунд"):
            calculator.set_delay(DELAY)
        with allure.step("Нажать кнопки 7, +, 8, ="):
            calculator.click_buttons("7", "+", "8", "=")
        with allure.step("Дождаться результата вычисления"):
            result = calculator.get_result(timeout=DELAY + 5)
    finally:
        driver.quit()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15"
