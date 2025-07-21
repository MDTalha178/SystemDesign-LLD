from abc import ABC, abstractmethod


class RoomElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError("Sub class should have to implement this")

