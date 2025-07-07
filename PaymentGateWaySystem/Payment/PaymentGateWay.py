from typing import Dict

from Models.Banks.Banks import BankInterface
from Models.Client import Client
from Models.PaymentMethod import PaymentMethod
from Models.PaymentStatus import PaymentStatus
from Payment.PaymentProcessor import PaymentProcessor
from Routing.Routing import Routing


class PaymentGateWay:

    def __init__(
            self
    ):
        self.clients: Dict[str, Client] = {}
        self.router = Routing()
        self.payment_processor =PaymentProcessor()

    def add_client(self, name):
        client:Client = Client(name)
        self.clients[client.get_client_id()] = client
        print("Client Added Successfully!")

    def remove_client(self, clientID):
        if self.clients.get(clientID):
            self.clients.pop(clientID)
            print("Client Remove Successfully!")
            return
        print("Invalid Client ID")

    def add_payment_method(self, clientID, paymentMode:PaymentMethod):
        if self.clients.get(clientID):
            client:Client = self.clients.get(clientID)
            if paymentMode in client.get_supported_payment_mode():
                print("Payment Mode Already Added")
                return
            client.add_payment_mode(payment_mode=[paymentMode])
            print("Payment Added Successfully")
            return
        print("Invalid Client ID")

    def get_supported_payment_mode(self, clientID):
        if self.clients.get(clientID):
            supported_payment  = self.clients.get(clientID).get_supported_payment_mode()
            if supported_payment:
                return supported_payment
            print("No Payment Method Added")
        print("Invalid Client ID")

    def remove_payment_method(self, clientId, paymentMode):
        if self.clients.get(clientId):
            client: Client = self.clients.get(clientId)
            if paymentMode in client.get_supported_payment_mode():
                print("Remove payment Method Successfully!")
                client.remove_payment_mode(paymentMode)
                return
            print("Invalid Payment Mode")
            return
        print("Invalid Client Id")

    def make_payment(self, paymentMode:PaymentMethod, amount, client_id, banks, payment_credential:Dict):

        client = self.clients.get(client_id)
        if client is None:
            print("Invalid Client")
            return

        # Validated payment Mode for Client
        try:
            self.payment_processor.validate_payment_method(
                client, paymentMode
            )
        except ValueError as v:
            print("Unsupported Payment mode: ", v)
            return

        try:
            self.payment_processor.validate_instrument(
                paymentMode,
                payment_credential
            )
        except ValueError as v:
            print("Invalid Instrument Details! ", v)
            return

        status:PaymentStatus = self.payment_processor.process_payment(
            bank=banks,
            payMode=paymentMode,
            amount=amount
        )
        if status == PaymentStatus.SUCCESSFUL:
            print(f"Payment Successful via {banks.get_bank_name()} for an amount is : {amount}")
            return
        print(f"Payment is {status.value} via {banks.get_bank_name()} for an amount is: {amount}")

