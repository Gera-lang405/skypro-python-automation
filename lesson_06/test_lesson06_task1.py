import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
SCREENSHOT = os.path.join(os.path.dirname(__file__), "dynamic_loading.png")


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    try:
        # 1. Открываем страницу
        driver.get(URL)

        # 2. Находим и нажимаем кнопку Start
        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
        start_button.click()

        # 3. Ждём появления текста Hello World!
        finish_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))

        # 4. Делаем скриншот страницы
        driver.save_screenshot(SCREENSHOT)

        # 5. Проверяем, что появившийся текст равен Hello World!
        assert finish_text.text == "Hello World!"
    finally:
        driver.quit()
