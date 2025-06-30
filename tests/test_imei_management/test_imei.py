import unittest

from src.card_checker.imei.imei_management import Imei_Management
    
class TestImeiManagement(unittest.TestCase):
    def setUp(self):
        self.valid_imei = "490154203237518"
        self.invalid_imei_length = "49015420323751"  # 14 digits
        self.invalid_imei_characters = "49015420323751A"  # Contains a letter
        self.invalid_imei_luhn = "490154203237519"  # Fails Luhn check

    def test_valid_imei(self):
        imei_manager = Imei_Management(self.valid_imei)
        self.assertTrue(imei_manager.is_valid())

    def test_invalid_imei_length(self):
        imei_manager = Imei_Management(self.invalid_imei_length)
        self.assertFalse(imei_manager.is_valid())

    def test_invalid_imei_characters(self):
        imei_manager = Imei_Management(self.invalid_imei_characters)
        self.assertFalse(imei_manager.is_valid())

    def test_invalid_imei_luhn(self):
        imei_manager = Imei_Management(self.invalid_imei_luhn)
        self.assertFalse(imei_manager.is_valid())
        
if __name__ == '__main__':
    unittest.main()