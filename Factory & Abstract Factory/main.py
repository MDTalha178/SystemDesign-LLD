from AbstarctFactory.factory.NotificationFactory import NotificationFactory
from FactoryDesign.Factory.UserFactory import UserFactory


"************* Driver code for Abstract ************"
user_type = 'ADMIN'

user_obj = UserFactory().create_user_instance(user_type)
user_obj.add_user('Talha', 'talha@yopmail.com', '123')

user_type = 'CUSTOMER'
user_obj = UserFactory().create_user_instance(user_type)
user_obj.add_user('arsaln', 'asraln@yopmail.com', '123')


"********** Driver Code Abstract Factory***********"
try:
    notification_type ="EMAIL"

    notification = NotificationFactory()
    notification_obj = notification.create_notification_instance(notification_type)

    # sending notification for Email
    notification_obj.create_alter_notification().send_notification()
    notification_obj.create_welcome_notification().send_notification()

    # sending notification for SMS
    notification_type ="SMS"
    notification_obj = notification.create_notification_instance(notification_type)
    notification_obj.create_welcome_notification().send_notification()
    notification_obj.create_alter_notification().send_notification()

    notification_type ="PUSH"
    notification_obj = notification.create_notification_instance(notification_type)
    notification_obj.create_welcome_notification().send_notification()
    notification_obj.create_alter_notification().send_notification()
except Exception as e:
    print(e)






