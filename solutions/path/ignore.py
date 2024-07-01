from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root

_GITIGNORE_FILE = ".gitignore"


class IgnoreManager(Singleton):

    @staticmethod
    def _find_gitignore(root: Root) -> Path:
        pass

    __slots__ = ("_ignore_list",)

    def __init__(self) -> None:
        self._ignore_list = []
