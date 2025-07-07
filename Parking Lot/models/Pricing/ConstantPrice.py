from models.Pricing.PricingStrategy import PricingStrategy
from models.Pricing.PricingStrategyType import PricingStrategyType


class ConstantPriceStrategy(PricingStrategy):

    def __init__(self, constant_price=40):
        self.constant_price = constant_price

    def calculate_price(self):
        return self.constant_price

    def get_pricing_strategy(self):
        return PricingStrategyType.CONSTANT
