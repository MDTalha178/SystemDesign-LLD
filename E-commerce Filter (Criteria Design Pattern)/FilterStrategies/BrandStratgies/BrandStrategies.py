from abc import ABC, abstractmethod


class BrandStrategies(ABC):

    @abstractmethod
    def compare(self, product_brand, filter_product_brand):
        raise NotImplementedError("Sub class should have to implement!")