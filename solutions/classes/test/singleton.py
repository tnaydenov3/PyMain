from solutions.classes.singleton import Singleton
from solutions.testing.testcase import TestCase


def _init_test() -> None:
    class SingletonOne(Singleton):

        def __init__(self) -> None:
            pass

    class SingletonTwo(Singleton):

        def __init__(self) -> None:
            pass

    return SingletonOne, SingletonTwo


@TestCase
def test_singleton() -> None:
    pass
