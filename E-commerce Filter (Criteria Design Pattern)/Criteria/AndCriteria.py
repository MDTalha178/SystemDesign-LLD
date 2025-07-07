from typing import List

from Criteria.Criteria import Criteria
from models.Product.Product import Product


class AndCriteria(Criteria):
    criteria: List[Criteria]

    def __init__(self, criteria: List[Criteria]):
        self.criteria = criteria

    def satisfy(self, products: List[Product]):
        return [
            product for product in products
            if not any(criteria.satisfy([product]) == [] for criteria in self.criteria)
        ]
