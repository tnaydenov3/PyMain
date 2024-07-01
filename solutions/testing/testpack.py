from solutions.testing.testcase import TestCase


class TestPack:

    __slots__ = "_testcases"

    def __init__(self) -> None:
        self._testcases = []

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (total_tests: {len(self._testcases)})>"

    @property
    def testcases(self) -> list[TestCase]:
        return self._testcases
