from models.Order.OrderProduct import OrderProduct


class OrderFactory:

    @staticmethod
    def create_order(product, user, quantity, total_price):
        return OrderProduct(product, user, quantity, total_price)
