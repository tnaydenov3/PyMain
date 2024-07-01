from solutions.path.ignore import IgnoreManager
from solutions.path.tree import Tree
from solutions.root import PyMainRoot
from solutions.testing.runner import TestRunner


class PyMainIgnoreManager(IgnoreManager):

    @staticmethod
    def _project_root() -> PyMainRoot:
        return PyMainRoot()

    __slots__ = tuple()


class PyMainTestRunner(TestRunner):

    @staticmethod
    def _project_root() -> PyMainRoot:
        return PyMainRoot()

    __slots__ = tuple()


class PyMainTree(Tree):

    @staticmethod
    def _project_root() -> PyMainRoot:
        return PyMainRoot()

    @staticmethod
    def _project_ignore_manager() -> PyMainIgnoreManager:
        return PyMainIgnoreManager()

    __slots__ = tuple()
