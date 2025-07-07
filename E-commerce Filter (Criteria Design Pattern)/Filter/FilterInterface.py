from abc import ABC, abstractmethod
from typing import List

from models.Product.Product import Product


class FilterCriteriaInterface(ABC):

    @abstractmethod
    def satisfy(self, product: List[Product]):
        raise NotImplementedError("Subclass should have to implement this class")
