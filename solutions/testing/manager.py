from solutions.classes.singleton import Singleton
from solutions.root import PyMainRoot
from solutions.testing.runner import TestRunner

_PYMAIN_ROOT = PyMainRoot()


class TestManager(Singleton):

    __slots__ = tuple()

    def __init__(self, *, project_root=_PYMAIN_ROOT) -> None:
        TestRunner()._root = project_root
