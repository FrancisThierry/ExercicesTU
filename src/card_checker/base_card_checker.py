from importlib import abc


class BaseCardChecker(abc.ABC):
    """
    Base class for card checkers.
    This class provides a common interface for all card checkers.
    """

    def __init__(self, card_number: str):
        self.card_number = card_number

    def is_valid(self) -> bool:
        """
        Check if the card number is valid.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    def luhn_check(self) -> bool:
        """        Perform Luhn check on the card number.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    def check_length(self) -> bool:
        """
        Check if the card number has the correct length.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")