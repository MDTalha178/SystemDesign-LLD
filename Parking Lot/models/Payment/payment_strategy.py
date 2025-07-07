from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: int):
        raise NotImplementedError("Subclass should have to implement this")
