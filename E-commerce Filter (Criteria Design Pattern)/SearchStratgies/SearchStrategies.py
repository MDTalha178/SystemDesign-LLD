from abc import ABC, abstractmethod


class SearchStrategies(ABC):

    @abstractmethod
    def compare(self, product_name, search_product):
        raise NotImplementedError("Subclass should have to implement this class")