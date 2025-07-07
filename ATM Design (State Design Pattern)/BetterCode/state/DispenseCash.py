from state.state import State
from model.card import Card
from ATMState.atmState import ATMState
from factory.cardmangerfactories import CardManagerFactory
from state.readyState import ReadyState
from services.CarDipense import CardDispense
from model.atm import ATM

from state.EjectingCard import EjectingCardState


class DispenseCash(State):
    __dispense_cash = None

    def __init(self, atm: "ATM"):
        self.atm = atm
        self.__dispense_cash = CardDispense()

    def init_transaction(self):
        raise ValueError("Can't start a Transaction  while despensing  a cash")

    def read_card_details_and_pin(self, card: "Card", pin: int):
        raise ValueError("Can't read a card details while despensing  a cash")

    def dispense_cash(self, card: "Card", amount: int, transaction_id: int) -> int:
        """Returns the amount dispensed."""
        card_manager = CardManagerFactory().get_card_manager(card.get_card_type)
        is_transaction_successful = card_manager.dotTransaction(card, amount, transaction_id)

        if is_transaction_successful:
            self.__dispense_cash.despense_cash(self.atm, amount, transaction_id)
            self.atm.update_status(EjectingCardState(self.atm))
            return amount

        self.atm.update_status(ReadyState(self.atm))

    def eject_card(self) -> None:
        raise ValueError("Can't Eject a card  while despensing a cash")

    def read_cash_withdraw_details(self, card: "Card", transaction_id: int, amount: int) -> bool:
        """Returns True if cash withdrawal details are valid, False otherwise."""
        raise ValueError("Can't widthraw a cash  while Disepensing a cash")

    def cancel_transaction(self, transaction_id: int) -> bool:
        """Returns True if the transaction is canceled, False otherwise."""
        raise ValueError("Can't cancel a transaction while Disepensing a cash")
        return False

    def get_state(self) -> "ATMState":
        return ATMState.DISPENSING_CASH
