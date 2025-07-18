from Interface.SubscriberInterface import SubscriberInterface


class ConsoleSubscriber(SubscriberInterface):
    def update(self, message:str):
        print("NEW UPDATE IN CONSOLE SUBSCRIBER")
        print(message)