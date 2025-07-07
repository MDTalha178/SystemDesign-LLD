from Models.Banks.Banks import Banks
from Models.Banks.HDFCBank import HDFCBank
from Models.PaymentMethod import PaymentMethod
from Payment.PaymentGateWay import PaymentGateWay

pg = PaymentGateWay()
hdfc = HDFCBank()
bank = Banks(hdfc)
print("=== Payment Gateway Demo ===\n")

# Add clients
print("1. Adding Clients:")
print(pg.add_client("Flipkart"))
print(pg.add_client("Amazon"))
print(pg.add_client("Paytm"))
print()

print(pg.clients)
first_key = next(iter(pg.clients))
print("clientID", first_key)

# Add paymode support
print("2. Adding Payment Mode Support:")
pg.add_payment_method(first_key, PaymentMethod.UPI)
print(pg.add_payment_method(first_key, PaymentMethod.DEBIT_CARD))
print(pg.add_payment_method(first_key, PaymentMethod.CREDIT_CARD))
print(pg.remove_payment_method(first_key, PaymentMethod.NET_BANKING))
print()

print("Getting Supported Payment Method")
print(pg.get_supported_payment_mode(first_key))

print()
print("5. Processing Payments:")
pg.make_payment(PaymentMethod.CREDIT_CARD, '100', first_key, bank, {
    "card_number": "1234567890123456",
    "expiry": "12/25",
    "cvv": "123"
})

# pg.make_payment(PaymentMethod.UPI, "2000", first_key, bank, {
#     "VPA": "user@paytm"
# })