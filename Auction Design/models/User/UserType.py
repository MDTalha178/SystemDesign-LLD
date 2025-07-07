from models.User.UserEnum import UserEnum


class UserType:

    def __init__(self, role_name:UserEnum):
        self.role_name = role_name

    def get_role(self):
        return self.role_name