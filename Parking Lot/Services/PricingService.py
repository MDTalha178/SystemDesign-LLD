from Factory.ConstantHourlyFactory import ConstantHourlyFactory
from Factory.pricing_factory import PricingStrategyFactory
from models.Pricing.PricingStrategyType import PricingStrategyType
from models.Tickets.tickets import Ticket


class PricingService:

    @staticmethod
    def calculate_parking_charge(ticket: Ticket) -> int:
        price = None
        if ticket.get_pricing_strategy() == PricingStrategyType.HOURLY:
            strategy = PricingStrategyFactory.create_hourly_pricing_strategy(ticket)
            price = strategy.calculate_price()
        if ticket.get_pricing_strategy() == PricingStrategyType.CONSTANT:
            strategy = ConstantHourlyFactory.create_constant_pricing(ticket)
            price = strategy.constant_price()
        return price
