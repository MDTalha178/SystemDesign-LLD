from AbstarctFactory.Interface.NotificationfactoryInterface import NotificationFactoryInterface
from AbstarctFactory.models.AlterEmailNotification import AlterEmailNotification
from AbstarctFactory.models.WelcomeEmailNotification import WelcomeEmailNotification


class EmailNotificationFactory(NotificationFactoryInterface):

    def create_welcome_notification(self):
        return WelcomeEmailNotification()

    def create_alter_notification(self):
        return AlterEmailNotification()
