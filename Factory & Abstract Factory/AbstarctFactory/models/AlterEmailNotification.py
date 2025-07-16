from AbstarctFactory.Interface.NotificationInterface import Notification


class AlterEmailNotification(Notification):

    def send_notification(self):
        print("Sending Alter notification Email!")