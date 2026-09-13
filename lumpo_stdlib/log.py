# lumpo_stdlib/log.py
import sys


class LogLevel:
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


_LEVEL_NAMES = {
    LogLevel.DEBUG: "DEBUG",
    LogLevel.INFO: "INFO",
    LogLevel.WARNING: "WARNING",
    LogLevel.ERROR: "ERROR",
    LogLevel.CRITICAL: "CRITICAL",
}


class Logger:
    def __init__(self, level=LogLevel.INFO):
        self.level = level
        self.enabled = True

    def _log(self, level, msg):
        if not self.enabled or level < self.level:
            return
        name = _LEVEL_NAMES.get(level, "INFO")
        line = f"{name}: {msg}"
        if level >= LogLevel.ERROR:
            print(line, file=sys.stderr)
        else:
            print(line)

    def debug(self, msg):
        self._log(LogLevel.DEBUG, msg)

    def info(self, msg):
        self._log(LogLevel.INFO, msg)

    def warning(self, msg):
        self._log(LogLevel.WARNING, msg)

    def error(self, msg):
        self._log(LogLevel.ERROR, msg)

    def critical(self, msg):
        self._log(LogLevel.CRITICAL, msg)


# Default module-level logger
logger = Logger()


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)


def set_log_level(level):
    global logger
    if not isinstance(level, int):
        name = str(level).upper()
        level = getattr(LogLevel, name, LogLevel.INFO)
    logger = Logger(level)


def get_logger():
    return logger
