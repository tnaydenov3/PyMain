from solutions.testing.testcase import TestCase


class TestsCounter:

    __slots__ = ("_passed", "_failed", "_error", "_total")

    def __init__(self) -> None:
        self._passed = 0
        self._failed = 0
        self._error = 0
        self._total = 0

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

    def all_passed(self) -> bool:
        return self._passed == self._total

    def increment_counter(self, result: str) -> None:
        self._total += 1
        match result:
            case TestCase.PASS:
                self._passed += 1
            case TestCase.FAIL:
                self._failed += 1
            case TestCase.ERROR:
                self._error += 1
