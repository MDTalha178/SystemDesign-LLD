import random
import string
from typing import List
from Models.PaymentMethod import PaymentMethod


class Client:

    def __init__(self, name):
        self.org_id = ''.join(random.choices(string.ascii_letters, k=12))
        self.name = name
        self.__supported_payment_mode: List[PaymentMethod] = []

    def get_client_name(self):
        return self.name

    def get_supported_payment_mode(self) ->List:
        return self.__supported_payment_mode

    def add_payment_mode(self, payment_mode: List[PaymentMethod]):
        self.__supported_payment_mode.extend(payment_mode)

    def get_client_id(self):
        return self.org_id

    def remove_payment_mode(self, paymentMode: PaymentMethod):
        self.__supported_payment_mode.remove(paymentMode)