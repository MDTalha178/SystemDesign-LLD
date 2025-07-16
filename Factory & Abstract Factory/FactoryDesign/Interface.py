from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def get_user_details(self):
        raise NotImplemented("Sub class should have to implement this")

    @abstractmethod
    def get_user_type(self):
        raise NotImplemented("Sub class should have to implement this")
