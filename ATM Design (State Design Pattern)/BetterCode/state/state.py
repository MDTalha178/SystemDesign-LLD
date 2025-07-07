from abc import ABC, abstractmethod
from model.card import Card
from ATMState.atmState import ATMState


class State(ABC):

    @abstractmethod
    def init_transaction(self) -> int:
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def read_card_details_and_pin(self, card: "Card", pin: str) -> bool:
        """Returns True if the card is valid, False otherwise."""
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def eject_card(self) -> None:
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        NotImplemented("Subclasses must implement this method")

    @abstractmethod
    def get_state(self) -> "ATMState":
        NotImplemented("Subclasses must implement this method")
