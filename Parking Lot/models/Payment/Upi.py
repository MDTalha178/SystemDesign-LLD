from models.Payment.payment_strategy import PaymentStrategy


class UPIStrategy(PaymentStrategy):

    def pay(self, amount: int):
        print("Pay via strategy")
