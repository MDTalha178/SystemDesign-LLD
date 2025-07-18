from Enum.LoggerEnum import LoggerEnum
from Factory.LogingFactory import LoggingFactory
from Publisher.ConsoleSubscriber import ConsoleSubscriber
from Publisher.PublisherImpl import PublisherImpl


console_subs = ConsoleSubscriber()

publisher = PublisherImpl()
publisher.subscribe(subscriber=console_subs)


factory = LoggingFactory().create_logging_chain(publisher)
factory.log(LoggerEnum.DEBUG, "Debug Message")
factory.log(LoggerEnum.INFO, "Info Message")
factory.log(LoggerEnum.ERROR, "Error Message")
factory.log(LoggerEnum.WARNING, "Warning Message")