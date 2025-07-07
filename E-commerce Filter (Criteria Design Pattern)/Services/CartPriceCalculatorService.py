from typing import List
from functools import reduce

from Cart.ProductCart import ProductCart


class CartPriceCalculatorService:
    __total_cart_price: int

    def calculate_total_cart_value(self, product_cart: List[ProductCart]):
        self.__total_cart_price = reduce(lambda x, cart: x + cart.quantity * cart.product.product_price, product_cart,
                                         0)

    def get_total_cart_price(self):
        return self.__total_cart_price

    @staticmethod
    def calculate_product_based(cart_product: ProductCart):
        return cart_product.product.product_price * cart_product.quantity
