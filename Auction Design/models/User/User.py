import  random
import string
from models.User.UserType import UserType


class User:

    def __init__(self, user_name, name, user_type:UserType):
        self.user_id = ''.join(random.choices(string.ascii_letters,k=7))
        self.user_name = user_name
        self.name = name
        self.user_type = user_type


    @property
    def get_username(self):
        return self.user_name

    @property
    def get_name(self):
        return self.name

    @property
    def get_user_id(self):
        return self.user_id

    def get_details(self):
        print("User id is ", self.user_id)
        print("Username is ,", self.user_name)
        print("Name is ", self.name)
        print("User Type is ", self.user_type.role_name.value)
