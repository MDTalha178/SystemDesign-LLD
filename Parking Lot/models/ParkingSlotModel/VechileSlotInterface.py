from abc import ABC, abstractmethod


class ElectricVehicleCarSlot(ABC):

    @abstractmethod
    def charge_vehicle(self):
        raise NotImplementedError("Subclass should have to implement this!")


class BiKeSlotInterface(ABC):
    pass


class CarSlotInterface(ABC):
    pass
