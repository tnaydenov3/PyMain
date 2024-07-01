from unittest import TestCase

_MSG_TESTCASE = "{result} | {module} | {func_name} | {time}"


class ConsoleTestingLoggerUtil:

    @classmethod
    def _make_testcase_log_msg(cls, testcase: TestCase) -> str:
        pass

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
