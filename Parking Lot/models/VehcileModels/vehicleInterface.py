from abc import ABC, abstractmethod

from models.VehcileModels.vehicle_type import VehicleType


class VehicleInterface(ABC):
    vehicle_type: VehicleType
    registration_number: str
    vehicle_color: str

    @abstractmethod
    def get_vehicle_type(self) -> VehicleType:
        raise NotImplementedError("Sub class should have to implement this")

    @abstractmethod
    def get_registration_number(self) -> str:
        raise NotImplementedError("Sub should have to implement this")

    @abstractmethod
    def get_vehicle_color(self) -> str:
        raise NotImplementedError("Sub should have to implement this")
