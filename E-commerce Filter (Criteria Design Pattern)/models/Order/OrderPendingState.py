import time
from models.Order.Order import Order
from models.Order.OrderProduct import OrderProduct
from models.Order.OrderStateInterface import OrderStateInterface
from models.Order.OrderStatus import OrderStatus


class OrderPendingState(OrderStateInterface):

    def __init__(self, order_product: OrderProduct, order: Order):
        self.order_product = order_product
        self.order = order

    def confirm_order_state(self):
        raise ValueError("Order is in Pending we can't confirm")

    def cancel_order_state(self):
        raise ValueError("Order is pending once it will be confirm then only you can cancel")

    def pending_order_state(self):
        self.order_product.order_status = self

        print("Waiting for Order Conformation")
        from factory.CreateOrderStatus import CreateOrderStatus
        time.sleep(5)
        print("Woo we got the Conformation Now Placing Your Order")
        self.order.update_order_state(
            self.order_product,
            CreateOrderStatus().create_confirm_order_state(
                order_product=self.order_product,
                order=self.order
            )
        )
        print("Your Order Placed Successfully!")

    def refund_order_state(self):
        raise ValueError("Order is pending once it will be confirm then only you can initiate a refund!")

    def get_state(self):
        return OrderStatus.PENDING.value
