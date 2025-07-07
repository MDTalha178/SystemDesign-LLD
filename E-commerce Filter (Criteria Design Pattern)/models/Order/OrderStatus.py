from enum import Enum


class OrderStatus(Enum):
    CONFIRM = "CONFIRM"
    PENDING = "PENDING"
    CANCEL = "CANCEL"
