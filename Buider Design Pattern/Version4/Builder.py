# from Version1.Category import Category


class Builder:
    name: str
    description: str
    price: str
    category: str
    product_images: list
    quantity: int
    is_in_stock: bool

    def set_name(self, value):
        self.name = value

    def set_description(self, value):
        self.description = value

    def set_price(self, value):
        self.name = value

    def set_category(self, value):
        self.category = value

    def set_product_images(self, value):
        self.product_images = value

    def set_quantity(self, value):
        self.quantity = value

    def set_is_in_stock(self):
        self.is_in_stock = self.quantity > 0

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
