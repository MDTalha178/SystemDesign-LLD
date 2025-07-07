from abc import ABC, abstractmethod

class EmailInterface(ABC):

    @abstractmethod
    def clone(self):
        pass