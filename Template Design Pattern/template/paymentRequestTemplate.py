from abc import ABC, abstractmethod


class PaymentRequestTemplate(ABC):

    @abstractmethod
    def validate_request(self):
        raise NotImplementedError("Subclass should have to implement")

    @abstractmethod
    def validate_payment_route(self):
        raise NotImplementedError("Sub class should have to implement")

    @abstractmethod
    def validate_payment_method(self):
        raise NotImplementedError("Subclass should have to implements")

    def send_money(self):
        # step 1
        self.validate_request()

        # step 2
        self.validate_payment_route()

        #step 2
        self.validate_payment_method()