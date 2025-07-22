from abc import ABC, abstractmethod

from Payment.PaymentMethod import PaymentMethod


class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, amount:int, credential:dict):
        raise NotImplementedError("Sub class should have to implements")


    @abstractmethod
    def get_payment_method(self) -> PaymentMethod:
        raise NotImplementedError("Sub class should have to implements")

    @abstractmethod
    def connect(self):
        raise NotImplementedError("Sub class should have to implements")