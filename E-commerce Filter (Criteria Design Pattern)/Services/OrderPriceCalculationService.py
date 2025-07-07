from Cart.ProductCart import ProductCart


class OrderPriceCalculationService:

    @staticmethod
    def calculate_price(cart_product: ProductCart):
        return cart_product.product.product_price * cart_product.quantity
