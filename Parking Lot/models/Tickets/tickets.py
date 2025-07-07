import uuid
from datetime import datetime
from typing import Optional, List

from Services.PricingService import PricingService
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.Payment.payment_strategy import PaymentStrategy
from models.Pricing.PricingStrategy import PricingStrategy
from models.VehcileModels.vehicleInterface import VehicleInterface


class Ticket:
    __ticket_id: uuid
    __entry_time: datetime
    __exit_time: Optional[datetime]
    __parking_slot: ParkingSlot
    __vehicle: VehicleInterface
    __pricing_strategy: PricingStrategy
    __payment_strategy: PaymentStrategy

    def __init__(
            self, entry_time: datetime,
            parking_slot: ParkingSlot,
            vehicle: VehicleInterface,
            pricing_strategy: PricingStrategy

    ):
        self.__entry_time = entry_time
        self.__exit_time = None
        self.__vehicle = vehicle
        self.__parking_slot = parking_slot
        self.__pricing_strategy = pricing_strategy
        self.__ticket_id = uuid

    def get_ticket_id(self):
        return self.__ticket_id

    def set_exit_time(self, exit_time: datetime):
        self.__exit_time = exit_time

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.__payment_strategy = payment_strategy

    def calculate_and_pay(self):
        price: int = PricingService.calculate_parking_charge(ticket=self)
        print("Amount should have to : ", price)
        self.__payment_strategy.pay(price)

    def get_entry_time(self):
        return self.__entry_time

    def get_parking_slot(self):
        return self.__parking_slot

    def get_exit_time(self):
        return self.__exit_time

    def get_pricing_strategy(self):
        return self.__pricing_strategy

    def get_payment_strategy(self):
        return self.__payment_strategy
