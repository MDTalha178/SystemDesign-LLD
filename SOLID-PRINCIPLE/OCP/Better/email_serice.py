from interface import NotificationServiceInterface
class EmailNotificationService(NotificationServiceInterface):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")