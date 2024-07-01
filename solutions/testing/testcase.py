import time
from types import FunctionType


class PyMainTestCase:

    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"

    __slots__ = ("_func", "_result", "_time_ns", "_error")

    def __init__(self, func: FunctionType) -> None:
        self._func = func
        self._result = None
        self._time_ns = None
        self._error = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self.func.__name__})>"

    @property
    def func(self) -> FunctionType:
        return self._func

    @property
    def func_name(self) -> str:
        return self._func.__name__

    @property
    def func_module(self) -> str:
        return self._func.__module__

    @property
    def result(self) -> str:
        return self._result

    @property
    def time_ns(self) -> float:
        return self._time_ns

    @property
    def error(self) -> Exception | None:
        return self._error

    def run(self) -> None:
        try:
            start_time = time.perf_counter_ns()
            self._func()
            end_time = time.perf_counter_ns()
            self._result = self.PASS

        except AssertionError as error:
            end_time = time.perf_counter_ns()

            error_func = error.__traceback__.tb_frame.f_code.co_name
            if error_func == self._func.__name__:
                self._result = self.FAIL
            else:
                self._result = self.ERROR

            self._error = error

        except Exception as error:
            end_time = time.perf_counter_ns()
            self._result = self.ERROR
            self._error = error

        self._time_ns = end_time - start_time
