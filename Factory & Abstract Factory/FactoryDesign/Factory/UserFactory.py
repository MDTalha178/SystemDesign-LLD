from FactoryDesign.models.Admin import Admin
from FactoryDesign.models.Customer import Customer


class UserFactory:

    @staticmethod
    def create_user_instance(user_type):
        if user_type == 'ADMIN':
            return Admin()
        if user_type == 'CUSTOMER':
            return Customer()