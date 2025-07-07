from abc import ABC, abstractmethod

from models.Auction.Auction import Auction
from models.Auction.AuctionStatus import AuctionStatus


class AuctionStateInterface(ABC):

    @abstractmethod
    def participate_auction(self, user, bid_amount, auction:Auction):
        raise NotImplemented("Sub class should have to implements")


    @abstractmethod
    def get_state(self) -> AuctionStatus:
        raise NotImplemented("Sub class should have to implements")

    @abstractmethod
    def update_state(self, auction:Auction) -> AuctionStatus:
        raise NotImplemented("Sub class should have to implements")
