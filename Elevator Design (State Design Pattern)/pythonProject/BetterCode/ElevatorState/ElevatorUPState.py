from BetterCode.ElevatorState.StateInterface import ElevatorState


class ElevatorUPState(ElevatorState):
    destination = []

    def __init__(self, floor_number, current_floor, elevator):
        self.floor_number = floor_number
        self.current_floor = current_floor
        self.elevator = elevator

    def moving_up(self, floor_number: int):
        for i in range(self.current_floor, self.destination[-1] + 1):
            print("Current Floor is: ", i)

            if i in self.floor_number:
                print("Destination has Been Reached! and floor number is", i)
            self.elevator.update_current_floor(i)

    def start_moving(self):
        self.destination.append(self.floor_number)
        self.destination.sort()
        self.moving_up(self.floor_number)

    def moving_down(self, floor_number: int):
        raise ValueError("While in a Start Mode elevator can't move Down")

    def start_elevator(self, floor_number: int):
        if floor_number < self.current_floor:
            self.destination.append(floor_number)
            self.destination.sort()

    def destination_reached(self, floor_number: int):
        raise ValueError("While Elevator in a Start Mode elevator can't Reached any Destination")

    def next_elevator_call(self, parked_elevator_call: list):
        raise ValueError("While Elevator in a Start Mode elevator can't move for next elevator call")
