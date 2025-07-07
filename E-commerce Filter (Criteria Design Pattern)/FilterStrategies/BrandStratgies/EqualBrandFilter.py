from FilterStrategies.BrandStratgies.BrandStrategies import BrandStrategies


class EqualBrandFilter(BrandStrategies):

    def compare(self, product_brand, filter_product_brand) -> bool:
        return product_brand == filter_product_brand
