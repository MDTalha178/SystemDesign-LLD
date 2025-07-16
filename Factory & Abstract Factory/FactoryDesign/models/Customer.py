from FactoryDesign.Interface import UserInterface


class Customer(UserInterface):

    def __init__(self):
        self.name = None
        self.email = None
        self.password = None

    def get_user_type(self):
        return "ADMIN"

    def get_user_details(self):
        return {"Name": self.name, "Email": self.email}

    def add_user(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email
        print("Customer Created!")
