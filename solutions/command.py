from typing import Any
from solutions.project import PyMainTree
from solutions.testing.runner import TestRunner


class Commands:

    TEST = "test"

    @staticmethod
    def run_project_tests() -> None:
        TestRunner().run_tree(tree=PyMainTree.get_project_tree())

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError


class CommandCall:

    _COMMANDS = {Commands.TEST: Commands.run_project_tests}

    def __call__(self, command: str, /) -> None:
        func = self._COMMANDS[command]
        func()

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
