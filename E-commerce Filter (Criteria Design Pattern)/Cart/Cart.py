from Services.cartService import CartService
from models.Product.Product import Product


class Cart:

    def __init__(self):
        self.cart_service = CartService()

    def add_item_to_cart(self, user, product: list[Product], quantity=1):
        self.cart_service.add_cart(product, user, quantity)

    def remove_item_from_cart(self, user, product: Product):
        self.cart_service.remove_item(product, user)

    def get_cart_details(self, user):
        return self.cart_service.get_cart_details(user)

    def get_total_cart_value(self):
        return self.cart_service.get_total_cart_value()

    