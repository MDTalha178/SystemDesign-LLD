from Enum.LoggerEnum import LoggerEnum
from Interface.LogInterface import LogInterface
from Interface.PublisherInterface import PublisherInterface


class WarnLoggerLevel(LogInterface):
    debugger_logger = {}

    def __init__(self, next_handler: LogInterface, publisher: PublisherInterface):
        self.next_handler = next_handler
        self.publisher = publisher
        self.log_level = LoggerEnum.WARNING

    def log(self, loglevel: LoggerEnum, message: str):
        if loglevel == loglevel:
            print(f"WARNING: {message}")
            self.publisher.publish(f"WARNING: {message}")
            return
        if self.next_handler:
            self.next_handler.log(loglevel, message)