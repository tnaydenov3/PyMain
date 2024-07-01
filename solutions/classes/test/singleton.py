from solutions.classes.singleton import Singleton
from solutions.testing.runner import TestRunner
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
    s_class_one, _ = _init_test()

    obj_1 = s_class_one()
    obj_2 = s_class_one()

    assert obj_1 is obj_2


@PyMainTestCase
def test_singleton_diff_class() -> None:
    s_class_one, s_class_two = _init_test()

    obj_1 = s_class_one()
    obj_2 = s_class_two()

    assert not obj_1 is obj_2


if __name__ == "__main__":
    TestRunner().run_local(file=__file__)
