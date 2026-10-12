from selenium import webdriver

from pages.calculator_page import CalculatorPage

DELAY = 45


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        calculator = CalculatorPage(driver)
        calculator.open()
        calculator.set_delay(DELAY)
        calculator.click_buttons("7", "+", "8", "=")
        result = calculator.get_result(timeout=DELAY + 5)
    finally:
        driver.quit()

    assert result == "15"
