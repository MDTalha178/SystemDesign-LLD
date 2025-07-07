from models.ParkingSlotModel.CarParkingSlot import CarParkingSlot
from models.ParkingSlotModel.VechileSlotInterface import ElectricVehicleCarSlot, CarSlotInterface
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.ParkingSlotModel.parking_floor import ParkingFloor
from models.VehcileModels.vehicle_type import VehicleType


class ElectricCarSlot(ParkingSlot, ElectricVehicleCarSlot, CarSlotInterface):
    def __init__(self, slot_number: str, parking_floor: ParkingFloor):
        super().__init__(
            slot_number,
            [VehicleType.ELECTRIC_CAR, VehicleType.ELECTRIC_BIKE],
            parking_floor
        )

    def charge_vehicle(self):
        pass
