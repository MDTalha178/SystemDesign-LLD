from models.Pricing.PricingStrategy import PricingStrategy
from models.Pricing.PricingStrategyType import PricingStrategyType


class HourlyPricingStrategy(PricingStrategy):
    price_per_hour: int
    number_of_hours: int

    def __init__(self, price_per_hour, number_of_hours):
        self.price_per_hour = price_per_hour
        self.number_of_hours = number_of_hours

    def calculate_price(self):
        return self.price_per_hour * self.number_of_hours

    def get_pricing_strategy(self):
        return PricingStrategyType.HOURLY
