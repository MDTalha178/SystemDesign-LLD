from abc import ABC, abstractmethod


class UserIteratorInterface(ABC):

    @abstractmethod
    def has_next(self):
        raise NotImplementedError("Sub class should have to implement this method")

    @abstractmethod
    def __iter__(self):
        raise  NotImplementedError("Sub class should have to implement this method")

    @abstractmethod
    def next(self):
        raise NotImplementedError("Sub class should have to implement this method")