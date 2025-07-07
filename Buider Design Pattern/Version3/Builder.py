from Version1.Category import Category
from Version4.Prouuct import Product


class Builder:
    name: str
    description: str
    price: str
    category: Category
    product_images: list
    quantity: int
    is_in_stock: bool

    def set_name(self, value):
        self.name = value
        return self

    def set_description(self, value):
        self.description = value
        return self

    def set_price(self, value):
        self.price = value
        return self

    def set_category(self, value):
        self.category = value
        return self

    def set_product_images(self, value):
        self.product_images = value
        return self

    def set_quantity(self, value):
        self.quantity = value
        return self

    def set_is_in_stock(self):
        self.is_in_stock = self.quantity > 0
        return self

    @property
    def get_name(self):
        return self.name

    @property
    def get_description(self):
        return self.description

    @property
    def get_price(self):
        return self.price

    @property
    def get_category(self):
        return self.category

    @property
    def get_product_images(self):
        return self.product_images

    @property
    def get_quantity(self):
        return self.quantity

    @property
    def get_is_in_stock(self):
        return self.is_in_stock

    def build(self):
        return Product(self)
