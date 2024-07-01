from types import ModuleType
from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root
from solutions.path.tree import Tree
from solutions.testing.testcase import PyMainTestCase
from solutions.testing.testpack import PyMainTestPack


class TestRunner(Singleton):

    @staticmethod
    def _project_root() -> Root:
        raise NotImplementedError

    __slots__ = ("_root", "_test_pack")

    def __init__(self) -> None:
        self._root: Root = self._project_root().root
        self._test_pack = PyMainTestPack()

    def _load_test_from_module(self, *, module_name: str) -> None:
        module: ModuleType = __import__(name=module_name, fromlist=[module_name])

        for obj in module.__dict__.values():
            if isinstance(obj, PyMainTestCase):
                self._test_pack.add_testcase(testcase=obj)

    def _load_tests_from_path(self, *, file_path: Path) -> None:
        module_name = file_path.module_form(root=self._root)
        self._load_test_from_module(module_name=module_name)

    def _load_tests_from_tree(self, *, tree: Tree) -> None:
        for module_name in tree.get_module_forms():
            self._load_test_from_module(module_name=module_name)

    def run_local(self, file: str) -> None:
        self._test_pack = PyMainTestPack()
        file_path = Path.from_string(path_str=file)
        self._load_tests_from_path(file_path=file_path)
        self._test_pack.run()

    def run_tree(self, tree: Tree) -> None:
        self._test_pack = PyMainTestPack()
        self._load_tests_from_tree(tree=tree)
        self._test_pack.run()
