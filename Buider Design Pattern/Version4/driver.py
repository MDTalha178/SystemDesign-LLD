
from Version4.Prouuct import Product

# category = Category
product_obj = (Product.get_builder()
               .set_name("Apple")
               .set_description("Its and Iphone Apple 14pro")
               .set_price("1122222")
               .set_category("Apple")
               .set_quantity(1222)
               .set_product_images(['Image1', 'Image2'])
               .set_is_in_stock().build())

print(product_obj.get_name())
