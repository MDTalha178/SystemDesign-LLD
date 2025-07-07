import time


class Elevator:
    current_floor = 0  # we consider as first floor
    total_floor = [0, 1, 2, 3, 4, 5]
    stopped_floor = []
    moving_state = None
    parked_request = []

    def __init__(self):
        self.current_floor = 0

    def validate_is_possible_request(self, floor_number):
        if self.moving_state == 'UP':
            if floor_number > self.current_floor:
                self.stopped_floor.append(floor_number)
                self.stopped_floor.sort()
            else:
                self.parked_request.append(floor_number)
        if self.moving_state == 'DOWN':
            if floor_number < self.current_floor:
                self.stopped_floor.append(floor_number)
                self.stopped_floor.sort(reverse=True)
            else:
                self.parked_request.append(floor_number)

    def elevator_call(self, floor_number: int):
        if floor_number not in self.total_floor:
            raise ValueError("Invalid floor requested")

        if self.current_floor == floor_number:
            return

        if self.moving_state is not None:
            self.validate_is_possible_request(floor_number)

        if floor_number > self.current_floor:
            self.moving_state = 'UP'
            self.stopped_floor.append(floor_number)
            self.stopped_floor.sort()
            self.move_up()
        else:
            self.moving_state = 'DOWN'
            self.stopped_floor.append(floor_number)
            self.stopped_floor.sort(reverse=True)
            self.move_down()

    def move_up(self):
        start = self.current_floor
        for i in range(start, (self.stopped_floor[-1] + 1)):
            print("Current  floor is: ", i)
            time.sleep(2)
            if i in self.stopped_floor:
                print("Elevator Stopped at :", i)
                time.sleep(1)
                self.stopped_floor.remove(i)
            self.current_floor = i
        self.stopped_floor = []
        self.moving_state = None

        if self.parked_request is not None:
            print("Park request Processing")
            for i in self.parked_request[1:]:
                self.elevator_call(i)
                self.parked_request.remove(i)

    def move_down(self):
        start = self.current_floor
        for i in range(start, self.stopped_floor[0]-1, -1):
            print("Current  floor is: ", i)
            time.sleep(2)
            if i in self.stopped_floor:
                print("Elevator Stopped at :", i)
                self.stopped_floor.remove(i)
            self.current_floor = i
        self.stopped_floor = []
        self.moving_state = None

        if self.parked_request is not None:
            print("Park request Processing")
            for i in self.parked_request[1:]:
                self.elevator_call(i)
                self.parked_request.remove(i)


obj = Elevator()
obj.elevator_call(4)
obj.parked_request.append(2)
print(obj.current_floor)
obj.elevator_call(2)
obj.elevator_call(0)
obj.elevator_call(3)