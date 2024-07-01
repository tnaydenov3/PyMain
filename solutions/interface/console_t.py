from solutions.interface.util import ConsoleUtil
from solutions.testing.testcase import TestCase


_MSG_TESTCASE = "{result} | {module} | {func_name} | {time}"


class ConsoleTestingLoggerUtil:

    @classmethod
    def _make_testcase_log_msg(cls, testcase: TestCase) -> str:
        result = testcase.result
        module = testcase.func_module
        func_name = testcase.func_name

        time_ns = testcase.time_ns
        time = ConsoleUtil.time_nanosecs_to_human_readable(time_ns=time_ns)

        log_message = _MSG_TESTCASE.format(
            result=result,
            module=module,
            func_name=func_name,
            time=time,
        )

        return log_message

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
