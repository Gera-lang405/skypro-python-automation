import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru"

# Cookie SESSION взяты из двух реальных аккаунтов gitflic.ru
# (DevTools -> Application -> Cookies -> https://gitflic.ru).
# Значения передаются через переменные окружения, а не хранятся в коде:
# репозиторий публичный, и cookie в нём дали бы доступ к аккаунтам.
USER_1_SESSION = os.environ.get("GITFLIC_SESSION_USER_1", "")
USER_2_SESSION = os.environ.get("GITFLIC_SESSION_USER_2", "")


def login_with_cookie(driver, session_value):
    driver.add_cookie({"name": "SESSION", "value": session_value})
    driver.refresh()
    # Без авторизации страница проектов перенаправляет на /auth/login
    driver.get(f"{BASE_URL}/project")
    assert "/auth/login" not in driver.current_url


def open_profile(driver, wait):
    # Логотип в шапке ведёт на страницу текущего пользователя
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a.navbar-main__logo"))).click()
    wait.until(EC.url_contains("/user/"))
    return driver.current_url


@pytest.mark.skipif(
    not (USER_1_SESSION and USER_2_SESSION),
    reason="Задайте GITFLIC_SESSION_USER_1 и GITFLIC_SESSION_USER_2")
def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        # Пользователь 1
        driver.get(BASE_URL)
        login_with_cookie(driver, USER_1_SESSION)
        user_1_url = open_profile(driver, wait)

        # Выход: очищаем cookie
        driver.delete_all_cookies()
        driver.refresh()

        # Пользователь 2
        login_with_cookie(driver, USER_2_SESSION)
        user_2_url = open_profile(driver, wait)

        assert user_1_url != user_2_url
    finally:
        driver.quit()
