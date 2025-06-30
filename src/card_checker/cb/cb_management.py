from card_checker.base_card_checker import BaseCardChecker


class CbManagement(BaseCardChecker):
    def __init__(self, cbNumber):
        self.cbNum = cbNumber
        
    def check_length(self):
        return len(self.cbNum) != 15

    def is_valid(self):
        """Check if the CB number is valid."""
        if self.check_length or not self.cbNum.isdigit():
            return False
        return self.luhn_check()    
    def luhn_check(self):
        """Perform Luhn check on the CB number."""
        total = 0
        reverse_digits = self.cbNum[:-1][::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n      
        return (total + int(self.cbNum[-1])) % 10 == 0            