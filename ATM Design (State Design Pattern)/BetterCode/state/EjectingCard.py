from state.state import State
from ATMState.atmState import ATMState
from state.readyState import ReadyState
from model.atm import ATM
from model.card import Card


class EjectingCardState(State):
    atm = None

    def __init__(self, atm: "ATM"):
        self.atm = atm

    def init_transaction(self):
        raise ValueError("Can't start a Transaction  while Ejecting a card")

    def read_card_details_and_pin(self):
        raise ValueError("Can't read a card without inserting them..")

    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        raise ValueError("Can't dispense a cash  without inserting them..")

    def eject_card(self) -> None:
        self.atm.update_status(ReadyState(self.atm))
        return True

    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        raise ValueError("Can't widthraw a cash  without inserting them..")

    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        raise ValueError("Can't cancel a transaction without inserting them..")

    def get_state(self) -> "ATMState":
        return ATMState.EJECTING_CARD
