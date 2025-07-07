from abc import ABC, abstractmethod


class ElevatorState(ABC):

    @abstractmethod
    def moving_down(self, floor_number: int):
        raise NotImplemented("Sub class should be implement this")

    @abstractmethod
    def moving_up(self, floor_number: int):
        raise NotImplemented("Sub class should be implement this")

    @abstractmethod
    def start_elevator(self, floor_number: int):
        raise NotImplemented("Sub class should be implement this")

    @abstractmethod
    def destination_reached(self, floor_number: int):
        raise NotImplemented("Sub class should be implement this")

    @abstractmethod
    def next_elevator_call(self, parked_elevator_call: list):
        raise NotImplemented("Sub class should be implement this")

    @abstractmethod
    def start_moving(self):
        raise NotImplemented("Sub class should be implement this")
