from abc import ABC, abstractmethod


class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self):
        raise NotImplementedError("Sub class should have to implement this method")

    @abstractmethod
    def get_pricing_strategy(self):
        raise NotImplementedError("Sub class should have to implement this method")
