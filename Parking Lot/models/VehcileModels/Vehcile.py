from models.VehcileModels.vehicleInterface import VehicleInterface
from models.VehcileModels.vehicle_type import VehicleType


class Vehicle(VehicleInterface):
    vehicle_type: VehicleType = None
    registration_number: str = None
    vehicle_color: str = None

    def __init__(self, vehicle_type: VehicleType, registration_number: str, vehicle_color: str):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.registration_number = vehicle_color

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def get_registration_number(self) -> str:
        return self.registration_number

    def get_vehicle_color(self) -> str:
        return self.vehicle_color
