from abc import ABC, abstractmethod
from typing import Optional

from models.ParkingSlotModel.Parkinglot import Parkinglot
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.VehcileModels.Vehcile import Vehicle


class FindSlotStrategy(ABC):

    @abstractmethod
    def find_slot(self, vehicle: Vehicle, parking_lot: Parkinglot) -> Optional[ParkingSlot]:
        raise NotImplementedError("Sub class should have to implement this class!")
