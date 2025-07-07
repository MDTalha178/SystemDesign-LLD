from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Sub class should have to implement")

    @abstractmethod
    def undo(self):
        raise NotImplementedError("Sub class should have to implement")