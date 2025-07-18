from Log.DebuggerLogger import DebuggerLoggerLevel
from Log.ErrorLogger import ErrorLoggerLevel
from Log.InfoLogger import InfoLoggerLevel
from Log.WarnLogger import WarnLoggerLevel


class LoggingFactory:

    @staticmethod
    def create_logging_chain(publisher):
        return DebuggerLoggerLevel(
            next_handler=ErrorLoggerLevel(
                next_handler=InfoLoggerLevel(
                    next_handler=WarnLoggerLevel(
                        next_handler=None,
                        publisher=publisher
                    ),publisher=publisher
                ),publisher=publisher
            ),publisher=publisher
        )
