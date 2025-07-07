from models.Order.Order import Order
from models.Order.OrderProduct import OrderProduct
from models.Order.OrderStateInterface import OrderStateInterface
from models.Order.OrderStatus import OrderStatus


class OrderConfirmState(OrderStateInterface):

    def __init__(self, order_product: OrderProduct, order: Order):
        self.order_product = order_product
        self.order = order

    def confirm_order_state(self):
        self.order_product.order_status = self

    def cancel_order_state(self):
        raise ValueError("Order Should be confirmed or Placed before cancellation")

    def pending_order_state(self):
        raise ValueError("Order Should be confirmed or Placed before cancellation")

    def refund_order_state(self):
        raise ValueError("Order Should be confirmed or Placed before cancellation")

    def get_state(self):
        return OrderStatus.CONFIRM.value
