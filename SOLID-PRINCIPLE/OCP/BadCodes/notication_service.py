from email_serice import EmailNotificationService
from sms_service import SMSNotificationService
from push_service import PushNotificationService

class SendNotificationService:

    def send_notification(self, notification_type, message):
        if notification_type == "email":
            email = EmailNotificationService()
            email.send_email_notification(message)
        elif notification_type == "sms":
            email = SMSNotificationService()
            email.send_sms_notification(message)
        elif notification_type == "push":
            email = PushNotificationService()
            email.send_push_notification(message)
        else:
            print(f"Invalid notification type: {notification_type}")