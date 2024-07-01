from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root
from solutions.testing.testpack import TestPack


class TestRunner(Singleton):

    __slots__ = ("_root",)

    def __init__(self, root: Root) -> None:
        self._root = root.root

    def _load_local_tests(self, file_path: Path) -> TestPack:
        pass
