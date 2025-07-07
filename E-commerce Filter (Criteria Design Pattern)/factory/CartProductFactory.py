from Cart.ProductCart import ProductCart


class CartProductFactory:

    @staticmethod
    def create_cart(product, user, quantity):
        return ProductCart(user, product, quantity)