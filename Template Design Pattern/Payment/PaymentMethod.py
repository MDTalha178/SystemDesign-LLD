from enum import Enum


class PaymentMethod(Enum):
    UPI = "UPI"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    WALLET = "WALLET"