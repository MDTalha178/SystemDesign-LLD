from typing import List
from Cart.ProductCart import ProductCart
from Services.CartPriceCalculatorService import CartPriceCalculatorService
from factory.CartProductFactory import CartProductFactory
from models.Product.Product import Product


class CartService:
    cart_memory: List[ProductCart]

    def __init__(self):
        self.cart_memory = []
        self.price_calculator_service = CartPriceCalculatorService()

    def get_cart_details(self, user) -> List[ProductCart]:
        return list(filter(lambda cart: user == cart.user, self.cart_memory))

    def add_cart(self, products: list, user, quantity=1):
        for product in products:
            product_cart: ProductCart = CartProductFactory().create_cart(product, user, quantity)
            self.cart_memory.append(product_cart)

            # set cart value
            product_cart.set_total_price(self.price_calculator_service.calculate_product_based(product_cart))

        # update the cart price
        self.price_calculator_service.calculate_total_cart_value(self.cart_memory)

    def remove_item(self, product: Product, user):
        self.cart_memory = [
            cart_product for cart_product in self.cart_memory
            if not (cart_product.product == product and cart_product.user == user)
        ]

        # update the cart price
        self.price_calculator_service.calculate_total_cart_value(self.cart_memory)

    def get_total_cart_value(self):
        return self.price_calculator_service.get_total_cart_price()
