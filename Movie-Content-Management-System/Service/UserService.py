from Model.User import User


class UserService:

    def __init__(self):
        self.user = {str:User}

    def create_user(self, user:User):
        self.user.update({
            user.user_id:user
        })
        print("User is created successfully!")

    def check_user_is_valid(self, user_id):
        if self.user.get(user_id):
            return True
        print("User ID is Invalid!")
        return False