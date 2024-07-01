from solutions.interface.util import ConsoleUtil
from solutions.testing.testcase import TestCase

_MSG_RESULT_VAL_PASSFAIL = "{result}"
_MSG_RESULT_VAL_ERROR = "{result} ({error})"

_MSG_TESTCASE = "{result} | {module} | {func_name} | {time}"


class ConsoleTestingLoggerUtil:

    @classmethod
    def _make_testcase_log_msg(cls, testcase: TestCase) -> str:
        result_val = testcase.result
        module = testcase.func_module
        func_name = testcase.func_name
        time_ns = testcase.time_ns

        match result_val:
            case TestCase.PASS | TestCase.FAIL:
                result = _MSG_RESULT_VAL_PASSFAIL.format(result=result_val)
            case TestCase.ERROR:
                result = _MSG_RESULT_VAL_ERROR.format(
                    result=result_val, error=testcase.error
                )
            case _:
                raise NotImplementedError

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
