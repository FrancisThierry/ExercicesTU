import unittest
from src.card_checker.cb.cb_management import CbManagement
class TestCbManagement(unittest.TestCase):
    def setUp(self):
        self.valid_cb = "123456789012345"  # 15 digits
        self.invalid_cb_length = "123456789012345"  # 15 digits
        self.invalid_cb_characters = "123456789012345A"  # Contains a letter
        self.invalid_cb_luhn = "1234567890123457"  # Fails Luhn check

    def test_valid_cb(self):
        cb_manager = CbManagement(self.valid_cb)
        self.assertTrue(cb_manager.is_valid())

    def test_invalid_cb_length(self):
        cb_manager = CbManagement(self.invalid_cb_length)
        self.assertFalse(cb_manager.is_valid())

    def test_invalid_cb_characters(self):
        cb_manager = CbManagement(self.invalid_cb_characters)
        self.assertFalse(cb_manager.is_valid())

    def test_invalid_cb_luhn(self):
        cb_manager = CbManagement(self.invalid_cb_luhn)
        self.assertFalse(cb_manager.is_valid())