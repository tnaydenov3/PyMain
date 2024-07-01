from solutions.testing.testcase import PyMainTestCase


class TestResultCounter:

    __slots__ = ("_passed", "_failed", "_error", "_total", "_time_ns")

    def __init__(self) -> None:
        self._passed = 0
        self._failed = 0
        self._error = 0
        self._total = 0
        self._time_ns = 0

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (total_ran: {self._total})>"

    @property
    def passed(self) -> int:
        return self._passed

    @property
    def failed(self) -> int:
        return self._failed

    @property
    def error(self) -> int:
        return self._error

    @property
    def total(self) -> int:
        return self._total

    @property
    def time_ns(self) -> int:
        return self._time_ns

    def all_passed(self) -> bool:
        return self._passed == self._total

    def increment_counter(self, *, testcase: PyMainTestCase) -> None:
        self._total += 1

        match testcase.result:
            case PyMainTestCase.PASS:
                self._passed += 1
            case PyMainTestCase.FAIL:
                self._failed += 1
            case PyMainTestCase.ERROR:
                self._error += 1

        self._time_ns += testcase.time_ns
