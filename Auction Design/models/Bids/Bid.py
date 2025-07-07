from Service.BidderService.BidService import BidService
from models.Auction.Auction import Auction
from models.User.User import User

class Bid:
    def __init__(
            self,
    ):
        self.bid_Service = BidService()

    def create_bid(self, bid_amount, auction:Auction, buyer:User):
        self.bid_Service.create_bid(
            buyer, bid_amount, auction
        )

    def update_bid(self, bid_amount, auction:Auction):
        self.bid_Service.update_bid(
            auction.auctionId, bid_amount
        )

    def withdraw_bid_status(self, user_id, auction):
        self.bid_Service.withdraw_bid(user_id, auction.auctionId)
