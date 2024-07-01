from solutions.interface.colors import TextColors
from solutions.interface.util import ConsoleUtil
from solutions.testing.counter import TestResultCounter
from solutions.testing.testcase import PyMainTestCase

MSG_PASS = TextColors.green(PyMainTestCase.PASS)
MSG_FAIL = TextColors.yellow(PyMainTestCase.FAIL)
MSG_ERROR = TextColors.red(PyMainTestCase.ERROR)

_T_RESULT_ERROR = f"{MSG_ERROR}: {{error}}"

_T_TESTCASE_LOG = "{result} | {module} | {func_name} | {time}"

_MSG_TOTAL_ALLPASS = "All tests PASSED {passed}/{total} | {time}"
_T_TOTAL_ALLPASS = TextColors.col_templ_custom(
    _MSG_TOTAL_ALLPASS,
    passed=TextColors.GREEN,
    total=TextColors.GREEN,
)

_MSG_TOTAL_DEFAULT = (
    "Total: {total} | PASS {passed}, FAIL {failed}, ERROR {error} | {time}"
)
_T_TOTAL_DEFAULT = TextColors.col_templ_custom(
    _MSG_TOTAL_DEFAULT,
    passed=TextColors.GREEN,
    failed=TextColors.RED,
    error=TextColors.RED,
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
            case PyMainTestCase.PASS:
                result = MSG_PASS
            case PyMainTestCase.FAIL:
                result = MSG_FAIL
            case PyMainTestCase.ERROR:
                result = _T_RESULT_ERROR.format(error=error)
            case _:
                raise NotImplementedError

        time = ConsoleUtil.time_nanosecs_to_human_readable(time_ns=time_ns)

        log_message = _T_TESTCASE_LOG.format(
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
            log_message = _T_TOTAL_ALLPASS.format(passed=passed, total=total, time=time)

        else:
            log_message = _T_TOTAL_DEFAULT.format(
                total=total, passed=passed, failed=failed, error=error, time=time
            )

        return log_message

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
