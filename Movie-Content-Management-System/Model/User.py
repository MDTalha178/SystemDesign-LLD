from Service.UserService import UserService


class User:

    def __init__(self, user_id, name, preferred_genre):
        self.user_id = user_id,
        self.name = name,
        self.preferred_genre = preferred_genre

        self.user_service = UserService()


    def add_user(self):
        self.user_service.create_user(
            self
        )