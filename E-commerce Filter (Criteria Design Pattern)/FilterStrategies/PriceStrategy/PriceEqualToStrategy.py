from FilterStrategies.PriceStrategy.PriceStrategies import PriceStrategy


class PriceEqualToStrategy(PriceStrategy):

    def compare(self, product_price: int, filter_product_price: int):
        return product_price == filter_product_price
