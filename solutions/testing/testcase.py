from types import FunctionType


class TestCase:

    __slots__ = ("_func",)

    def __init__(self, func: FunctionType) -> None:
        self._func = func

    @property
    def func(self) -> FunctionType:
        return self._func
