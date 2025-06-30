import unittest

from src.card_checker.secu_social.secu_social_management import SecuSocialManagement
class TestSecuSocialManagement(unittest.TestCase):
    def setUp(self):
        self.valid_num = "142567890123457"  # Example of a valid Secu Social number
        self.invalid_num_length = "12345678901234"  # 14 digits
        self.invalid_num_characters = "12345678901234A"  # Contains a letter
        self.invalid_num_luhn = "123456789012349"  # Fails Luhn check
        self.valid_num_luhn = "370000000000010"  # Example of a valid Secu Social number with correct Luhn check

    # def test_valid_secu_social(self):
    #     secu_manager = SecuSocialManagement(self.valid_num)
    #     self.assertTrue(secu_manager.is_valid())

    def test_invalid_secu_social_length(self):
        secu_manager = SecuSocialManagement(self.invalid_num_length)
        self.assertFalse(secu_manager.is_valid())

    def test_invalid_secu_social_characters(self):
        secu_manager = SecuSocialManagement(self.invalid_num_characters)
        self.assertFalse(secu_manager.is_valid())

    def test_invalid_secu_social_luhn(self):
        secu_manager = SecuSocialManagement(self.invalid_num_luhn)
        self.assertFalse(secu_manager.luhn_check())
        
    def test_valid_first_digit(self):
        secu_manager = SecuSocialManagement(self.valid_num)
        self.assertTrue(secu_manager.isStartWithOneOrTwo())
        
    def test_valid_country_code(self):
        secu_manager = SecuSocialManagement(self.valid_num)
        self.assertTrue(secu_manager.hasCountryCode())
        
    def test_valid_secu_social_luhn(self):
        secu_manager = SecuSocialManagement(self.valid_num_luhn)
        self.assertTrue(secu_manager.luhn_check())
        
if __name__ == '__main__':
    unittest.main()