import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# ---------- capitalize ----------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("тест", "Тест"),
    ("python", "Python"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("123", "123"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", " "),
    ("   ", "   "),
    ("123abc", "123abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises((TypeError, AttributeError)):
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skyPro", "SkyPro"),
    ("hello World", "Hello World"),
])
def test_capitalize_keeps_other_letters(input_str, expected):
    # Дефект №1 (см. defects.txt): метод меняет регистр остальных букв
    assert string_utils.capitalize(input_str) == expected


# ---------- trim ----------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" SkyPro", "SkyPro"),
    ("  04 апреля 2023", "04 апреля 2023"),
    ("  тест", "тест"),
    ("skypro", "skypro"),
    ("  sky pro  ", "sky pro  "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("     ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none():
    with pytest.raises((TypeError, AttributeError)):
        string_utils.trim(None)


# ---------- contains ----------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "o", True),
    ("SkyPro", "Pro", True),
    ("Тест", "Т", True),
    ("123", "2", True),
    ("04 апреля 2023", " ", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "s", False),
    ("", "a", False),
    (" ", "a", False),
    ("123", "4", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (None, "S"),
    ("SkyPro", None),
])
def test_contains_none(input_str, symbol):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.contains(input_str, symbol)


# ---------- delete_symbol ----------

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
    ("Тест", "Т", "ест"),
    ("123", "2", "13"),
    ("04 апреля 2023", " ", "04апреля2023"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("SkyPro", "s", "SkyPro"),
    ("", "a", ""),
    (" ", " ", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (None, "S"),
    ("SkyPro", None),
])
def test_delete_symbol_none(input_str, symbol):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.delete_symbol(input_str, symbol)
