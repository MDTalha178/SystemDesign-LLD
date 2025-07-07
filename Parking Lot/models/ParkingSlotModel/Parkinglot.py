from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.ParkingSlotModel.parking_floor import ParkingFloor
from models.Pricing import PricingStrategy
from models.Tickets.tickets import Ticket


class Parkinglot:
    parking_floor: list[ParkingFloor]
    pricing_strategies: PricingStrategy
    parking_slot_in_memory = dict[str, ParkingSlot]
    ticket_in_memory = dict[str, Ticket]

    def __init__(self, parking_floor: list[ParkingFloor], pricing_strategies: PricingStrategy):
        self.parking_floor = parking_floor
        self.pricing_strategies = pricing_strategies

    def get_parking_floor(self):
        return self.parking_floor

    def get_pricing_strategies(self):
        return self.pricing_strategies

    def add_parking_floor(self, parking_floor: ParkingFloor):
        self.parking_floor.append(parking_floor)

    def remove_parking_floor(self, parking_floor: ParkingFloor):
        self.parking_floor.remove(parking_floor)

    def add_pricing_strategies(self, pricing_strategies: PricingStrategy):
        self.pricing_strategies.append(pricing_strategies)

    def remove_pricing_strategies(self, pricing_strategies: PricingStrategy):
        self.pricing_strategies.remove(pricing_strategies)
