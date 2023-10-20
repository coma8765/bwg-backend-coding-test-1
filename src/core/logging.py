import logging

_app_logger = logging.getLogger("app")


def get_logger(name: str):
    return _app_logger.getChild(name)
