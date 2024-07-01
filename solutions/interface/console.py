import sys

from solutions.interface.console_t import ConsoleTestingLoggerUtil
from solutions.testing.testcase import TestCase

_UTIL_PREV_LINE = "\033[F"
_UTIL_CLEAR_PREV_LINE = "\033[F\033[K"


class ConsoleLogger:

    _LOG_TEMP = "[{prefix}] {message}"

    @staticmethod
    def _log_to_console(message: str, *, newline: bool = True) -> None:
        eol = "\n" if newline else ""
        sys.stdout.write(f"{message}{eol}")
        sys.stdout.flush()

    @classmethod
    def log(cls, message: str, *, prefix: str) -> None:
        log_msg = cls._LOG_TEMP.format(prefix=prefix, message=message)
        cls._log_to_console(message=log_msg)

    @classmethod
    def log_test_result(cls, testcase: TestCase) -> None:
        log_msg = ConsoleTestingLoggerUtil._make_testcase_log_msg(testcase=testcase)
        cls._log_to_console(message=log_msg)

    @classmethod
    def clear_last_line(cls) -> None:
        cls._log_to_console(message=_UTIL_CLEAR_PREV_LINE, newline=False)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
