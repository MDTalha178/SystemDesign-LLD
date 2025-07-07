from typing import List
from Criteria.Criteria import Criteria
from FilterStrategies.PriceStrategy.PriceStrategies import PriceStrategy
from models.Product.Product import Product


class PriceFilterCriteria(Criteria):

    def __init__(self, filter_price: int, comparison_strategy):
        self.filter_price = filter_price
        self.comparison_strategy: PriceStrategy = comparison_strategy

    def satisfy(self, products: List[Product]):
        return [
            product for product in products
            if self.comparison_strategy.compare(
                product.product_price,
                self.filter_price
            )
        ]
