from abc import ABC, abstractmethod
class Visa(ABC):

    @abstractmethod
    def connectToVisa(self):
        pass