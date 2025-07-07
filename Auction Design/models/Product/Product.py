class Product:

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price



    @property
    def get_product_name(self):
        return self.product_name

    @property
    def get_product_price(self):
        return self.product_price
