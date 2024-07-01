from solutions.path.ignore import IgnoreManager
from solutions.root import PyMainRoot
from solutions.testing.manager import TestManager


class PyMainIgnoreManager(IgnoreManager):

    @staticmethod
    def _project_root() -> PyMainRoot:
        return PyMainRoot()

    __slots__ = tuple()


class PyMainTestManager(TestManager):

    @staticmethod
    def _implemented() -> bool:
        return True

    __slots__ = tuple()
