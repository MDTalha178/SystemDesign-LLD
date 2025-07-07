from state.state import State
from ATMState.atmState import ATMState
from model.card import Card
from model.atm import ATM
from state.readyState import ReadyState
from factory.cardmangerfactories import CardManagerFactory

from state.DispenseCash import DispenseCash


class CashWidthrawDetails(State):
    def __init__(self, atm: "ATM"):
        self.atm = atm

    def init_transaction(self):
        raise ValueError("Can't initiate transaction a while reading a card..")

    def read_card_details_and_pin(self):
        raise ValueError("Can't read a card details while verifyng your card details.")

    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        raise ValueError("Can't depense a without reading a card details..")

    def eject_card(self) -> None:
        raise ValueError("Can't eject a card without reading a card details and PIN..")

    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        card_manager = CardManagerFactory().get_card_manager(card.get_card_type)
        is_valid_widthraw = card_manager.validate_widthrwal(transaction_id, amount)

        if is_valid_widthraw:
            self.atm.update_status(DispenseCash(self.atm))
        else:
            self.atm.update_status(ReadyState(self.atm))

    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        self.atm.update_status(ReadyState(self.atm))
        return True

    def get_state(self) -> "ATMState":
        return ATMState.READING_CASH_WITHDRAW_DETAILS
