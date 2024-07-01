import sys

from solutions.interface.colors import LogColors
from solutions.interface.console_t import ConsoleTestingLoggerUtil
from solutions.testing.counter import TestResultCounter
from solutions.testing.testcase import PyMainTestCase

_UTIL_PREV_LINE = "\033[F"
_UTIL_CLEAR_PREV_LINE = "\033[F\033[K"


class ConsoleLogger:

    _LOG_TEMPL = "[{prefix}] {message}"

    @staticmethod
    def _log_to_console(message: str, /, *, newline: bool = True) -> None:
        eol = "\n" if newline else ""
        sys.stdout.write(f"{message}{eol}")
        sys.stdout.flush()

    @classmethod
    def log(
        cls,
        message: str,
        /,
        *,
        prefix: str,
        color_msg: str = None,
        color_prefix: str = None,
    ) -> None:
        if color_msg:
            message = LogColors.color_text(text=message, color=color_msg)
        if color_prefix:
            prefix = LogColors.color_text(text=prefix, color=color_prefix)

        log_msg = cls._LOG_TEMPL.format(prefix=prefix, message=message)
        cls._log_to_console(message=log_msg)

    @classmethod
    def log_test_result(cls, *, testcase: PyMainTestCase) -> None:
        log_msg = ConsoleTestingLoggerUtil.make_testcase_log_msg(testcase=testcase)
        cls._log_to_console(message=log_msg)

    @classmethod
    def log_testpack_result(cls, *, counter: TestResultCounter) -> None:
        log_msg = ConsoleTestingLoggerUtil.make_testpack_log_msg(test_counter=counter)
        cls._log_to_console(message=log_msg)

    @classmethod
    def clear_last_line(cls) -> None:
        cls._log_to_console(message=_UTIL_CLEAR_PREV_LINE, newline=False)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
