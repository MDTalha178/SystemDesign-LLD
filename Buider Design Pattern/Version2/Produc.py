from Version1.Category import Category


class Product:
    name: str
    description: str
    price: str
    category: Category
    product_images: list
    quantity: int
    is_in_stock: bool

    def __int__(self, **kwargs):
        self.name = kwargs.get('name')
        self.price = kwargs.get('price')
        self.category = kwargs.get('category')
        self.quantity = kwargs.get('quantity')
        self.product_images = kwargs.get('product_images')
        self.is_in_stock = kwargs.get('quantity') > 0
        self.description = kwargs.get('description')


""""
Issue in this code when any one create a object of product so they forgot to send or add any value in 
my dictionary product class will get None which violation of product attribute values
"""