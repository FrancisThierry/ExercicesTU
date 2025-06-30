from src.card_checker.base_card_checker import BaseCardChecker


class SecuSocialManagement(BaseCardChecker):
    def __init__(self, numSecu):
        self.ns = numSecu
        
    def check_length(self):
        """Check if the Secu Social number has the correct length."""
        return len(self.ns) != 15
        
    def isStartWithOneOrTwo(self):
        """
        Check if the Secu Social number starts with '1' or '2'.
        This is a basic validation for the first digit.
        """
        if len(self.ns) < 1:
            return False
        return self.ns[0] in ('1', '2')
    def hasCountryCode(self):
        """
        Check if the Secu Social number has a valid country code.
        The first two digits should be '01' to '99'.
        """
        if len(self.ns) < 2:
            return False
        return self.ns[:2].isdigit() and 1 <= int(self.ns[:2]) <= 99
    
    def is_valid(self):
        """Check if the Secu Social number is valid."""
        # start by 1 or 2
        if not self.isStartWithOneOrTwo():
            return False
        # check country code
        if not self.hasCountryCode():
            return False
        if len(self.ns) != 15 or not self.ns[:-2].isdigit():
            return False
        cle = self.get_cle()
        if cle is None:
            return False
        return self.ns[-2:] == cle
    def luhn_check(self):
        # Convertir la chaîne en liste d'entiers
        digits = [int(d) for d in self.ns]
        
        # print(f"Digits for Luhn check: {digits}")

        # Inverser la liste pour parcourir les chiffres de droite à gauche
        # L'algorithme de Luhn double un chiffre sur deux en commençant par le deuxième en partant de la droite.
        digits.reverse() 
        
        # print(f"Digits for Luhn check: {digits}")
        

        total = 0
        for i, digit in enumerate(digits):
            if i % 2 == 1:  # Index impair = 2ème, 4ème, etc. chiffre en partant de la droite (après inversion)
                doubled_digit = digit * 2
                if doubled_digit > 9:
                    total += (doubled_digit - 9) # Équivalent à additionner les chiffres (ex: 12 -> 1+2=3, ou 12-9=3)
                else:
                    total += doubled_digit
            else: # Index pair = 1er, 3ème, etc. chiffre en partant de la droite (après inversion)
                total += digit
        # print(f"Total after Luhn check: {total}")p
        
        # Le numéro est valide selon Luhn si la somme totale est un multiple de 10
        return total % 10 == 0
    def get_num_sans_cle(self):
        """
        Retourne le numéro de sécurité sociale sans la clé de contrôle.
        Si le numéro n'est pas valide, retourne None.
        """
        if len(self.ns) != 15 or not self.ns[:-2].isdigit():
            return None
        return self.ns[:-2]
    
    
    def get_cle(self):
        """
        Calcule la clé de contrôle du numéro de sécurité sociale français.
        La clé est composée des deux derniers chiffres du résultat : 97 - (numéro sans clé % 97)
        """
        if len(self.ns) != 15 or not self.ns[:-2].isdigit():
            return None
        num_sans_cle = self.ns[:-2]
        try:
            cle_calculee = 97 - (int(num_sans_cle) % 97)
            return f"{cle_calculee:02d}"
        except ValueError:
            return None

    