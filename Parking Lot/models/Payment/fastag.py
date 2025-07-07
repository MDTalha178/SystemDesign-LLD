from models.Payment.payment_strategy import PaymentStrategy


class FasttagStrategy(PaymentStrategy):

    def pay(self, amount: int):
        print("Pay via fasttag")