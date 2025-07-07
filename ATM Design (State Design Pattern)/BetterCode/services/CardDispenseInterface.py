from abc import ABC, abstractmethod
from model.atm import ATM

class CardDespenseInterface(ABC):

    @abstractmethod
    def despense_cash(self, atm:'ATM', amount:int, transaction_id:int):
        raise NotImplementedError('Sub Class Should be impelent this method')