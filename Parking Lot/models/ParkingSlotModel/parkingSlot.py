from typing import Optional
from functools import reduce
from models.ParkingSlotModel.park import Park
from models.ParkingSlotModel.parking_floor import ParkingFloor
from models.ParkingSlotModel.parking_status import ParkingStatus
from models.VehcileModels.Vehcile import Vehicle
from models.VehcileModels.vehicle_type import VehicleType


class ParkingSlot:
    slot_number: str = None
    parking_status: ParkingStatus
    vehicle: Optional[Vehicle]
    parking_floor: ParkingFloor
    supported_vehicle_type: Optional[list[VehicleType]]
    park: Park

    def __init__(self, slot_number: str, supported_vehicle_type: list, parking_floor: ParkingFloor):
        self.slot_number = slot_number
        self.supported_vehicle_type = supported_vehicle_type
        self.parking_status = ParkingStatus.EMPTY
        self.parking_floor = parking_floor
        self.parking_floor.add_parking_slot(self)

    def get_slot_number(self) -> str:
        return self.slot_number

    def get_parking_status(self) -> ParkingStatus:
        return self.parking_status.value

    def get_vehicle(self) -> Vehicle:
        return self.vehicle

    def get_supported_vehicle_type(self):
        return self.supported_vehicle_type

    def set_vehicle(self, vehicle: Vehicle):

        try:
            if self.supported_vehicle_type in vehicle.vehicle_type:
                self.vehicle = vehicle
                self.parking_status = self.parking_status.FULL
        except Exception as e:
            raise Exception('Parking Slot is Full')

    def remove_vehicle(self):
        self.parking_status = self.parking_status.EMPTY
        self.vehicle = None

    def get_floor(self) -> ParkingFloor:
        return self.parking_floor

    def is_slot_available(self):
        return self.parking_status.EMPTY == ParkingStatus.EMPTY

    def park(self):
        pass

    def display(self):
        print("Slot Number is :", self.slot_number)
        print("Slot Status is :", self.parking_status)
        print("Slot Supported Vehicle Types :",  reduce((lambda x, y: x + "," + y), self.supported_vehicle_type))

        if not self.is_slot_available():
            print("Vehicle Registration Number is: ",  self.vehicle.registration_number)
            print("Vehicle type is: ", self.vehicle.vehicle_type)
            print("Car Color  is: ", self.vehicle.vehicle_color)
