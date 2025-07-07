from abc import ABC, abstractmethod
class Master(ABC):

    @abstractmethod
    def connectTomaster(self):
        pass