from Cart.Cart import Cart
# from Cart.ProductCart import ProductCart
from Criteria.AndCriteria import AndCriteria
# from Criteria.BrandFilterCriteria import BrandFilterCriteria
# from Criteria.PriceFilterCriteria import PriceFilterCriteria
from Criteria.ProductNameFilterCriteria import ProductNameFilterCriteria
# from FilterStrategies.BrandStratgies.EqualBrandFilter import EqualBrandFilter
# from FilterStrategies.PriceStrategy.PriceGreaterThanStrategy import PriceGreaterThanStrategy
from SearchStratgies.ProductStratgies.ProductNameBasedSearchStratgies import ProductNameBasedSearchStrategies
# from Services.cartService import CartService
from models.Order.Order import Order
from models.Product.Brand import Brand
from models.Product.Product import Product
from models.Product.ProductCategory import ProductCategory
from models.User.User import User

c1 = ProductCategory("Electronics")

obj1 = Product("Apple", 9999, Brand.APPLE, c1)
obj2 = Product("Samsung", 4999, Brand.SAMSUNG, c1)
obj3 = Product("OPPO", 7888, Brand.OPPO, c1)
obj4 = Product("Xiaomi", 3000, Brand.APPLE, c1)
obj4 = Product("Apple", 3000, Brand.APPLE, c1)

# price_com = PriceGreaterThanStrategy()
# price_criteria = PriceFilterCriteria(440, price_com)
#
# brand_strategies = EqualBrandFilter()
# brand_criteria = BrandFilterCriteria(Brand.APPLE, brand_strategies)
#

user_input = input("Enter the product name : ")
product_strategy = ProductNameBasedSearchStrategies()
product_name = ProductNameFilterCriteria(user_input, product_strategy)

# and_criteria = AndCriteria([price_criteria, brand_criteria])

and_criteria = AndCriteria([product_name])


product = [obj1, obj2, obj3, obj4]
products = and_criteria.satisfy(product)

# brand_stratgies = EqualBrandFilter()
# brand_criteria = BrandFilterCriteria(Brand.APPLE, brand_stratgies)
#
# brand_criteria = AndCriteria([])
# brand_filter_product = and_criteria.criteria()

for product in products:
    print(f"Product name is {product.product_name} and the price is {product.product_price}")


user_obj = User("Md", "Talha", "talha@gmail.com")
cart_obj = Cart()
cart_obj.add_item_to_cart(user_obj, [obj1, obj3, obj4], quantity=2)
cart_details = cart_obj.get_cart_details(user_obj)

print("***************")
for cart_details in cart_details:
    print("--------------")
    cart_details.get_details()

print("Your Total cart Value is:", cart_obj.get_total_cart_value())

print("Removing some Items")
cart_obj.remove_item_from_cart(user_obj, product=obj3)

updated_cart = cart_obj.get_cart_details(user_obj)
for cart_details in updated_cart:
    print("--------------")
    cart_details.get_details()
print("Your Total cart Value is:", cart_obj.get_total_cart_value())

print("-------------------------")

print("Creating Your Order")

order_obj = Order()
order_obj.create_order(updated_cart)
order_ids = order_obj.get_order_id()

for order_id in order_ids:
    order_obj.get_order_details(order_id)


print("Start Cancellation")
for order_id in order_ids:
    order_obj.cancel_order(order_id)
    break

print("After Cancellation")

for order_id in order_ids:
    order_obj.get_order_details(order_id)


