import unittest
from src.get_main_colors import rgb_tuple_to_color_hex_string, is_int


class TestGetMainColor(unittest.TestCase):
    def test_rgb_tuple_to_color_hex_string(self):
        white_rgb: tuple = (255, 255, 255)
        white_hex: str = "#ffffff"
        self.assertEqual(white_hex, rgb_tuple_to_color_hex_string(white_rgb))

        salmon_rgb: tuple = (250, 128, 114)
        salmon_hex: str = "#fa8072"
        self.assertEqual(salmon_hex, rgb_tuple_to_color_hex_string(salmon_rgb))

        indigo_rgb: tuple = (75, 0, 130)
        indigo_hex: str = "#4b0082"
        self.assertEqual(indigo_hex, rgb_tuple_to_color_hex_string(indigo_rgb))

    def test_is_int(self):
        self.assertEqual(True, is_int(45))
        self.assertEqual(True, is_int("10"))
        self.assertEqual(True, is_int("１０"))
        self.assertEqual(False, is_int(""))
        self.assertEqual(False, is_int("test"))

