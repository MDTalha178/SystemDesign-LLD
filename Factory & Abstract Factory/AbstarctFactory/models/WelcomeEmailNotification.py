from AbstarctFactory.Interface.NotificationInterface import Notification


class WelcomeEmailNotification(Notification):

    def send_notification(self):
        print("Sending  welcome notification Email!")