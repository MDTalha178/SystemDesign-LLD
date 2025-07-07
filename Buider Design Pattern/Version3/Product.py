from Version1.Category import Category
from Version3.Builder import Builder


class Product:
    name: str
    description: str
    price: str
    category: Category
    product_images: list
    quantity: int
    is_in_stock: bool

    def __int__(self, builder: Builder):
        self.name = builder.get_name
        self.description = builder.description
        self.category = builder.category
        self.product_images = builder.product_images
        self.price = builder.price
        self.is_in_stock = builder.is_in_stock
        self.quantity = builder.quantity


""""
now its pretty much clean Issue in this code when any one create a object of product we are exposing of
constructor to accept any thing a
"""
