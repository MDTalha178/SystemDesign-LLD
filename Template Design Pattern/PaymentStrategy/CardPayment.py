import time

from Interface.PaymentStartegyInterface import PaymentStrategy
from Payment.PaymentMethod import PaymentMethod
from template.paymentRequestTemplate import PaymentRequestTemplate


class CardPayment(PaymentStrategy, PaymentRequestTemplate):

    def process_payment(self, amount:int, credential:dict):
        print("Connecting to CARD provider")
        self.connect()

    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.DEBIT_CARD

    def connect(self):
        print("Connecting to CARD please wait....")
        time.sleep(5)
        self.send_money()
        time.sleep(3)
        print("Payment Successfully")

    def validate_request(self):
        print("Validating a request in card")

    def validate_payment_method(self):
        print("Validating a payment method in Card")


    def validate_payment_route(self):
        print("Validating ap payment route in card")
