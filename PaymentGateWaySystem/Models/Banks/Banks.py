from abc import abstractmethod, ABC
from Models.PaymentMethod import PaymentMethod

class BankInterface(ABC):

    def __init__(self):
        self.bank_name = None



    @abstractmethod
    def process_payment(self, payment_mode:PaymentMethod, amount:int):
        raise NotImplemented("Sub Class should have to implements this")

class Banks:

    def __init__(self, bank:BankInterface):
        self.bank = bank

    def get_bank_name(self):
        return self.bank.bank_name

    def process_payment(self, payment_mode:PaymentMethod, amount:int):
       return self.bank.process_payment(payment_mode=payment_mode, amount=amount)
