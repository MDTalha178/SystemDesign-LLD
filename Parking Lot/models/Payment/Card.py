from models.Payment.payment_strategy import PaymentStrategy


class CarStrategy(PaymentStrategy):
    def pay(self, amount: int):
        print("Pay via card!")