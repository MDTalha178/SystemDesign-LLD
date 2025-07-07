import datetime
import random
import string

from Service.AuctionService.AuctionService import AuctionService
from Service.ParticipationCommissionService.ParticipantionCostService import ParticipationCostCommissionService
from models.Auction.BidLimit import BidLimit
from models.Auction.State.AuctionStateInterface import AuctionStateInterface
from models.Product.Product import Product
from models.User.User import User


class Auction:

    def __init__(
             self,
             bidLimit:BidLimit,
             seller:User,
             status:AuctionStateInterface, close_time,
             product:Product,
             participation_cost: int

    ):
        self.auctionId = random.choices(string.ascii_letters,k=7)
        self.bidLimit:BidLimit = bidLimit
        self.seller = seller
        self.status = status
        self.close_time = close_time
        self.__open_time = None
        self.product:Product = product
        self.participation_cost = participation_cost
        self.bidder = []

        # Initialize some services
        self.participation_commission_service = ParticipationCostCommissionService()
        self.auction_Service = AuctionService()


    @property
    def get_auction_id(self):
        return self.auctionId

    def get_bid_limit(self) -> BidLimit:
        return self.bidLimit

    @property
    def get_seller(self):
        return self.seller

    @property
    def get_bidder_list(self) ->list:
        return self.bidder

    @property
    def get_status(self) -> AuctionStateInterface:
        return self.status

    @property
    def get_close_time(self):
        return self.close_time

    @property
    def get_open_time(self):
        return self.__open_time

    def get_product(self):
        return self.product

    @property
    def get_participation_cost(self):
        return self.participation_cost

    def set_open_time(self):
        self.__open_time = datetime.datetime.now()

    def participate_in_bid(self, user, bid_amount):
        self.status.participate_auction(
            user, bid_amount, self
        )


    def calculate_commission(self):
        commission = self.participation_commission_service.calculate_commission(self)
        return commission


    def create_auction(self):
        self.auction_Service.create_auction(
            self
        )

    def update_auction_status(self):
        self.status.update_state(self)

    def update_status(self, state):
        self.auction_Service.update_auction_status(self, state)


    def get_details(self):
        print("AuctionId is ", self.auctionId)
        print("Auction Min limit is ", self.bidLimit.min_limit)
        print("Auction Max limit is ",  self.bidLimit.max_limit)
        print("Seller name is ", self.seller.name)
        print("product name is ", self.product.product_name)
        print("Auction status is ",  self.status.get_state().value)