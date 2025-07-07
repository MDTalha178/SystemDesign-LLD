from interface import NotificationServiceInterface
class PushNotificationService(NotificationServiceInterface):
    def send_notification(self, message):
        print(f"Sending push notification: {message}")