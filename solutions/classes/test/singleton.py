from solutions.classes.singleton import Singleton
from solutions.testing.testcase import PyMainTestCase


def _init_test() -> None:
    class SingletonOne(Singleton):

        def __init__(self) -> None:
            pass

    class SingletonTwo(Singleton):

        def __init__(self) -> None:
            pass

    return SingletonOne, SingletonTwo


@PyMainTestCase
def test_singleton() -> None:
    pass
