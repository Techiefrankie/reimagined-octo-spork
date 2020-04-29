import logging


class Config:
    LOGGER_FILE = "logs.log"
    LOG_FORMAT = "%(levelname)s %(asctime)s: %(message)s"


class DevConfig(Config):
    LOG_LEVEL = logging.DEBUG
