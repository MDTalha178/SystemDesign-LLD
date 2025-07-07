from SearchStratgies.SearchStrategies import SearchStrategies


class ProductNameBasedSearchStrategies(SearchStrategies):

    def compare(self, product_name, search_product):
        return product_name.lower() == search_product.lower()
