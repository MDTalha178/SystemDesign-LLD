import datetime
from models.Auction.BidLimit import BidLimit
from models.Bids.Bid import Bid
from models.Product.Product import Product
from models.User.User import User
from models.User.UserEnum import UserEnum
from models.User.UserType import UserType

user_memory = {}
auction_memory = {}
bid_memory = {}


def create_user(**kwargs):
    command_type = kwargs.get('command')
    user_fields = ['user_name', 'name']

    data = {}

    for fields in user_fields:
        user_input = input(f"Please enter your {fields}: ")
        data.update({fields: user_input})
    if command_type == 'ADD_BUYER':
        user_type =UserType(UserEnum.BUYER)
    else:
        user_type = UserType(UserEnum.SELLER)
    user_obj = User(data.get('user_name'), data.get('name'), user_type)
    user_memory.update({user_obj.user_id: user_obj})
    print("User Created!")

def get_user():
    for user in user_memory.values():
        user.get_details()

def create_product():
    product_obj = Product('Scorpio', 1209999)
    return product_obj

def create_auction(**kwargs):
    seller = kwargs.get('seller_id')
    auction_fields = ['mid_bid_limit', 'max_bid_limit', 'close_time', 'participation_cost']
    data = {}
    for fields in auction_fields:
        user_input = input(f"Please enter your {fields}: ")
        data.update({fields: user_input})

    auction_limit = BidLimit(int(data.get('mid_bid_limit')), int(data.get('max_bid_limit')))
    from models.Auction.State.LiveAuctionState import LiveAuctionSate
    auction_status = LiveAuctionSate()
    product = create_product()
    from models.Auction.Auction import Auction
    auction_obj = Auction(
        auction_limit,
        user_memory.get(seller),
        auction_status,
        datetime.datetime.now(),
        product,
        120

    )
    auction_memory.update({auction_obj.auctionId: auction_obj})

def get_auction_list():
    for auction in auction_memory.values():
        auction.get_details()

def retrieve_auction(auction_id):
    from models.Auction.Auction import Auction
    auction_obj:Auction = auction_memory.get(auction_id, None)

    if auction_obj is None:
        print("Invalid auctionID")
    auction_obj.get_details()


def create_bid(**kwargs):
    if not bid_memory :
        bid_obj = Bid()
        bid_memory.update({'bid_obj': bid_obj})
    else:
         bid_obj = bid_memory.get('bid_obj')
    auction_obj = auction_memory.get(kwargs.get('auctionId'))
    bid_obj.create_bid(
        kwargs.get('bid_amount'),
        auction_obj,
        kwargs.get('buyer')
    )

def retrieve_bid(**kwargs):
    pass

COMMAND = {
    "ADD_BUYER":create_user,
    "ADD_SELLER": create_user,
    "CREATE_AUCTION": create_auction,
    "GET_AUCTION": get_auction_list,
    "RETRIEVE_AUCTION": retrieve_auction,
    "GET_USER": get_user,
    "CREATE_BID": create_bid,
    "RETRIEVE_BID": retrieve_bid
}

print("These Are the following command we support!")
for key in COMMAND.keys():
    print(key)

while True:
    command = input("Please choose the command:  ")

    res = COMMAND.get(command)

    if command  == 'stop':
        break

    elif command in ["ADD_BUYER", "ADD_SELLER"]:
        res(command=command)

    elif command in ["CREATE_AUCTION"]:
        seller_id =  input("Please enter seller id:  ")
        res(command=command, seller_id=seller_id)

    elif command == 'GET_AUCTION':
        get_auction_list()

    elif command == 'RETRIEVE_AUCTION':
        auction_id = input("Please enter auction id:  ")
        retrieve_auction(auction_id)

    elif command == 'GET_USER':
        get_user()

    elif command == 'CREATE_BID':
        fields = ['auctionId' ,'bid_amount', 'buyer']
        data = {}
        for field in fields:
            userInput =  input(f"Please enter the {fields}")
            data.update({field:userInput})
        res(**data)
