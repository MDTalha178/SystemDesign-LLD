from InMemorydatabase.database_interface import DatabaseInterface


class InMemoryDatabase(DatabaseInterface):

    user_list = []

    def create_data(self, data):
        for i in range(0, 200):
            self.user_list.append(f"user: {i}")

    def get_user(self):
        return self.user_list