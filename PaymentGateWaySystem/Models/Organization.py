import random
import string
from typing import List

from Models.PaymentMethod import PaymentMethod


class Organization:

    def __init__(self, organization_name):
        self.org_id = ''.join(random.choices(string.ascii_letters, k=12))
        self.organization_name = organization_name
        self.supported_payment_mode:List[PaymentMethod] = []


    def get_organization_name(self):
        return self.organization_name

    def get_supported_payment_mode(self):
        return self.supported_payment_mode

    def add_payment_mode(self, payment_mode:List[PaymentMethod]):
        self.supported_payment_mode.extend(payment_mode)

    def get_org_id(self):
        return self.org_id

    def remove_payment_mode(self, paymentMode:PaymentMethod):
        self.supported_payment_mode.remove(paymentMode)
