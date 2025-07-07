from abc import ABC, abstractmethod

from Models.Banks.Banks import BanksInterface


class RoutingInterface(ABC):

    @abstractmethod
    def add_routing(self, bank:BanksInterface):
        raise NotImplemented("Sub Class should have to implements")

    @abstractmethod
    def route_payment(self):
        raise NotImplemented("Sub Class should have to implements")