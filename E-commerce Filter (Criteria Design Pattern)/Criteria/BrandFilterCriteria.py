from typing import List
from Criteria.Criteria import Criteria
from FilterStrategies.BrandStratgies.BrandStrategies import BrandStrategies
from models.Product.Product import Product


class BrandFilterCriteria(Criteria):

    def __init__(self, filter_brand, comparison_strategy:BrandStrategies):
        self.filter_brand = filter_brand
        self.comparison_strategy = comparison_strategy

    def satisfy(self, products: List[Product]):
        return [
            product for product in products
            if self.comparison_strategy.compare(product.product_brand, self.filter_brand)
        ]
