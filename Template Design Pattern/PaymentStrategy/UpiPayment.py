import time

from Interface.PaymentStartegyInterface import PaymentStrategy
from Payment.PaymentMethod import PaymentMethod
from template.paymentRequestTemplate import PaymentRequestTemplate


class UPIPayment(PaymentStrategy, PaymentRequestTemplate):

    def process_payment(self, amount:int, credential:dict):
        print("Processing Payment via UPI")
        self.connect()

    def get_payment_method(self) -> PaymentMethod:
        return PaymentMethod.UPI

    def connect(self):
        print("Connecting to UPI please wait....")
        time.sleep(3)
        self.send_money()
        time.sleep(5)
        print("Payment Successfully")

    def validate_request(self):
        print("Validating a request in UPI")

    def validate_payment_method(self):
        print("Validating a payment method in UPI")

    def validate_payment_route(self):
        print("Validating ap payment route in UPI")