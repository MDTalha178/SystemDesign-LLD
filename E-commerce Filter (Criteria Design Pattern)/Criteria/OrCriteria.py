from typing import List

from Criteria.Criteria import Criteria
from models.Product.Product import Product


class OrCriteria(Criteria):

    def __init__(self, criteria: List[Criteria]):
        self.criteria = criteria

    def satisfy(self, products: List[Product]):
        return [
            product for product in products
            if any(criteria.satisfy([product]) != [] for criteria in self.criteria)
        ]
