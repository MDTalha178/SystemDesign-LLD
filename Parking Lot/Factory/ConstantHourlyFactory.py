from models.Pricing.ConstantPrice import ConstantPriceStrategy
from models.Tickets.tickets import Ticket


class ConstantHourlyFactory:

    @staticmethod
    def create_constant_pricing(ticket: Ticket):
        return ConstantPriceStrategy(
            constant_price=40
        )