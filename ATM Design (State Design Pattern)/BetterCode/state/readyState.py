from state.state import State
from ATMState.atmState import ATMState
from state.ReadCardDetailsAndPIn import ReadCardDetailsAndPinState
from model.atm import ATM
from model.card import Card
import random


class ReadyState(State):
    atm = None
    backend_server = None

    def __init__(self, atm: "ATM"):
        self.atm = atm
        from API.backendAPI import BackendServer
        self.backend_server = BackendServer

    def init_transaction(self):
        transaction_id = self.backend_server.create_transaction(self.atm.atm_id)

        # Update the state
        self.atm.update_status(ReadCardDetailsAndPinState(self.atm))
        return transaction_id

    def read_card_details_and_pin(self):
        raise ValueError("Can't read a card without inserting them..")

    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        raise ValueError("Can't depense a without inserting them..")

    def eject_card(self) -> None:
        raise ValueError("Can't eject a card without inserting themt..")

    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        raise ValueError("Can't widthraw a cash  without inserting them..")

    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        raise ValueError("Can't cancel a transaction without inserting them..")

    def get_state(self) -> "ATMState":
        return ATMState.READY_FOR_TRANSACTION
