"""
This class is used to responsible a  send email to user
"""
import copy

class EmailService:
    def __init__(self, subject, email_service):
        self.__subject = subject
        self.__email_service = email_service
        self.__template = self.load_template() 
    
    def load_template(self):
        print("Supose This tempate get from S3 and this a heavy opration and we need to replace a user details this opeartion take time")

    def send_email(self, user):
        print(f"Sending an email to {user}")
    
    def get_subject(self):
        return self.__subject
    

    def get_email_service(self):
        return self.__email_service

    def get_template(self):
        return self.__template
    
    def clone(self):
        """
        Here we will cloning the objects
        """
        return copy.copy(self)
    
    
