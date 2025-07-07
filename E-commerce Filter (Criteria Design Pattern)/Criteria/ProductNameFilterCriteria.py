from typing import List
from Criteria.Criteria import Criteria
from SearchStratgies.SearchStrategies import SearchStrategies
from models.Product.Product import Product


class ProductNameFilterCriteria(Criteria):

    def __init__(self, filter_product_name, strategy: SearchStrategies):
        self.filter_product_name = filter_product_name
        self.strategy = strategy

    def satisfy(self, products: List[Product]):
        return [
            product for product in products
            if self.strategy.compare(product.product_name, self.filter_product_name)
        ]
