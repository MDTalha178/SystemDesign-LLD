from models.Auction.Auction import Auction
from models.Bids.BidStatus import BidStatus
from models.User.User import User


class Bidder:
    def __init__(
            self,
            buyer:User,

    ):
        self.buyer:User = buyer
        self.is_preferred_bidder = False
        self.auction_list:list[{}] = [{str:Auction}]


    def update_auction_list(self, auction:Auction):
        self.auction_list.append({auction.auctionId:auction, 'status':BidStatus.PARTICIPATED})

        #update preferred buyer
        self.is_preferred_bidder = len(self.auction_list) >= 2


    def update_status(self, auctionID):
        for auction in self.auction_list:
            if auctionID == auction.auctionId:
                auction.status = BidStatus.WITHDRAW