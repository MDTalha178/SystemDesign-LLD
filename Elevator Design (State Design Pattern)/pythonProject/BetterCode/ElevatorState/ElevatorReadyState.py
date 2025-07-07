from BetterCode.ElevatorState.ElevatorDownState import ElevatorDownState
from BetterCode.ElevatorState.ElevatorUPState import ElevatorUPState
from BetterCode.ElevatorState.StateInterface import ElevatorState
from BetterCode.Factory.elevator_factory import ElevatorFactory
from BetterCode.Model.Elevator import Elevator


class ElevatorReadyState(ElevatorState):

    def __init__(self, elevator: Elevator):
        self.elevator = elevator

    def moving_up(self, floor_number: int):
        raise ValueError("While in a ready Mode elevator can't move up")

    def moving_down(self, floor_number: int):
        raise ValueError("While in a ready Mode elevator can't move Down")

    def start_elevator(self, floor_number: int):
        if floor_number > self.elevator.current_floor:
            self.elevator.update_elevator_status(
                ElevatorUPState(floor_number, self.elevator.current_floor, self.elevator))
        else:
            self.elevator.update_elevator_status(
                ElevatorDownState(self.elevator, self.elevator.current_floor, floor_number))
        self.elevator.state.start_moving()

    def destination_reached(self, floor_number: int):
        raise ValueError("While Elevator in a ready Mode elevator can't Reached any Destination")

    def next_elevator_call(self, parked_elevator_call: list):
        raise ValueError("While Elevator in a ready Mode elevator can't move for next elevator call")

    def start_moving(self):
        raise ValueError("While Elevator in a ready Mode elevator can't start moving")
