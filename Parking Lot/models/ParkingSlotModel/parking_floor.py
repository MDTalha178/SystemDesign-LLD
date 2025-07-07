from models.ParkingSlotModel.parkingSlot import ParkingSlot


class ParkingFloor:
    floor_number: int
    parking_slot: list[ParkingSlot]

    def __init__(self, floor: int, parking_slot: list[ParkingSlot]):
        self.floor_number = floor
        self.parking_slot = [parking_slot for parking_slot in parking_slot]

    def get_floor_number(self) -> int:
        return self.floor_number

    def get_parking_slot(self) -> list[ParkingSlot]:
        return self.parking_slot

    def set_parking_floor(self, floor_number: int) -> None:
        self.floor_number = floor_number

    def set_parking_slot(self, parking_slot: list[ParkingSlot]):
        self.parking_slot = parking_slot

    def add_parking_slot(self, parking_slot: ParkingSlot):
        self.parking_slot.append(parking_slot)
