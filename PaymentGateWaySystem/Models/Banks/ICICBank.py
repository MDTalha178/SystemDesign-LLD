import random

from Models.Banks.Banks import Banks, BankInterface
from Models.Banks.SupportedBank import SupportedBank
from Models.PaymentMethod import PaymentMethod
from Models.PaymentStatus import PaymentStatus


class ICICBank(BankInterface, Banks):

    def __init__(self):
        self.bank_name = SupportedBank.ICICI
        super().__init__(self)

    def process_payment(self, payment_mode: PaymentMethod, amount):
        payment_status: PaymentStatus = random.choices([
            PaymentStatus.PROCESSING,
            PaymentStatus.FAILED,
            PaymentStatus.PENDING,
            PaymentStatus.SUCCESSFUL
        ])

        return payment_status.value