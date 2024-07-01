from solutions.project import PyMainTree
from solutions.testing.runner import TestRunner


class Commands:

    @staticmethod
    def run_project_tests() -> None:
        TestRunner().run_tree(tree=PyMainTree.get_project_tree())

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
