from state.state import State
from ATMState.atmState import ATMState
from model.card import Card
from factory.cardmangerfactories import CardManagerFactory
from API.backendAPI import BackendServer
from model.atm import ATM
from state.ReadingCashWidthrawDetails import CashWidthrawDetails

from state.readyState import ReadyState


class ReadCardDetailsAndPinState(State):
    def __init(self, atm: "ATM"):
        self.atm = atm
        self.backend_server = BackendServer

    def init_transaction(self):
        raise ValueError("Transaction already created!")

    def read_card_details_and_pin(self, card: "Card", pin: int):

        card_manager = CardManagerFactory().get_card_manager(card.get_card_type)

        # validate Card details
        is_valid_card = card_manager.validateCard(card, pin)
        if is_valid_card:
            self.atm.update_status(CashWidthrawDetails(self.atm))
        else:
            self.atm.update_status(ReadyState(self.atm))

    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        raise ValueError("Can't despense a cash  while reading card and verifying PIN.")

    def eject_card(self) -> None:
        raise ValueError("Can't Eject a card  while reading card and verifying PIN.")

    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        raise ValueError("Can't widthraw a cash  while reading card and verifying PIN.")

    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        self.atm.update_status(ReadyState(self.atm))
        return True

    def get_state(self) -> "ATMState":
        return ATMState.READ_CARD_DETAILS_AND_PIN
