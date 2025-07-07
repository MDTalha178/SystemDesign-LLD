from BetterCode.ElevatorState.ElevatorReadyState import ElevatorReadyState
from BetterCode.ElevatorState.StateInterface import ElevatorState


class Elevator:
    def __init__(self):
        self.state = ElevatorReadyState(self)
        self.current_floor = 0

    def update_elevator_status(self, elevator_state: ElevatorState):
        self.state = elevator_state

    def update_elevator_current_floor(self, current_floor_number):
        self.current_floor = current_floor_number
