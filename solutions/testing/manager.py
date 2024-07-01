from solutions.classes.singleton import Singleton
from solutions.root import PyMainRoot
from solutions.testing.runner import TestRunner

_PYMAIN_ROOT = PyMainRoot()


class TestManager(Singleton):

    @staticmethod
    def _implemented() -> bool:
        raise NotImplementedError

    __slots__ = tuple()

    def __init__(self, *, project_root=_PYMAIN_ROOT) -> None:
        assert self._implemented()
        TestRunner()._root = project_root


class PyMainTestManager(TestManager):

    @staticmethod
    def _implemented() -> bool:
        return True

    __slots__ = tuple()
