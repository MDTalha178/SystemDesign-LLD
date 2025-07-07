from Version1.Category import Category


class Product:
    name: str
    description: str
    price: str
    category: Category
    product_images: list
    quantity: int
    is_in_stock: bool

    def __int__(self, name, price, category, product_images, quantity, description):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.product_images = product_images
        self.is_in_stock = quantity > 0
        self.description = description


""""
Issue in this code when any one create a object of product they have remember the order of parameter
"""
