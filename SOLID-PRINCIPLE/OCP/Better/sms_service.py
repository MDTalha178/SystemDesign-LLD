from interface import NotificationServiceInterface
class SMSNotificationService(NotificationServiceInterface):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")