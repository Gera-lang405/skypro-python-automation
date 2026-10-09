from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru"

# Cookie SESSION взяты из реальных аккаунтов:
# DevTools -> Application -> Cookies -> https://gitflic.ru
USER_1_ALIAS = "georgi"
USER_1_SESSION = "ВСТАВИТЬ_SESSION_АККАУНТА_GEORGI"

USER_2_ALIAS = "ЛОГИН_ВТОРОГО_АККАУНТА"
USER_2_SESSION = "ВСТАВИТЬ_SESSION_ВТОРОГО_АККАУНТА"


def login_with_cookie(driver, session_value):
    driver.add_cookie({"name": "SESSION", "value": session_value})
    driver.refresh()
    # Страница проектов без авторизации перенаправляет на /auth/login
    driver.get(f"{BASE_URL}/project")
    assert "/auth/login" not in driver.current_url


def open_profile(driver, wait, alias):
    driver.get(f"{BASE_URL}/user/{alias}")
    wait.until(EC.url_contains(f"/user/{alias}"))
    return driver.current_url


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        # Пользователь 1
        driver.get(BASE_URL)
        login_with_cookie(driver, USER_1_SESSION)
        user_1_url = open_profile(driver, wait, USER_1_ALIAS)

        # Выход: очищаем cookie
        driver.delete_all_cookies()
        driver.refresh()

        # Пользователь 2
        login_with_cookie(driver, USER_2_SESSION)
        user_2_url = open_profile(driver, wait, USER_2_ALIAS)

        assert user_1_url != user_2_url
    finally:
        driver.quit()
