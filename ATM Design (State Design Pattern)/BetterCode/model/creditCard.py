from abc import ABC, abstractmethod
class CreditCard(ABC):

    @abstractmethod
    def makePinPayment(self):
        pass