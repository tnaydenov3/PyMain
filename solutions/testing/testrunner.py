from solutions.testing.testpack import TestPack


class TestRunner:

    @staticmethod
    def _find_local_tests(file: str) -> TestPack:
        pass

    @staticmethod
    def run_local(file: str) -> None:
        pass

    @staticmethod
    def run_global(file) -> None:
        pass

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
