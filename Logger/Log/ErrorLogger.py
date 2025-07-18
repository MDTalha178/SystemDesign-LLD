from Enum.LoggerEnum import LoggerEnum
from Interface.LogInterface import LogInterface
from Interface.PublisherInterface import PublisherInterface


class ErrorLoggerLevel(LogInterface):
    debugger_logger = {}

    def __init__(self, next_handler:LogInterface, publisher:PublisherInterface):
        self.next_handler = next_handler
        self.publisher = publisher
        self.log_level = LoggerEnum.ERROR

    def log(self, loglevel: LoggerEnum, message: str):
        if loglevel == LoggerEnum.ERROR:
            print(f"ERROR: {message}")
            self.publisher.publish(f"ERROR: {message}")
            return
        self.next_handler.log(loglevel, message)