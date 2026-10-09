from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru"

# Cookie взяты из реальных аккаунтов: DevTools -> Application -> Cookies
USER_1 = {
    "alias": "georgi",
    "cookie": {"name": "COOKIE_NAME", "value": "COOKIE_VALUE_USER_1"},
}
USER_2 = {
    "alias": "USER_2_ALIAS",
    "cookie": {"name": "COOKIE_NAME", "value": "COOKIE_VALUE_USER_2"},
}


def login_with_cookie(driver, wait, cookie):
    driver.add_cookie(cookie)
    driver.refresh()
    # Страница проектов без авторизации перенаправляет на /auth/login
    driver.get(f"{BASE_URL}/project")
    wait.until(EC.url_contains("/project"))
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
        login_with_cookie(driver, wait, USER_1["cookie"])
        user_1_url = open_profile(driver, wait, USER_1["alias"])

        # Выход: очищаем cookie
        driver.delete_all_cookies()
        driver.refresh()

        # Пользователь 2
        login_with_cookie(driver, wait, USER_2["cookie"])
        user_2_url = open_profile(driver, wait, USER_2["alias"])

        assert user_1_url != user_2_url
    finally:
        driver.quit()
