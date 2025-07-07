from datetime import datetime

from Utils.Utils import GenerateOrderId
from models.Order.OrderStateInterface import OrderStateInterface
from models.Order.OrderStatus import OrderStatus
from models.Product.Product import Product
from models.User.User import User


class OrderProduct:
    order_id: str
    product: Product
    order_date: datetime
    quantity: int
    total_price: int
    user: User
    order_status: OrderStateInterface

    def __init__(self, product: Product, user: User, quantity, total_price):
        self.order_id = GenerateOrderId().create_order_id()
        self.product = product
        self.user = user
        self.quantity = quantity
        self.order_date = datetime.now()
        self.total_price = total_price

    def get_product(self) -> Product:
        return self.product

    def get_quantity(self) -> int:
        return self.quantity

    def get_total_price(self) -> int:
        return self.total_price

    def get_order_status(self) -> OrderStatus:
        return self.order_status.get_state()

    def get_details(self):
        print(
            f"Order id is : {self.order_id}\n"
            f"Product Name is: {self.product.product_name} and Quantity is : {self.quantity}\n"
            f"Product price is : {self.product.product_price}\n"
            f"Order status: {self.get_order_status()}\n"
            f"Order Placed at: {self.order_date}\n"
            f"Total Pay : {self.total_price}\n"
        )
