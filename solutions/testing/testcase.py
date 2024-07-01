from types import FunctionType


class TestCase:

    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"

    __slots__ = ("_func", "_result", "_time")

    def __init__(self, func: FunctionType) -> None:
        self._func = func
        self._result = None
        self._time = None
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
    def time(self) -> float:
        return self._time

    @property
    def error(self) -> Exception | None:
        return self._error
