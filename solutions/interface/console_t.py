from solutions.testing.testcase import TestCase


_MSG_TESTCASE = "{result} | {module} | {func_name} | {time}"


class ConsoleTestingLoggerUtil:

    @classmethod
    def _make_testcase_log_msg(cls, testcase: TestCase) -> str:
        result = testcase.result

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
