import random
import string


class GenerateOrderId:

    @staticmethod
    def create_order_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=12))
