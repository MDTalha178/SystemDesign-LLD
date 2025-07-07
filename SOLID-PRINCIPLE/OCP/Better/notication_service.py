from email_serice import EmailNotificationService
from sms_service import SMSNotificationService
from push_service import PushNotificationService
from interface import NotificationServiceInterface

class SendNotificationService:

    def send(self, notification_type, message):
       for notification in notification_type:
           notification.send_notification(message)


notification = SendNotificationService()
notification.send([EmailNotificationService(), SMSNotificationService(), PushNotificationService()],"Hello I am learning LLD")