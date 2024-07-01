from solutions.interface.console import ConsoleLogger
from solutions.testing.testcase import TestCase


class TestPack:

    __slots__ = ("_testcases", "_passed", "_failed", "_error")

    def __init__(self) -> None:
        self._testcases: list[TestCase] = []
        self._passed = 0
        self._failed = 0
        self._error = 0

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (total_tests: {len(self._testcases)})>"

    @property
    def testcases(self) -> list[TestCase]:
        return self._testcases

    def add_testcase(self, testcase: TestCase) -> None:
        self._testcases.append(testcase)

    def all_passed(self) -> bool:
        return self._passed == len(self._testcases) and not self._passed == 0

    def run(self) -> None:
        for testcase in self._testcases:
            testcase.run()

            match testcase.result:
                case TestCase.PASS:
                    self._passed += 1
                case TestCase.FAIL:
                    self._failed += 1
                case TestCase.ERROR:
                    self._error += 1

            ConsoleLogger.log_test_result(testcase=testcase)
