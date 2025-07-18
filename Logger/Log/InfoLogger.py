from Enum.LoggerEnum import LoggerEnum
from Interface.LogInterface import LogInterface
from Interface.PublisherInterface import PublisherInterface


class InfoLoggerLevel(LogInterface):
    debugger_logger = {}

    def __init__(self, next_handler: LogInterface, publisher: PublisherInterface):
        self.next_handler = next_handler
        self.publisher = publisher
        self.log_level = LoggerEnum.INFO

    def log(self, loglevel: LoggerEnum, message: str):
        if loglevel == LoggerEnum.INFO:
            print(f"INFO: {message}")
            self.publisher.publish(f"INFO: {message}")
            return
        self.next_handler.log(loglevel, message)