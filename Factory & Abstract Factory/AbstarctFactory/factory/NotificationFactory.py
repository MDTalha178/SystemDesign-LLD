from AbstarctFactory.factory.EmailNotificationFactory import EmailNotificationFactory
from AbstarctFactory.factory.SmsNotificationFactory import SmsNotificationFactory


class NotificationFactory:

    @staticmethod
    def create_notification_instance(notification_type):
        if notification_type == 'EMAIL':
            return EmailNotificationFactory()
        elif notification_type == 'SMS':
            return SmsNotificationFactory()
        raise ValueError("Notification Type not supported!")