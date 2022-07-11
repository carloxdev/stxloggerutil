# Python's Libraries
import logging


# Own's Libraries
from .log_message import LogMessage


def step(_message, _level=1):
    def inner(func):
        def wrapper(*args, **kwargs):
            msg = LogMessage.get_Start(args, _message, _level)
            logging.debug(msg)
            try:
                response = func(*args, **kwargs)
                logging.debug(LogMessage.get_End(_message, _level, ": OK"))
                return response

            except Exception as e:
                logging.error(LogMessage.get_End(_message, _level, str(e)))
                raise e

        return wrapper
    return inner
