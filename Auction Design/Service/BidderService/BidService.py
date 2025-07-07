from models.Auction.Auction import Auction
from models.Bids.Bid import Bid
from models.Bids.Bidder import Bidder


class BidService:
    def __init__(self):
        self.in_memory: {str:Bidder}= {}

    def create_bid(self, user, bid_amount, auction:Auction):
        if auction.get_bid_limit().max_limit >= bid_amount >= auction.bidLimit.min_limit:

            user_obj:Bidder = self.in_memory.get(user.user_id,None)
            if user_obj:
                user_obj.update_auction_list(
                    auction
                )
            else:
                bidder = Bidder(user)
                bidder.update_auction_list(auction)
                self.in_memory.update({user.user_id: bidder})
        print(
            f"Bid Amount is should be in range min amount {auction.get_bid_limit().min_limit} and max amount is {auction.get_bid_limit().min_limit}")


    def update_bid(self, auction_id, amount):
        bid:Bid = self.in_memory.get(auction_id, None)
        if bid is None:
            print("Auction id is invalid")
        bid.bid_amount = amount
        self.in_memory.update({auction_id: bid})

    def withdraw_bid(self, user_id, auction_id):
        bidder: Bidder = self.in_memory.get(user_id, None)
        if bidder is None:
            print("Auction id is invalid")
        bidder.update_status(auction_id)