from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
DELAY = 45


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)

        delay_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(str(DELAY))

        for key in ["7", "+", "8", "="]:
            driver.find_element(
                By.XPATH, f"//div[@class='keys']/span[text()='{key}']").click()

        WebDriverWait(driver, DELAY + 5).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15"
    finally:
        driver.quit()
