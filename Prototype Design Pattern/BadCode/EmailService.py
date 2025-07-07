"""
This class is used to responsible a  send email to user
"""
class EmailService:
    def __init__(self, user, subject, email_service):
        self.user = user
        self.subject = subject
        self.email_service = email_service
        self.template = "Supose This tempate get from S3 and this a heavy opration and we need to replace a user details this opeartion take time"
    

    def send_email(self):
        print(f"Sending an email to {self.user}")
    
