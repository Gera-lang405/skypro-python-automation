from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

FORM_DATA = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "zip-code": "",
    "city": "Москва",
    "country": "Россия",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "job-position": "QA",
    "company": "SkyPro",
}


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)

        for name, value in FORM_DATA.items():
            field = wait.until(
                EC.visibility_of_element_located((By.NAME, name)))
            field.send_keys(value)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        zip_code = wait.until(
            EC.visibility_of_element_located((By.ID, "zip-code")))
        assert "alert-danger" in zip_code.get_attribute("class")

        for field_id in FORM_DATA:
            if field_id == "zip-code":
                continue
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class")
    finally:
        driver.quit()
