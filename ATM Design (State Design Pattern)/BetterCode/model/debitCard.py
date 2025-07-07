from abc import ABC, abstractmethod
class DebitCard(ABC):

    @abstractmethod
    def makePinPayment(self):
        pass