# Урок 10. Allure-отчёт для тестов Page Object

Решение домашнего задания №7 «PageObject», дополненное документацией
кода и разметкой Allure.

## Структура

| Файл | Что внутри |
| --- | --- |
| `pages/calculator_page.py` | `CalculatorPage` — страница медленного калькулятора |
| `pages/login_page.py` | `LoginPage` — авторизация в магазине |
| `pages/main_page.py` | `MainPage` — список товаров, добавление в корзину |
| `pages/cart_page.py` | `CartPage` — корзина и кнопка Checkout |
| `pages/checkout_page.py` | `CheckoutPage` — форма покупателя и итоговая сумма |
| `test_calculator.py` | тест калькулятора (Google Chrome) |
| `test_shop.py` | тест интернет-магазина (Firefox) |

Все методы классов страниц описаны docstring-ами с типами параметров
и возвращаемых значений. В тестах шаги и проверки размечены
`with allure.step(...)`, у тестов есть `@allure.title`,
`@allure.description`, `@allure.feature` и `@allure.severity`.

## Подготовка

Нужны Python 3, браузеры **Google Chrome** и **Firefox**.

Установить библиотеки:

```bash
pip install selenium pytest allure-pytest
```

Для просмотра отчёта нужен **Allure Report** (консольная утилита `allure`,
для неё нужна Java 8+). Варианты установки:

- Windows: `scoop install allure`
- macOS: `brew install allure`
- любая ОС: скачать архив со страницы
  [Allure releases](https://github.com/allure-framework/allure2/releases),
  распаковать и добавить папку `bin` в переменную `PATH`.

## Как запустить тесты и сформировать результаты для отчёта

Из корня репозитория:

```bash
pytest lesson_10 --alluredir=lesson_10/allure-results
```

Результаты прогона сохранятся в папку `lesson_10/allure-results`.
Тест калькулятора идёт около минуты: в нём задержка 45 секунд.

## Как просмотреть отчёт

Вариант 1 — собрать отчёт и сразу открыть его в браузере:

```bash
allure serve lesson_10/allure-results
```

Вариант 2 — сохранить отчёт в папку и открыть его:

```bash
allure generate lesson_10/allure-results -o lesson_10/allure-report --clean
allure open lesson_10/allure-report
```

В отчёте видны названия тестов, описания, разделы (`feature`),
важность (`severity`) и все шаги с проверками.

Папки `allure-results` и `allure-report` в репозиторий не добавляются
(указаны в `.gitignore`).
