from  enum import  Enum

class AuctionStatus(Enum):
    UPCOMING = "Upcoming"
    LIVE = "Live"
    RESUME = "Resume"
    CLOSED = "Closed"