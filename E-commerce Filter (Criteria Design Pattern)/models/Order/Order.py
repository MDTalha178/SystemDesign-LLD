from typing import List
from Cart.ProductCart import ProductCart
from models.Order.OrderProduct import OrderProduct
from models.Order.OrderStateInterface import OrderStateInterface


class Order:
    __order_id_in_memory = []

    def __init__(self):
        from Services.OrderService import OrderService
        self.order_service = OrderService()

    def create_order(self, product_cart: List[ProductCart]):
        self.order_service.create_order(product_cart, self.__order_id_in_memory, self)

    def get_order_details(self, order_id):
        return self.order_service.get_order_detail(order_id)

    def update_order_state(self, order_product: OrderProduct, state: OrderStateInterface):
        self.order_service.update_order_status(
            order_product=order_product,
            order_status=state
        )

    def cancel_order(self, order_id):
        self.order_service.cancel_order(order_id, self)

    def get_order_id(self):
        return self.__order_id_in_memory
