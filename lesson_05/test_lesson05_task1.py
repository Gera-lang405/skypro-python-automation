from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://httpbin.qa-territory.online/"


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(BASE_URL)
        start_url = driver.current_url

        driver.find_element(By.LINK_TEXT, "HTML Form").click()
        wait.until(EC.url_contains("/forms/post"))
        assert driver.current_url.endswith("/forms/post")

        driver.back()
        wait.until(EC.url_to_be(start_url))
        assert driver.current_url == start_url
    finally:
        driver.quit()
