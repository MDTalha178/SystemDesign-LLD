from models.ParkingSlotModel.VechileSlotInterface import CarSlotInterface
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.ParkingSlotModel.parking_floor import ParkingFloor
from models.VehcileModels.vehicle_type import VehicleType


class CarParkingSlot(ParkingSlot, CarSlotInterface):

    def __init__(self, slot_number: str, parking_floor: ParkingFloor):
        super().__init__(
            slot_number,
            [VehicleType.CAR, VehicleType.BIKE],
            parking_floor,
        )
