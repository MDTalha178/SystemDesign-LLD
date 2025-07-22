from Interface.PaymentStartegyInterface import PaymentStrategy


class PaymentGateWay:

    @staticmethod
    def process_payment(amount, payment_method:PaymentStrategy):
        payment_method.process_payment(amount, credential={"UPI": 'test@ybl'})


