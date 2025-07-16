from AbstarctFactory.Interface.NotificationfactoryInterface import NotificationFactoryInterface
from AbstarctFactory.models.AlterSmsNotification import AlterSmsNotification
from AbstarctFactory.models.WelcomeSmsNootification import WelcomeSmsNotification


class SmsNotificationFactory(NotificationFactoryInterface):

    def create_welcome_notification(self):
        return AlterSmsNotification()

    def create_alter_notification(self):
        return WelcomeSmsNotification()
