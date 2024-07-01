from types import ModuleType
from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root
from solutions.testing.testcase import TestCase
from solutions.testing.testpack import TestPack


class TestRunner(Singleton):

    __slots__ = ("_root",)

    def __init__(self, root: Root) -> None:
        self._root = root.root

    def _load_tests_from_path(self, file_path: Path) -> TestPack:
        module_name = file_path.module_form(root=self._root)
        module: ModuleType = __import__(module_name)

        test_pack = TestPack()
        for obj in module.__dict__.values():
            if isinstance(obj, TestCase):
                test_pack.add_testcase(testcase=obj)

        return test_pack
