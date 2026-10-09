from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

PRODUCTS = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-onesie",
]


def test_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    # Авторизация
    wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    for product_id in PRODUCTS:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    # Переход в корзину и оформление заказа
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.visibility_of_element_located(
        (By.ID, "first-name"))).send_keys("Георгий")
    driver.find_element(By.ID, "last-name").send_keys("Селиванов")
    driver.find_element(By.ID, "postal-code").send_keys("354000")
    driver.find_element(By.ID, "continue").click()

    # Чтение итоговой стоимости
    total_text = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".summary_total_label"))).text
    total = total_text.replace("Total:", "").strip()

    driver.quit()

    assert total == "$58.29"
