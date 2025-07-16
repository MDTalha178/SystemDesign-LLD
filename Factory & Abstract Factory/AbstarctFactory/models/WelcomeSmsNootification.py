from AbstarctFactory.Interface.NotificationInterface import Notification


class WelcomeSmsNotification(Notification):
    def send_notification(self):
        print("Sending Welcome  SMS notification")