class BidLimit:

    def __init__(self, min_limit:int, max_limit:int):
        self.min_limit = min_limit
        self.max_limit = max_limit


    def get_min_limit(self):
        return self.min_limit

    def get_max_limit(self):
        return self.max_limit