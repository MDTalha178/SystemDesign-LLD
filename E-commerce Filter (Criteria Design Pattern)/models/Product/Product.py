from models.Product.Brand import Brand
from models.Product.ProductCategory import ProductCategory


class Product:
    product_name: str
    product_price: int
    product_brand: Brand
    product_category: ProductCategory

    def __init__(
            self,
            product_name: str,
            product_price: int,
            product_brand: Brand,
            product_category: ProductCategory,

    ):
        self.product_name = product_name
        self.product_price = product_price
        self.product_brand = product_brand
        self.product_category = product_category
