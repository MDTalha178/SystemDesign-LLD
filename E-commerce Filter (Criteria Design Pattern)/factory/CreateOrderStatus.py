from models.Order.Order import Order
from models.Order.OrderCancellationState import OrderCancellationState
from models.Order.OrderConfirmState import OrderConfirmState
from models.Order.OrderPendingState import OrderPendingState
from models.Order.OrderProduct import OrderProduct


class CreateOrderStatus:

    @staticmethod
    def create_pending_order_status(order_product: OrderProduct, order: Order):
        return OrderPendingState(
            order_product=order_product,
            order=order
        )

    @staticmethod
    def create_confirm_order_state(order_product: OrderProduct, order: Order):
        return OrderConfirmState(
            order_product=order_product,
            order=order
        )

    @staticmethod
    def create_cancel_order_state(order_product: OrderProduct, order: Order):
        return OrderCancellationState(
            order_product=order_product,
            order=order
        )



