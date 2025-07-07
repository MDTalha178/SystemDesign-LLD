from BetterCode.ElevatorState.ElevatorDownState import ElevatorDownState
from BetterCode.ElevatorState.ElevatorUPState import ElevatorUPState
from BetterCode.Enum.ElevatorEnum import ElevatorEnum
from BetterCode.Model.Elevator import Elevator


class ElevatorFactory:

    @staticmethod
    def get_elevator_state(elevator:Elevator):
        elevator_type = elevator.state.get_elevaor_state()

        if elevator_type == ElevatorEnum.MOVING_UP:
            return ElevatorUPState
        elif elevator_type == ElevatorEnum.MOVING_DOWN:
            return ElevatorDownState
