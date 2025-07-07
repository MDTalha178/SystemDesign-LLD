from models.VehcileModels.Vehcile import Vehicle
from models.VehcileModels.vehicle_type import VehicleType


class ElectricVehicle(Vehicle):
    def __init__(self, vehicle_type: VehicleType, registration_number: str, vehicle_color: str):
        super().__init__(vehicle_type, registration_number, vehicle_color)
