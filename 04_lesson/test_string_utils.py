import unittest
from string_utils import StringUtils

string_utils = StringUtils()


class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.string_utils = StringUtils()

    def test_capitalize(self):
        self.assertEqual(self.string_utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.string_utils.capitalize("hello world"),
                         "Hello world")
        self.assertEqual(self.string_utils.capitalize(""), "")
        self.assertEqual(self.string_utils.capitalize("123abc"), "123abc")

    def test_capitalize_no_change(self):
        self.assertEqual(self.string_utils.capitalize(
            "Already Capitalized"), "Already capitalized")

    def test_trim(self):
        self.assertEqual(self.string_utils.trim("   skypro"), "skypro")
        self.assertEqual(self.string_utils.trim("   hello world   "),
                         "hello world")
        self.assertEqual(self.string_utils.trim("no_space"), "no_space")
        self.assertEqual(self.string_utils.trim("   "), "")

    def test_trim_no_change(self):
        self.assertEqual(self.string_utils.trim("hello"), "hello")

    def test_contains(self):
        self.assertTrue(self.string_utils.contains("SkyPro", "S"))
        self.assertFalse(self.string_utils.contains("SkyPro", "U"))
        self.assertTrue(self.string_utils.contains("hello world", " "))

    def test_contains_empty_string(self):
        self.assertFalse(self.string_utils.contains("", "a"))
        self.assertFalse(self.string_utils.contains("test", ""))

    def test_delete_symbol(self):
        self.assertEqual(self.string_utils.delete_symbol("SkyPro", "k"),
                         "SyPro")
        self.assertEqual(self.string_utils.delete_symbol("hello world", "o"),
                         "hell wrld")
        self.assertEqual(self.string_utils.delete_symbol("aaaaaa", "a"), "")
        self.assertEqual(self.string_utils.delete_symbol("test", "x"), "test")

    def test_delete_symbol_not_found(self):
        self.assertEqual(self.string_utils.delete_symbol("SkyPro", "z"),
                         "SkyPro")


if __name__ == '__main__':
    unittest.main()
