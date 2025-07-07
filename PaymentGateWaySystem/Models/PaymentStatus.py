from enum import Enum


class PaymentStatus(Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    SUCCESSFUL = "Successful"
    FAILED = 'Failed'