import time

from Payment.PaymentGateway import PaymentGateWay
from PaymentStrategy.CardPayment import CardPayment
from PaymentStrategy.UpiPayment import UPIPayment

upi_pay = UPIPayment()
payment_gateway = PaymentGateWay()

print("********Testing UPI payment********")
payment_gateway.process_payment(
    1200, upi_pay
)

print("********Testing Card payment********")
time.sleep(5)
card = CardPayment()
payment_gateway.process_payment(
    344, card
)