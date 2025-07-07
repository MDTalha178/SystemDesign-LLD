from abc import ABC, abstractmethod


class PriceStrategy(ABC):

    @abstractmethod
    def compare(self, product_price: int, filter_price: int):
        raise NotImplementedError("Subclass should have to implement")
