from solutions.interface.colors import LogColors
from solutions.interface.util import ConsoleUtil
from solutions.testing.counter import TestResultCounter
from solutions.testing.testcase import PyMainTestCase

_T_RESULT_PASS = LogColors.color_text(PyMainTestCase.PASS, color=LogColors.GREEN)
_T_RESULT_FAIL = LogColors.color_text(PyMainTestCase.FAIL, color=LogColors.RED)

_MSG_RESULT_ERROR = "{result} ({error})"
_T_RESULT_ERROR = LogColors.color_template(_MSG_RESULT_ERROR, result=LogColors.RED)


_T_TESTCASE_LOG = "{result} | {module} | {func_name} | {time}"


_MSG_TOTAL_ALLPASS = "All tests PASSED {passed}/{total} | {time}"
_MSG_TOTAL_DEFAULT = (
    "Total: {total} | PASS {passed}, FAIL {failed}, ERROR {error} | {time}"
)


class ConsoleTestingLoggerUtil:

    @classmethod
    def make_testcase_log_msg(cls, *, testcase: PyMainTestCase) -> str:
        result_val = testcase.result
        error = testcase.error
        module = testcase.func_module
        func_name = testcase.func_name
        time_ns = testcase.time_ns

        if not str(error):
            error = error.__class__.__name__

        match result_val:
            case PyMainTestCase.PASS | PyMainTestCase.FAIL:
                result = _MSG_RESULT_VAL_PASSFAIL.format(result=result_val)
            case PyMainTestCase.ERROR:
                result = _MSG_RESULT_VAL_ERROR.format(result=result_val, error=error)
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

    @classmethod
    def make_testpack_log_msg(cls, *, test_counter: TestResultCounter) -> str:
        total = test_counter.total
        passed = test_counter.passed
        failed = test_counter.failed
        error = test_counter.error
        time_ns = test_counter.time_ns

        time = ConsoleUtil.time_nanosecs_to_human_readable(time_ns=time_ns)

        if test_counter.all_passed():
            log_message = _MSG_TOTAL_ALLPASS.format(
                passed=passed, total=total, time=time
            )

        else:
            log_message = _MSG_TOTAL_DEFAULT.format(
                total=total, passed=passed, failed=failed, error=error, time=time
            )

        return log_message

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
