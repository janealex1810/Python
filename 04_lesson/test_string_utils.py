from string_utils import StringUtils

string_utils = StringUtils()


def test_capitalize():
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("123abc") == "123abc"


def test_capitalize_no_change():
    assert string_utils.capitalize("Already Capitalized") == "Already capitalized"


def test_trim():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("   hello world   ") == "hello world"
    assert string_utils.trim("no_space") == "no_space"
    assert string_utils.trim("   ") == ""


def test_trim_no_change():
    assert string_utils.trim("hello") == "hello"


def test_contains():
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("hello world", " ") is True


def test_contains_empty_string():
    assert string_utils.contains("", "a") is False
    assert string_utils.contains("test", "") is False


def test_delete_symbol():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("hello world", "o") == "hell wrld"
    assert string_utils.delete_symbol("aaaaaa", "a") == ""
    assert string_utils.delete_symbol("test", "x") == "test"


def test_delete_symbol_not_found():
    assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
