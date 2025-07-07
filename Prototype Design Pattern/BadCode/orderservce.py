import uuid
from EmailService import EmailService

Order_Databse = dict()

class OrderService:
    def __init__(self, name, product_name):
        self.name = name
        self.product_name = product_name
    

    def creat_order(self):
        print(f"Creating and order for {self.name} and the product is {self.product_name}")
        order_id = uuid
        order_dict = {
            'id': str(order_id),
            'user': self.name,
            'product_name': self.product_name
        }

        Order_Databse.update({
            str(order_id): order_dict
        })
        return str(order_id)
    

    def get_order(self, order_id):
        return Order_Databse.get(order_id, 'Sorry Invalid Order ID')



order_data = [
    {'user': 'Jhon', 'product_name': 'Votas AC'},
    {'user': 'Emily', 'product_name': 'Samsung TV'},
    {'user': 'Michael', 'product_name': 'Sony Headphones'},
    {'user': 'Sarah', 'product_name': 'Dell Laptop'},
    {'user': 'David', 'product_name': 'Apple iPhone'},
    {'user': 'Emma', 'product_name': 'HP Printer'},
    {'user': 'Daniel', 'product_name': 'Nike Shoes'},
    {'user': 'Olivia', 'product_name': 'LG Refrigerator'},
    {'user': 'James', 'product_name': 'Canon Camera'},
    {'user': 'Sophia', 'product_name': 'Asus Monitor'},
    {'user': 'William', 'product_name': 'Bose Speakers'},
]

# here we will create order Instance and send eamil
for data in order_data:
    order_insatnce  = OrderService(data.get('user'), data.get('product_name'))
    order_id  = order_insatnce.creat_order()

    print("Here create for this")
    print(order_insatnce.get_order(order_id))

    # Here we will send an email for each Order
    email = EmailService(data.get('user'), "Order Conformation", 'OrderService')
    email.send_email()
