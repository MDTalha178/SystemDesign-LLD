from FilterStrategies.PriceStrategy.PriceStrategies import PriceStrategy


class PriceLessThanStrategy(PriceStrategy):

    def compare(self, product_price: int, filter_product_price: int):
        return product_price < filter_product_price
