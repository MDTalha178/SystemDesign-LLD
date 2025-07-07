# from Version1.Category import Category


class Product:
    __name: str
    __description: str
    __price: str
    __category: str
    __product_images: list
    __quantity: int
    __is_in_stock: bool

    def __init__(self, builder):
        self.__name = builder.get_name
        self.__description = builder.description
        self.__price = builder.price
        self.__product_images = builder.product_images
        self.__category = builder.get_category
        self.__is_in_stock = builder.is_in_stock

    @staticmethod
    def get_builder():
        from Version3.Builder import Builder
        return Builder()

    def get_name(self):
        return self.__name


""""
now its pretty much clean Issue in this code when any one create a object of product we are exposing of
constructor to accept any thing a
"""
