from Service.BidderService.BidService import BidService
from models.Auction.Auction import Auction
from models.Auction.AuctionStatus import AuctionStatus
from models.Auction.State.AuctionStateInterface import AuctionStateInterface


class ClosedAuctionState(AuctionStateInterface):

    def __init__(self):

        self.bid_service = BidService()


    def participate_auction(self, user, bid_amount, auction:Auction):
        raise ValueError("You can't participate in closed Auction")


    def get_state(self) -> AuctionStatus:
        return AuctionStatus.CLOSED


    def update_state(self, auction:Auction) -> AuctionStatus:
        raise ValueError("Closed Auction can't modify")
