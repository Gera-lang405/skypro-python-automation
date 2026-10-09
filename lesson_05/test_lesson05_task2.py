from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORM_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get(FORM_URL)
        start_url = driver.current_url

        name_input = driver.find_element(By.NAME, "custname")
        name_input.send_keys("Георгий")

        submit_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Submit')]")
        submit_button.click()

        WebDriverWait(driver, 10).until(EC.url_changes(start_url))
        assert driver.current_url != start_url
    finally:
        driver.quit()
