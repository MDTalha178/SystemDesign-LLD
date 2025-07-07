from Service.BidderService.BidService import BidService
from models.Auction.Auction import Auction
from models.Auction.AuctionStatus import AuctionStatus
from models.Auction.State.AuctionStateInterface import AuctionStateInterface
from models.Auction.State.ClosedAuction import ClosedAuctionState


class LiveAuctionSate(AuctionStateInterface):

    def __init__(self):
        self.bid_service = BidService()


    def participate_auction(self, user, bid_amount, auction):
        self.bid_service.create_bid(
            user, bid_amount, auction
        )

    def get_state(self) -> AuctionStatus:
        return AuctionStatus.LIVE


    def update_state(self, auction:Auction):
        auction_state = ClosedAuctionState()
        auction.update_status(
            auction_state
        )

        # call Backend server to Update
        auction.auction_Service.update_auction_status(self, auction_state)