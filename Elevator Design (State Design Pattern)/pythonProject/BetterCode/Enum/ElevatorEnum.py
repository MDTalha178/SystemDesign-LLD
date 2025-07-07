from enum import Enum


class ElevatorEnum(Enum):
    READY = 'READY'
    STOP = 'STOP'
    MOVING_UP = 'MOVING_UP'
    MOVING_DOWN = 'MOVING_DOWN'
    OUT_OF_SERVICE = 'OUT_OF_SERVICE'
    OUT_FOR_MAINTENANCE = "OUT_FOR_MAINTENANCE"


