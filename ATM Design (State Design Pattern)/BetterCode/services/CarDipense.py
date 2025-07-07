from services.CardDispenseInterface import CardDespenseInterface
from API.backendAPI import BackendServer
from DTO.CashDispenserDTO import CashDispenserDTO
from model.atm import ATM


class CardDispense(CardDespenseInterface):
    def __init__(self):
        self.backend_server = BackendServer()

    def despense_cash(self, atm: 'ATM', amount: int, transaction_id: int):
        avilable_amount = self.backend_server.get_atm_amount(CashDispenserDTO(atm))

        if amount > avilable_amount:
            raise ValueError("ATM does not have enough cash to dispense")
        print("Dispensing cash: ", amount)
