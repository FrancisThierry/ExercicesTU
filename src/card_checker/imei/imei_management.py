from card_checker.base_card_checker import BaseCardChecker


class Imei_Management(BaseCardChecker):
    def __init__(self, imei):
        self.imei = imei
    def check_length(self):
        """Check if the IMEI number has the correct length."""
        return len(self.imei) != 15

    def is_valid(self):
        """Check if the IMEI number is valid."""
        if len(self.imei) != 15 or not self.imei.isdigit():
            return False
        return self.luhn_check()

    def luhn_check(self):
        """Perform Luhn check on the IMEI number."""
        total = 0
        reverse_digits = self.imei[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:  # Double every second digit
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0