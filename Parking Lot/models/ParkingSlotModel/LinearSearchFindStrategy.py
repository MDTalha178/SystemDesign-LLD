from typing import Optional

from models.ParkingSlotModel.FindSlotStrategy import FindSlotStrategy
from models.ParkingSlotModel.Parkinglot import Parkinglot
from models.ParkingSlotModel.parkingSlot import ParkingSlot
from models.VehcileModels.Vehcile import Vehicle


class LinearSearchFindStrategy(FindSlotStrategy):

    def find_slot(self, vehicle: Vehicle, parking_lot: Parkinglot) -> Optional[ParkingSlot]:
        parking_floor = parking_lot.get_parking_floor()
        for park_floor in parking_floor:
            parking_slot = park_floor.get_parking_slot()
            for park_slot in parking_slot:
                if park_slot.is_slot_available():
                    park_slot.display()
                    return park_slot
        print("Sorry No Slot Available")
        return None
