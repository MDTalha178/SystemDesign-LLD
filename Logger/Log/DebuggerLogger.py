from Enum.LoggerEnum import LoggerEnum
from Interface.LogInterface import LogInterface
from Interface.PublisherInterface import PublisherInterface


class DebuggerLoggerLevel(LogInterface):

    debugger_logger = {}

    def __init__(self, next_handler:LogInterface, publisher:PublisherInterface):
        self.next_handler = next_handler
        self.publisher = publisher
        self.log_level = LoggerEnum.DEBUG

    def log(self, loglevel:LoggerEnum, message:str):
        if loglevel == LoggerEnum.DEBUG:
            print(f"DEBUG: {message}")
            self.publisher.publish(f"DEBUG: {message}")
            return
        self.next_handler.log(loglevel, message)