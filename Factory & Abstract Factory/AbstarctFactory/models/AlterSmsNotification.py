from AbstarctFactory.Interface.NotificationInterface import Notification


class AlterSmsNotification(Notification):
    def send_notification(self):
        print("Sending Alter SMS Notification")