import random
from typing import List

from Models.Banks.Banks import BankInterface
from Models.Banks.SupportedBank import SupportedBank
from Models.PaymentMethod import PaymentMethod
from Models.PaymentStatus import PaymentStatus


class HDFCBank(BankInterface):
    def __init__(self):
        super().__init__()
        self.bank_name = SupportedBank.HDFC.value

    def process_payment(self, payment_mode: PaymentMethod, amount):
        payment_status: List[PaymentStatus] = random.choices([
            PaymentStatus.PROCESSING,
            PaymentStatus.FAILED,
            PaymentStatus.PENDING,
            PaymentStatus.SUCCESSFUL
        ])
        print(payment_status[0], "Clled")
        return payment_status[0]
