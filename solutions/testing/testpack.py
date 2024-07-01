from solutions.testing.testcase import TestCase


class TestPack:

    __slots__ = ("_testcases", "_passed", "_failed", "_error")

    def __init__(self) -> None:
        self._testcases = []
        self._passed = 0
        self._failed = 0
        self._error = 0

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (total_tests: {len(self._testcases)})>"

    @property
    def testcases(self) -> list[TestCase]:
        return self._testcases
