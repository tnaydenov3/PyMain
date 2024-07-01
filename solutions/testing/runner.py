from types import ModuleType
from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root
from solutions.testing.testcase import TestCase
from solutions.testing.testpack import TestPack


class TestRunner(Singleton):

    __slots__ = ("_root", "_test_pack")

    def __init__(self) -> None:
        self._root: Root = None
        self._test_pack = TestPack()

    def _load_tests_from_path(self, *, file_path: Path) -> None:
        module_name = file_path.module_form(root=self._root)
        module: ModuleType = __import__(module_name)

        for obj in module.__dict__.values():
            if isinstance(obj, TestCase):
                self._test_pack.add_testcase(testcase=obj)

    def _run_tests_from_path(self, path: Path) -> None:
        self._load_tests_from_path(file_path=path)
        self._test_pack.run()

    def run_local(self, file: str) -> None:
        self._test_pack = TestPack()
        file_path = Path.from_string(path_str=file)
        self._run_tests_from_path(file_path=file_path)
