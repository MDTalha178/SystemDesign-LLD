from models.Pricing.HourlyPricingStrategy import HourlyPricingStrategy
from models.Tickets.tickets import Ticket


class PricingStrategyFactory:

    @staticmethod
    def create_hourly_pricing_strategy(ticket: Ticket):
        return HourlyPricingStrategy(
            price_per_hour=40,
            number_of_hours= ticket.get_exit_time() - ticket.get_entry_time()

        )
