from models.Product.Product import Product
from models.User.User import User


class ProductCart:
    product: Product
    quantity: int
    total_price: int
    user: User

    def __init__(self, user, product: Product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_user(self):
        return self.user

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_details(self):
        print(f"Product Name is: {self.product.product_name} \n"
              f"Product price is: {self.product.product_price} \n"
              f"Product Quantity is {self.quantity}"
              f"Total Price is:  {self.total_price}"
              )
