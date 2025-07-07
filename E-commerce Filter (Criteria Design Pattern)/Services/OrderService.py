from typing import List
from Cart.ProductCart import ProductCart
from Services.OrderPriceCalculationService import OrderPriceCalculationService
from factory.CreateOrderStatus import CreateOrderStatus
from factory.OrderFactory import OrderFactory
from models.Order.OrderCancellationState import OrderCancellationState
from models.Order.OrderPendingState import OrderPendingState
from models.Order.OrderProduct import OrderProduct
from models.Order.OrderStateInterface import OrderStateInterface


class OrderService:

    def __init__(self):
        self.order_factory = OrderFactory()
        self.price_calculation_service = OrderPriceCalculationService()
        self.order_memory: List[OrderProduct] = []

    def create_order(self, product_order: List[ProductCart], order_id_memory: List, order_obj):
        for order in product_order:
            order_details: OrderProduct = self.order_factory.create_order(
                order.product, order.user, order.quantity, self.price_calculation_service.calculate_price(
                    order
                )
            )

            # update the Order state
            order_obj.update_order_state(
                order_details, CreateOrderStatus().create_pending_order_status(
                    order_product=order_details,
                    order=order_obj
                )
            )

            order_id_memory.append(order_details.order_id)
            self.order_memory.append(order_details)
        print("Order Placed Successfully!")

    def cancel_order(self, order_id, order_obj):
        print("Cancelling Your Order Please wait!")
        order_product = self.get_order_detail(order_id)
        if not order_product:
            print("Sorry Order ID is Invalid!")

        order_obj.update_order_state(
            order_product=order_product,
            state=CreateOrderStatus().create_cancel_order_state(
                order_product=order_product,
                order=order_obj
            )

        )
        print("Your Order Cancel Successfully!")
        self.get_order_detail(order_id)

    def get_order_detail(self, order_id):
        order_details = None
        for order in self.order_memory:
            if order.order_id == order_id:
                order_details = order
                break
        if order_details:
            order_details.get_details()
            return order_details
        print("Order id is Invalid!")

    @staticmethod
    def update_order_status(order_product: OrderProduct, order_status: OrderStateInterface):
        order_product.order_status = order_status

        if isinstance(order_status, OrderPendingState):
            order_product.order_status.pending_order_state()

        if isinstance(order_status, OrderCancellationState):
            order_product.order_status.cancel_order_state()
